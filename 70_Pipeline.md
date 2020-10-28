# Integration with the Newsreader pipeline

[Documentation of existing pipeline](https://vu-rm-pip3.readthedocs.io/en/latest/)

* NAF formatting: text2naf
* tokenizing: ixa-pipe-tok
* POS tagging, lemmatization and parsing: vua-alpino
* named entity recognition: ixa-pipe-nerc
* named entity disambiguation: ixa-pipe-ned
* word sense disambiguation: vua-wsd
* time/date standardisation: vuheideltimewrapper
* predicate-matrix tagging: vua-ontotagging
* semantic role labelling: vua-srl-nl
* factuality: multilingual_factuality
* opinion mining: opinion_miner_deluxePP
* event coreference: EventCoreference
* nominal event detection: vua-nominal-event-detection
* nominal event srl labelling: vua-srl-dutch-nominal-events
* FrameNet labelling: vua-framenet-classifier

## Install existing pipeline

TODO: links to install scripts from github

# Components to updated

## Open issues

1. We use UD for dependencies etc. Where in the pipeline do we need to make changes?
2. We use conll (tab separated files) as output. Where do we convert to/from NAF?


## POS tagging, lemmatization and parsing

TODO:
* use our Stanza trained on the large corpus

## semantic role labelling

TODO: 
* use Stroll

## Coref

TODO: 
* use e2e and/or Stroll.
* find out where in the pipeline this needs to be done.






