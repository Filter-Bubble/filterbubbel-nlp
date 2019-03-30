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

    print ('# sent_id =', sent_id)
    print ('# text =', sentence.rstrip())
    for token in parsed:
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
