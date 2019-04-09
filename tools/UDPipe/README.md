# UDPipe baseline for CoNLL18 Shared task

Copied from their [website](http://ufal.mff.cuni.cz/udpipe/models#conll18_shared_task_baseline_ud_22_models).

We present the tagger, lemmatizer and parser performance, measured on the testing
portion of the data, evaluated in three different settings::

* using raw text only,
* using gold tokenization only,
* and using gold tokenization plus gold morphology (UPOS, XPOS, FEATS and Lemma).

| Treebank         | Mode           | Words | Sents | UPOS  | XPOS  | Feats | AllTags | Lemma | UAS   | LAS   |
| --------         | ----           | ----- | ----- | ----  | ----  | ----- | ------- | ----- | ----- | ----- |
| Dutch            | Raw text       | 99.8% | 77.6% | 91.4% | 88.1% | 89.3% | 87.0%   | 89.9% | 75.4% | 69.6% |
| Dutch            | Gold tok       | -     | -     | 91.8% | 88.8% | 89.9% | 87.7%   | 90.1% | 77.0% | 71.2% |
| Dutch            | Gold tok+morph | -     | -     | -     | -     | -     | -       | -     | 82.9% | 79.4% |
| Dutch-LassySmall | Raw text       |100.0% | 80.4% | 97.6% | -     | 97.2% | -       | 98.1% | 84.4% | 82.0% |
| Dutch-LassySmall | Gold tok       | -     | -     | 97.7% | -     | 97.4% | -       | 98.2% | 87.5% | 85.0% |
| Dutch-LassySmall | Gold tok+morph | -     | -     | -     | -     | -     | -       | -     | 89.7% | 87.4% |



## Model version 2.3

| Treebank         | Mode         | Words | Sents | UPOS  | XPOS  | UFeats | AllTags | Lemma | UAS   | LAS   | MLAS  | BLEX   |
| --------         | ----         | ----- | ----- | ----  | ----  | ------ | ------- | ----- | ---   | ---   | ----  | ----   |
| Dutch-Alpino     | Raw text     | 99.9% | 91.7% | 94.3% | 91.5% | 93.6%  | 90.8%   | 95.4% | 82.3% | 78.2% | 63.0% | 66.0%  |
| Dutch-Alpino     | Gold tok     | -     | -     | 94.4% | 91.6% | 93.6%  | 91.0%   | 95.5% | 83.1% | 78.9% | 63.9% | 66.9%  |
| Dutch-Alpino     | Gold tok+mor | -     | -     | -     | -     | -      | -       | -     | 86.6% | 83.1% | 75.1% | 76.2%  |
| Dutch-LassySmall | Raw text     | 99.7% | 74.5% | 94.1% | 91.8% | 93.7%  | 91.1%   | 95.5% | 79.9% | 75.9% | 63.3% | 64.3%  |
| Dutch-LassySmall | Gold tok     | -     | -     | 94.3% | 92.2% | 94.2%  | 91.5%   | 95.9% | 83.6% | 79.1% | 67.2% | 68.3%  |
| Dutch-LassySmall | Gold tok+mor | -     | -     | -     | -     | -      | -       | -     | 87.5% | 84.1% | 78.1% | 78.8%  |



## Retraining

# Recommended parameters

Recommended parameters for Dutch can be found here https://github.com/ufal/udpipe/tree/master/training/models-ud-2.0

# Train the tokenizer

Train the tagger
```
time ./udpipe/src/udpipe --train combined_model \
--tokenizer=none \
--tagger="models=2;templates_1=tagger;guesser_suffix_rules_1=8;guesser_enrich_dictionary_1=6;guesser_prefixes_max_1=0;use_lemma_1=0;use_xpostag_1=1;use_feats_1=1;provide_lemma_1=0;provide_xpostag_1=1;provide_feats_1=1;prune_features_1=0;templates_2=lemmatizer;guesser_suffix_rules_2=6;guesser_enrich_dictionary_2=4;guesser_prefixes_max_2=4;use_lemma_2=1;use_xpostag_2=0;use_feats_2=0;provide_lemma_2=1;provide_xpostag_2=0;provide_feats_2=0;prune_features_2=0" \
--parser=none \
--heldout=/home/jiska/Code/ernie/labelled/combined/dataset_dev.conllu \
/home/jiska/Code/ernie/labelled/combined/dataset_train.conllu 2> train_tagger.err | tee train_tagger.out
```

Kickstart the parser with word vectors, we will use the fasttext ones.

Train the parser:
```
time ./udpipe/src/udpipe --train combined_parser \
--tokenizer=none \
--tagger="from_model=file:combined_model" \
--parser="iterations=30;embedding_upostag=20;embedding_feats=20;embedding_xpostag=0;embedding_form=50;embedding_form_file=fasttext.model50.vec;embedding_lemma=0;embedding_deprel=20;learning_rate=0.01;learning_rate_final=0.001;l2=0.5;hidden_layer=200;batch_size=10;transition_system=projective;transition_oracle=dynamic;structured_interval=10" \
--heldout=/home/jiska/Code/ernie/labelled/combined/dataset_dev.conllu \
/home/jiska/Code/ernie/labelled/combined/dataset_train.conllu 2> train_parser.err | tee train_parser.out
```
