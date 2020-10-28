# Integration with the Newsreader pipeline

[Documentation of existing pipeline](https://vu-rm-pip3.readthedocs.io/en/latest/)

And [our clone](https://github.com/Filter-Bubble/vu-rm-pip3).

These are the original components:
* NAF formatting: text2naf
* tokenizing: ixa-pipe-tok
* POS tagging, lemmatization and parsing: vua-alpino **replaced by stanza**
* named entity recognition: ixa-pipe-nerc
* named entity disambiguation: ixa-pipe-ned
* word sense disambiguation: vua-wsd
* time/date standardisation: vuheideltimewrapper
* predicate-matrix tagging: vua-ontotagging
* semantic role labelling: vua-srl-nl **to be replaced by stroll**
* factuality: multilingual_factuality
* opinion mining: opinion_miner_deluxePP
* event coreference: EventCoreference
* nominal event detection: vua-nominal-event-detection
* nominal event srl labelling: vua-srl-dutch-nominal-events
* FrameNet labelling: vua-framenet-classifier
* **Added: coreference resolution with e2e**



## Install existing pipeline

See the [installation scripts](https://github.com/Filter-Bubble/vu-rm-pip3/tree/master/scripts) from the vu-rm-pip3 pipeline.

# Components to updated

## Open issues

1. We use UD for dependencies etc. Where in the pipeline do we need to make changes?
2. We use conll (tab separated files) as output. Where do we convert to/from NAF?


## POS tagging, lemmatization and parsing
We replace the Alpino tagger with [a wrapper around the stanza tagger](https://github.com/Filter-Bubble/stanza_wrapper). 
Stanza finds POS tags, lemmas and dependencies, but not constituents. 
Stanza is trained on universal dependencies, not on Alpino dependencies.
Stanza creates the term layer, but never makes multi-token terms, so there will be a 1-to-1 mapping from tokens in the text layer to terms in the term layer.

TODO:
* use our Stanza trained on the large corpus

## semantic role labelling

TODO: 
* use Stroll
* map stroll SRL to NAF

## Coref
We have a [step in the pipeline ](https://github.com/Filter-Bubble/vu-rm-pip3/blob/master/scripts/bin/e2edutch.sh) to use e2e for coreference resolution.

TODO: 
* Also make step for Stroll.
* find out where in the pipeline this needs to be done.
* map stroll coref annotation to NAF
* Check if we can map the entities from other step (NER) to corefs
* Can we run multiple files in one go? Because loading embeddings takes much time



## Other pipeline steps
To do for the other pipeline steps:
- **ixa-pipe-nerc**	(text, terms -> entities) Could we also extract the named entities from Stanza? How does performance compare?
- **ixa-pipe-ned**	(entities-> entities) [Issue running this step](https://github.com/ixa-ehu/ixa-pipe-ned/issues/2)
- **vua-framenet-classifier**	(terms, srl, +vua-srl-nl,vua-ontotagging -> srl) Does this work on the stroll SRLs?
- **vua-nominal-event-detection**	(srl, terms-> srl) Does this work on the stroll SRL?
- **vua-srl-dutch-nominal-events**	(terms, dependencies, srl	+vua-nominal-event-detection ->	srl) Does this work on the stroll SRL and stanza dependencies?
- **vua-eventcoreference**	(srl, terms ->	coreferences) Does this work on the stroll SRL? 
- **opinion-miner**	(text, terms, deps, constituents, entities -> opinions) Can we make it work on top of stanza output (without constituents)?

