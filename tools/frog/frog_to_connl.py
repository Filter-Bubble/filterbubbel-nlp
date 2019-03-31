#!/usr/bin/env python3

import sys
import warnings
import frog

class InputError(Exception):
    def __init__(self, message):
        self.message = message

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

# Initialize frog
frog = frog.Frog(frog.FrogOptions(tok=True, parser=True))

# Parse all sentences from stdin
for idsent in sys.stdin:
    # input as:  sentid|sentence

    # output as: # sent_id =
    #            # text =
    #            1 ...
    #            2 ...
    #            3 ...
    pipe = idsent.find('|')
    if pipe == -1:
        raise InputError("Invalid input")

    sent_id = idsent[:pipe]

    sentence = idsent[pipe+1:]
    parsed = frog.process(sentence.rstrip())

    # The frog tokenizer does some multi word unit tricks (see token 12)
    # Truning is it off makes frog crash, so try to split mwu manually

    # # sent_id = LassySmall5_WR-P-P-H-0000000105_WR-P-P-H-0000000105.p.6.s.1
    # # text = De afgelopen week twijfelde ze nog of ze wel moest meedoen aan het NK .
    # 1	De	de	DET	_	Case=Acc,Nom|Definite=Def|Gender=Com|Number=Plur|PronType=Art	3	det	_	_
    # 2	afgelopen	aflopen	VERB	_	Aspect=Perf|Position=Prenom|Tense=Past|VerbForm=Part	3	mod	_	_
    # 3	week	week	NOUN	_	Case=Acc,Nom|Degree=Pos|Gender=Com|Number=Sing	4	mod	_	_
    # 4	twijfelde	twijfelen	VERB	_	Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin	0	ROOT	_	_
    # 5	ze	ze	PRON	_	Case=Acc,Nom|Gender=Fem|Number=Sing|Person=3|PronType=Prs|Variant=Short	4	su	_	_
    # 6	nog	nog	ADV	_	_	4	mod	_	_
    # 7	of	of	SCONJ	_	_	4	vc	_	_
    # 8	ze	ze	PRON	_	Case=Acc,Nom|Gender=Fem|Number=Sing|Person=3|PronType=Prs|Variant=Short	10	su	_	_
    # 9	wel	wel	ADV	_	_	10	None	_	_
    # 10	moest	moeten	VERB	_	Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin	7	body	_	_
    # 11	meedoen	meedoen	VERB	_	Position=Free|VerbForm=Inf	10	vc	_	_
    # 12	aan_het	aan_het	_	_	_	11	vc	_	_
    # 13	NK	NK	_	_	_	12	body	_	_
    # 14	.	.	PUNCT	_	_	13	punct	_	_


    parsed_nomwu = []
    for i in range(len(parsed)):
        token = parsed[i]

        # is it a mwu?
        if token['lemma'].find('_') != -1:
            subpos = token['pos'].split('_')
            subtext = token['text'].split('_')
            sublemma = token['lemma'].split('_')
            subpos = token['pos'].split('_')

            # we add len(submlemma) tokens, but remove the original one
            shift = len(sublemma) - 1

            # adjust the heads on the parsed tokens
            for j in range(len(parsed_nomwu)):
                depindex = int(parsed_nomwu[j]['depindex'])
                if depindex >= i:
                    parsed_nomwu[j]['depindex'] = depindex + shift

            # adjust the heads and indexes on the original tokens
            current_index = int(token['index'])
            for j in range(len(parsed)):
                depindex = int(parsed[j]['depindex'])
                if depindex >= current_index:
                    parsed[j]['depindex'] = depindex + shift

                index = int(parsed[j]['index'])
                if index > current_index:
                    parsed[j]['index'] = index + shift

            # split the mwu token in single tokens
            for j in range(len(sublemma)):
                subtoken = {}
                subtoken['index'] = int(token['index']) + j
                subtoken['text'] = subtext[j]
                subtoken['lemma'] = sublemma[j]
                subtoken['pos'] = subpos[j]
                # take the head of the token as the head of the subtoken
                # TODO: make a better guess?
                subtoken['depindex'] = token['depindex']
                subtoken['dep'] = token['dep']
                parsed_nomwu.append(subtoken)
        else:
            parsed_nomwu.append(token)

    print ('# sent_id =', sent_id)
    print ('# text =', sentence.rstrip())
    for token in parsed_nomwu:
        # Frog's python API returns an array of:
        # 'chunker': 'B-NP'
        # 'morph': '[dit]'
        # 'index': '1'
        # 'text': 'Dit'
        # 'depindex': '2'
        # 'ner': 'O'
        # 'posprob': 0.777085
        # 'lemma': 'dit'
        # 'dep': 'su'
        # 'pos': 'VNW(aanw,pron,stan,vol,3o,ev)

        # convert frogs pos to UPOS and FEATS
        try:
            upos, feats = cgn_to_ud[token['pos']]
        except KeyError:
            warnings.warn('Unknown frog pos: {}'.format(token['pos']))
            upos, feats = '_', '_'

        line = []

        # 1 id, starting at 1
        line.append('{}'.format(token['index']))

        # 2 form
        line.append('{}'.format(token['text']))

        # 3 lemma
        line.append('{}'.format(token['lemma']))

        # 4 upos
        line.append(upos)

        # 5 xpos
        line.append('_')

        # 6 feats
        line.append(feats)

        # 7 head
        line.append('{}'.format(token['depindex']))

        # 8 deprel
        line.append(token['dep'])

        # 9 deps
        line.append('_')

        # 10 misc
        line.append('_')

        print ('\t'.join(line))
    print ()
