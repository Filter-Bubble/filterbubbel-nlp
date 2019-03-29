#!/usr/bin/env python3
import sys
import spacy

class InputError(Exception):
    def __init__(self, message):
        self.message = message

nlp = spacy.load('nl_core_news_sm')

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
    parsed = nlp(sentence.rstrip())
    json = parsed.to_json()

    print ('# sent_id = ', sent_id)
    print ('# text = ', json['text'])
    for token in json['tokens']:
        line = [] 

        # 1 id, starting at 1
        line.append('{}'.format(token['id'] + 1))

        # 2 form
        line.append('{}'.format(parsed[int(token['id'])]))

        # 3 lemma
        line.append('_')

        # 4 upos
        line.append(token['pos'])

        # 5 xpos
        line.append('_')

        # 6 feats
        line.append(token['tag'])

        # 7 head
        line.append('{}'.format(token['head'] + 1))

        # 8 deprel
        line.append(token['dep'])

        # 9 deps
        line.append('_')

        # 10 misc
        line.append('_')

        print ('\t'.join(line))
    print ()
