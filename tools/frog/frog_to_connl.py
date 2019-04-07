#!/usr/bin/env python3
import sys
import warnings

# Frog output fields:
# 0 Token number (resets every sentence)
# 1 Token
# 2 Lemma (according to MBLEM)
# 3 Morphological segmentation (according to MBMA)
# 4 PoS tag (CGN tagset; according to MBT)
# 5 Confidence in the POS tag, a number between 0 and 1, representing the probability mass assigned to the best guess tag in the tag distribution
# 6 Named entity type, identifying person (PER), organization (ORG), location (LOC), product (PRO), event (EVE), and miscellaneous (MISC), using a BIO (or IOB2) encoding
# 7 Base (non-embedded) phrase chunk in BIO encoding
# 8 Token number of head word in dependency graph (according to CSI-DP)
# 9 Type of dependency relation with head word
INDEX, TEXT, LEMMA, MORPH, POS, CONF, NER, PHRASE, DEPINDEX, DEP = range(10)

class InputError(Exception):
    def __init__(self, message):
        self.message = message

# bare                                  full
# no ner, no mwu, no dep, no depindex # with ner, mwu, but also dep, depindex
# 1    Wat              wat           #  1    Wat             wat
# 2    was              zijn          #  2    was             zijn
# 3    het              het           #  3    het             het
# 4    succesvolste     successvol    #  4    succesvolste    succesvol
# 5    jaar             jaar          #  5    jaar            jaar
# 6    voor             voor          #  6    voor            voor
# 7    The              The           #  7    The_Beatles     The_Beatles
# 8    Beatles          Beatles       #  8    ,               ,
# 9    ,                ,             #  9    gemeten         meten
# 10   gemeten          meten         # 10    in              in
# 11   in               in            # 11    aantal          aantal
# 12   aantal           aantal        # 12    verkochte       verkopen
# 13   verkochte        verkopen      # 13    platen          plaat
# 14   platen           plaat         # 14    ?               ?
# 15   ?                ?    
def align_sentence(bare_sentence, full_sentence):
    # Assumption: some tokens have been merged with an '_'
    #  - len(full_sentence) < len(bare_sentence)
    #  - text and ordering have not been changed,
    #    '_'.join() for full and bare sentences match
    
    # We will look up the head by:
    # (1) matching a bare token (left), to a fully annotated token (right).
    # (2) Then find the full token that is the right head via the token[DEPINDEX]
    # (3) Then match it back to abare token (left)

    # build mapping bare <-> full
    b_to_f = {} # index of bare token to index of full token
    f_to_b = {} # string of full token INDEX to string of bare token INDEX

    ibare = 0
    ifull = 0
    while True:
        if ibare == len(bare_sentence):
            break
        if ifull == len(full_sentence):
            print ("Error...")
            return False
            break

        bare = bare_sentence[ibare]
        full = full_sentence[ifull]

        # Create links between the two tokens
        b_to_f[ibare] = ifull
        f_to_b[full[INDEX]] = bare[INDEX]
      
        # Move to the next tokens
        if bare[TEXT] == full[TEXT]:
            # TEXT matches, as would be the case for tokens 1-6 above
            # go to the next full token
            ibare += 1
            ifull += 1
        elif bare[TEXT] in full[TEXT].split('_'):
            # the TEXT has been merged into an MWU or NE, 
            # as tokens 7 and 8 both map to 7
            # dont go to the next full token
            ibare += 1
        else:
            # the TEXT has not been merged in, so should match
            # with the next full token
            ifull += 1

    for ibare, bare in enumerate(bare_sentence):
        # find the matching full token
        full = full_sentence[b_to_f[ibare]]

        # append its DEPINDEX to the bare token index 9,
        # but be careful with root as that points outside
        # of the sentence
        fullhead = full[DEPINDEX]
        if int(fullhead) == 0:
            bare.append('0')
        else:
            bare.append(f_to_b[fullhead])

        # append the relation as index 10
        bare.append(full[DEP])

    return True

def token_to_conllu(token):
    # convert frogs pos to UPOS and FEATS
    try:
        upos, feats = cgn_to_ud[token[POS]]
    except KeyError:
        warnings.warn('Unknown frog pos: {}'.format(token[POS]))
        upos, feats = '_', '_'

    conllu = []

    # 1 id, starting at 1
    conllu.append('{}'.format(token[INDEX]))

    # 2 form
    conllu.append('{}'.format(token[TEXT]))

    # 3 lemma
    conllu.append('{}'.format(token[LEMMA]))

    # 4 upos
    conllu.append(upos)

    # 5 xpos
    conllu.append('_')

    # 6 feats
    conllu.append(feats)

    # 7 head
    if len(token) > DEPINDEX:
        conllu.append('{}'.format(token[DEPINDEX]))
    else:
        conllu.append('_')

    # 8 deprel
    if len(token) > DEP:
        conllu.append(token[DEP])
    else:
        conllu.append('_')

    # 9 deps
    conllu.append('_')

    # 10 misc
    conllu.append('_')

    return '\t'.join(conllu)



# Initialize connl output
# Conversion from the tagset of frog to one of the Universal Dependencies
# frog's tag                     upos feature
# N(soort,ev,basis,zijd,stan) => NOUN Case=Acc,Nom|Degree=Pos|Gender=Com|Number=Sing
cgn_to_ud = {}
with open('cgn_to_upos.txt') as f:
    lines = f.readlines()
    for line in lines:
        fields = line.rstrip().split('\t')
        cgn_to_ud[fields[0]] = (fields[2], fields[3])

with open('full_parse', 'r') as f:
    full_parse_contents = f.readlines()
    full_parse = iter(full_parse_contents)

with open('bare_parse', 'r') as f:
    bare_parse_contents = f.readlines()
    bare_parse = iter(bare_parse_contents)

f = open('total_parse', 'w')

print ("Read {} lines from bare parse, and {} lines from full parse".format(len(bare_parse_contents), len(full_parse_contents)))

try:
    while True:
        # read the sentence from the full parse
        full_sentence = []
        while True:
            line = next(full_parse).rstrip()
            if len(line) == 0:
                break

            # parse the token
            token = line.split('\t')

            # append token to current sentence
            full_sentence.append(token)

        # read the sentence from the bare parse
        bare_sentence = []
        while True:
            line = next(bare_parse).rstrip()
            if len(line) == 0:
                break

            # parse the token
            token = line.split('\t')

            # append token to current sentence
            bare_sentence.append(token)

        # align them
        align_sentence(bare_sentence, full_sentence)

        # write sentence to file
        for token in bare_sentence:
            conllu = token_to_conllu(token)
            print (conllu, file=f)
        print ("\n", file=f)

except StopIteration:
    pass
