#!/usr/bin/env python3
import sys
import stanfordnlp

class InputError(Exception):
    def __init__(self, message):
        self.message = message

nlp = stanfordnlp.Pipeline(lang="nl")

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

    sentence = idsent[pipe+1:].rstrip()
    doc = nlp(sentence)

    # HACK: write out as conllu and reread...
    doc.write_conll_to_file('/tmp/conllu')
    with open('/tmp/conllu') as f:
        lines = f.readlines()

    print ('# sent_id =', sent_id)
    print ('# text =', sentence)
    print ("".join(lines))
