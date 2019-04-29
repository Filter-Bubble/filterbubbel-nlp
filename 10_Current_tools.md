# Current tools

## Part-of-speech and dependencies

| Tool        | Year | Test set |  Tokens | UPOS  | XPOS  | UFeats | Lemmas | UAS   | LAS   | CLAS  | MLAS  | BLEX  |
|-------------|-----:|----------|---------|-------|-------|--------|--------|-------|-------|-------|-------|-------|
| Alpino      | 2011 | Alpino   |  99.98  | 96.71 | 95.87 | 97.24  | 90.08  | 88.28 | 86.35 | 87.32 | 83.57 | 72.97 |
|             |      | Combined |   gold  | 95.97 | 94.45 | 96.11  | 90.98  | 90.90 | 88.63 | 85.45 | 79.93 | 73.05 |
| StanfordNLP | 2018 | Alpino   |  99.71  | 96.17 | 94.32 | 96.00  | 96.30  | 90.10 | 86.93 | 82.07 | 75.74 | 76.97 |
|             |      | Combined |   gold  | 96.32 | 94.89 | 96.16  | 96.61  | 87.53 | 84.20 | 83.27 | 77.22 | 78.91 |
| jPTDP       | 2018 | Alpino   |   gold  | 95.62 |       |        |        | 86.36 | 82.25 | 75.65 | 70.58 | 75.65 |
|             |      | Combined |   gold  | 95.84 |       |        |        | 83.20 | 79.49 | 76.74 | 72.45 | 76.74 |
| UDPipe      | 2018 | Alpino   |  99.91  | 94.36 | 91.59 | 93.66  | 95.49  | 82.38 | 78.29 | 70.44 | 62.94 | 65.89 |
|             |      | Combined |   gold  | 95.05 | 92.65 | 94.36  | 96.19  | 81.07 | 76.87 | 72.77 | 66.30 | 68.84 |
| spaCy       | 2018 | Alpino   |  96.84  | 76.86 |       | 43.17  | 0.00   | 69.29 | 57.01 | 46.70 | 11.40 |  0.00 |
|             |      | Combined |  97.11  | 77.69 |       | 43.44  | 0.01   | 69.17 | 57.43 | 47.40 | 12.44 |  0.00 |
| Frog        | 2007 | Alpino   |  98.54  | 86.77 |       | 43.27  | 97.60  | 34.57 | 12.79 |       |       |       |
|             |      | Combined |   gold  | 86.56 |       | 42.52  | 97.47  | 35.12 | 12.01 |       |       |       |
| Dupira      | 2012 |          |         |       |       |        |        |       |       |       |       |       |







Models are run using published settings and pre-trained networks.
Scores are calculated using the UD evaluation script, and are the AlgindAcc scores.

*Alpino*
  Tokenization, part-of-speech tagging and dependency parsing evaluated on the *UD_Dutch_Alpino_test* set.

*Combined*
  Part-of-speech tagging and dependency parsing evaluated on the larger test set, created from the (full) LassySmall and Alpino sets. Gold standard pre-tokenized text was used.

## [UDPipe](http://ufal.mff.cuni.cz/udpipe)

UDPipe is a trainable pipeline for tokenization, tagging, lemmatization and dependency parsing of CoNLL-U files. UDPipe is language-agnostic and can be trained given annotated data in CoNLL-U format. Trained models are provided for nearly all UD treebanks. UDPipe is available as a binary for Linux/Windows/OS X, as a library for C++, Python, Perl, Java, C#, and as a web service. Third-party R CRAN package also exists.

UDPipe is a free software distributed under the Mozilla Public License 2.0 and the linguistic models are free for non-commercial use and distributed under the CC BY-NC-SA license, although for some models the original data used to create the model may impose additional licensing conditions. UDPipe is versioned using Semantic Versioning.

Copyright 2017 by Institute of Formal and Applied Linguistics, Faculty of Mathematics and Physics, Charles University, Czech Republic.

## [jPTDP](https://github.com/datquocnguyen/jPTDP.git)

