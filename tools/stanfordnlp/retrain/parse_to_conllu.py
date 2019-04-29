#!/usr/bin/env python3
import sys
import stanfordnlp

class InputError(Exception):
    def __init__(self, message):
        self.message = message

config = {
        'tokenize_pretokenized': True,
        'processors': 'tokenize,pos,lemma,depparse', # mwt
        'lang': 'nl',
        'tokenize_model_path': '/home/jiska/Code/ernie/resources/stanfordnlp_resources/nl_alpino_models/nl_alpino_tokenizer.pt',
        'pos_model_path': '/home/jiska/Code/ernie/tools/stanfordnlp/lista/stanfordnlp/saved_models/pos/nl_combined_tagger.pt',
        'pos_pretrain_path': '/home/jiska/Code/ernie/tools/stanfordnlp/lista/stanfordnlp/saved_models/pos/nl_combined.pretrain.pt',
        'lemma_model_path': '/home/jiska/Code/ernie/resources/stanfordnlp_resources/nl_alpino_models/nl_alpino_lemmatizer.pt',


        'depparse_model_path': '/home/jiska/Code/ernie/tools/stanfordnlp/lista/stanfordnlp/saved_models/depparse/nl_combined_parser.pt',
        'depparse_pretrain_path': '/home/jiska/Code/ernie/tools/stanfordnlp/lista/stanfordnlp/saved_models/depparse/nl_combined.pretrain.pt'
        }

nlp = stanfordnlp.Pipeline(**config)

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
