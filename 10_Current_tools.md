# Current tools

Tool    | Year | Type                                           |    NER      |  POS      | Dependency parsing
---     | ---:                                            ---:  |   ---:      | ---:      | ---:
Alpino  | 2011 | Rulebased                                      |             | ~87.9     |  85?
Bert    | 2019 | Deep learning, autoencoder, Attention          |             |           |
Dupira  | 2012 | Rulebased                                      |             |           |  85
Flair   | 2019 | Deep learning, BiLSTM                          |    89.56    |  93.84    |
Frog    | 2007 | morphosyntactic tagger and parser for Dutch    |             |  96?      |  74.3
NLTK    |      |                                                |             |           | 
RNNTagger  |      | RNN                                         |             |    ?      | 
spaCy   | 2018 | machine learning                               |    86.88    |  91.45    | 
TreeTagger | 1995 | decision trees                              |             |    ?      | 

## [ALPINO](http://www.let.rug.nl/vannoord/alp/Alpino/)

Alpino is a dependency parser for Dutch, developed in the context of the PIONIER Project Algorithms for Linguistic Processing. The software is available under the conditions of the Gnu Lesser General Public License.


## [Bert](https://github.com/google-research/bert)

BERT, or Bidirectional Encoder Representations from Transformers, is a new method of pre-training language representations which obtains state-of-the-art results on a wide array of Natural Language Processing (NLP) tasks.
Publication, code, and trained networks have been made available by Google Research (Thanks!)

Provides models for English, and multilingual.


## [Dupira](https://ivdnt.org/downloads/taalmaterialen/tstc-dupira)

Dupira is een dependency parser voor het Nederlands, ontwikkeld aan de Radboud Universiteit in Nijmegen. Dupira is een regelgebaseerde parser, die uit de Dupiragrammatica, -lexicon en -facttables is gegenereerd met de AGFL-parsergenerator. Met behulp van de grammatica transduceert de parser zinnen naar dependency graphs. Dupira is ontwikkeld voor praktische toepassingen in information retrieval en informatiesystemen die een natuurlijke taalinterface nodig hebben. De beoogde gebruikers zijn eerder computerwetenschappers dan taalkundigen. Meer documentatie is te vinden in: Cornelis HA Koster (2013) "An Aboutness-based Dependency Parser for Dutch". Dit document wordt samen met Dupira gedistribueerd.


## [Flair](https://github.com/zalandoresearch/flair)

A very simple framework for state-of-the-art Natural Language Processing (NLP).
Some promising work on Dutch is [here](https://github.com/stefan-it/flair-experiments)
And details on the [Dutch Language Model used are here](https://github.com/stefan-it/flair-lms)


## [Frog](https://languagemachines.github.io/frog/)

Frog is an integration of memory-based natural language processing (NLP) modules developed for Dutch.


## [Natural Language Toolkit](https://www.nltk.org/)

Python based toolkit with lots of datasets included (one of which is the Alpino Dutch treebank).
[A tagger for Dutch build in NLTK](https://github.com/evanmiltenburg/Dutch-tagger) is on github, but it includes a disclaimer not to use it in production.


## [spaCy](https://spacu.io)

Dutch models are available [here](https://spacy.io/models/nl). From the link:
Dutch multi-task CNN trained on the Universal Dependencies and WikiNER corpus. Assigns context-specific token vectors, POS tags, dependency parse and named entities. Supports identification of PER, LOC, ORG and MISC entities.

To install dutch support after installation of spaCy:
```bash
$ pip install spacy
$ python -m spacy download nl_core_news_sm
```

LAS scores for english are between 89.66 and 90.97, NER F 85.86 and 86.62.
The Dutch sores are LAS 77.62 and NER F 87.02.

Assuming Dutch and English are "just as hard", and the only difference is due to amount of labelled data, we can expect some improvements.


## [TreeTagger](http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/)

The TreeTagger is a tool for annotating text with part-of-speech and lemma information. It was developed by Helmut Schmid in the TC project at the Institute for Computational Linguistics of the University of Stuttgart. The TreeTagger has been successfully used to tag German, English, French, Italian, Danish, Dutch, Spanish, Bulgarian, Russian, Portuguese, Galician, Greek, Chinese, Swahili, Slovak, Slovenian, Latin, Estonian, Polish, Romanian, Czech, Coptic and old French texts and is adaptable to other languages if a lexicon and a manually tagged training corpus are available.

Contains two versions for Dutch, one of which is trained on the Eindhoven corpus.

The tool is superceded by RNNTagger, from the same author.
