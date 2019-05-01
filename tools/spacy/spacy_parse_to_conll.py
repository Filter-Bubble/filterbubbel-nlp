#!/usr/bin/env python3
import sys
import spacy

class InputError(Exception):
    def __init__(self, message):
        self.message = message

# See here for a possible issue and fix for unwanted sentence splitting:
# https://github.com/explosion/spaCy/issues/1032
#def prevent_sentence_boundary_detection(doc):
#    for token in doc:
#        # This will entirely disable spaCy's sentence detection
#        token.is_sent_start = False
#    return doc
#
#nlp.add_pipe(prevent_sentence_segmentation, name='prevent-sbd', before='parser')

nlp = spacy.load('/home/jiska/Code/ernie/tools/spacy/retrain/retrain-dataset/model-best')

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
    # dont run the pipeline; we do not want any tokenization
    # doc = nlp(sentence.rstrip())
    
    doc = nlp.tokenizer.tokens_from_list(sentence.rstrip().split(' '))
    nlp.tagger(doc)
    nlp.parser(doc)

    json = doc.to_json()

    print ('# sent_id = ', sent_id)
    print ('# text = ', json['text'])

    for token in json['tokens']:
        line = [] 

        # 1 id, starting at 1
        line.append('{}'.format(token['id'] + 1))

        # 2 form
        line.append('{}'.format(doc[int(token['id'])]))

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