[An improved neural network model for joint POS tagging and dependency parsing](https://arxiv.org/abs/1807.03955)
Dat Quoc Nguyen, Karin Verspoor

Our parsing component can be viewed as an extension of the BIST graph-based dependency model (Kiperwasser and Goldberg, 2016), where we additionally incorporate the character-level vector representations of words.
* combined POS + dependency parsing based on BiLSTM models, character embeddings (per word), and optional external word vectors.
* word vector (static, external) + forward character lm per word + backward character lm per word
* forward lstm + backward lstm for POS tags
* forward lstm + backward lstm for concat layer
* MLP + parse projection
* code available (jPTDP) for python using Dynet (cpu + gpu support)

## [ALPINO](http://www.let.rug.nl/vannoord/alp/Alpino/)

Alpino is a dependency parser for Dutch, developed in the context of the PIONIER Project Algorithms for Linguistic Processing. The software is available under the conditions of the Gnu Lesser General Public License.


## [Dupira](https://ivdnt.org/downloads/taalmaterialen/tstc-dupira)

Dupira is een dependency parser voor het Nederlands, ontwikkeld aan de Radboud Universiteit in Nijmegen. Dupira is een regelgebaseerde parser, die uit de Dupiragrammatica, -lexicon en -facttables is gegenereerd met de AGFL-parsergenerator. Met behulp van de grammatica transduceert de parser zinnen naar dependency graphs. Dupira is ontwikkeld voor praktische toepassingen in information retrieval en informatiesystemen die een natuurlijke taalinterface nodig hebben. De beoogde gebruikers zijn eerder computerwetenschappers dan taalkundigen. Meer documentatie is te vinden in: Cornelis HA Koster (2013) "An Aboutness-based Dependency Parser for Dutch". Dit document wordt samen met Dupira gedistribueerd.

TODO: convert / map dupira's parse to the conllu format


## [Frog](https://languagemachines.github.io/frog/)

Frog is an integration of memory-based natural language processing (NLP) modules developed for Dutch.

Note: There are some issues with output conversion (ie. in proper connlu with the same tagset, no multi word units), so the scores are a lower bound.


## [spaCy](https://spacu.io)

Dutch models are available [here](https://spacy.io/models/nl). From the link:
Dutch multi-task CNN trained on the Universal Dependencies and WikiNER corpus. Assigns context-specific token vectors, POS tags, dependency parse and named entities. Supports identification of PER, LOC, ORG and MISC entities.

To install dutch support after installation of spaCy:
```bash
$ pip install spacy
$ python -m spacy download nl_core_news_sm
```

For a general description of the alogrithms in spacy, [see this blog post](https://explosion.ai/blog/how-spacy-works).
An update for spacy 2.1 [is in another blog post](https://explosion.ai/blog/spacy-v2-1).

## [StanfordNLP](https://stanfordnlp.github.io/stanfordnlp/index.html)

StanfordNLP is a Python natural language analysis package. It contains tools, which can be used in a pipeline, to convert a string containing human language text into lists of sentences and words, to generate base forms of those words, their parts of speech and morphological features, and to give a syntactic structure dependency parse, which is designed to be parallel among more than 70 languages, using the Universal Dependencies formalism. In addition, it is able to call the CoreNLP Java package and inherits additonal functionality from there, such as constituency parsing, coreference resolution, and linguistic pattern matching.

This package is built with highly accurate neural network components that enable efficient training and evaluation with your own annotated data. The modules are built on top of PyTorch. You will get much faster performance if you run this system on a GPU-enabled machine. This package is a combination of software based on the Stanford entry in the CoNLL 2018 Shared Task on Universal Dependency Parsing, and the group’s official Python interface to the Java Stanford CoreNLP software. The CoNLL UD system is partly a cleaned up version of code used in the shared task and partly an approximate rewrite in PyTorch of the original Tensorflow version of the tagger and parser.

# Out of scope

## [TreeTagger](http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/)

The TreeTagger is a tool for annotating text with part-of-speech and lemma information. It was developed by Helmut Schmid in the TC project at the Institute for Computational Linguistics of the University of Stuttgart. The TreeTagger has been successfully used to tag German, English, French, Italian, Danish, Dutch, Spanish, Bulgarian, Russian, Portuguese, Galician, Greek, Chinese, Swahili, Slovak, Slovenian, Latin, Estonian, Polish, Romanian, Czech, Coptic and old French texts and is adaptable to other languages if a lexicon and a manually tagged training corpus are available.

Contains two versions for Dutch, one of which is trained on the Eindhoven corpus.

The tool is superceded by RNNTagger, from the same author.

The tool does only POS, no dependency parse.

## [Natural Language Toolkit](https://www.nltk.org/)

Python based toolkit with lots of datasets included (one of which is the Alpino Dutch treebank).
[A tagger for Dutch build in NLTK](https://github.com/evanmiltenburg/Dutch-tagger) is on github, but it includes a disclaimer not to use it in production.

## [Tadpole]()

An efficient memory-based morphosyntactic tagger and parser for Dutch
Antal van den Bosch, Bertjan Busser, Sander Canisius, Walter Daelemans

Superceeded by Frog.
