# Retraining

WIP: the table below is still a work in progress.
Not all models were run equal (ie. gold/predicted POS for DEPS)


| Tool        | Test set | UPOS  | XPOS  | UFeats | Lemmas | UAS   | LAS   | CLAS  | MLAS  | BLEX  |
|-------------|----------|-------|-------|--------|--------|-------|-------|-------|-------|-------|
| AllenNLP    | Alpino   |       |  gold | 40.37  |        | 90.78 | 88.87 | 89.79 |       |       |
|             | Alpino   |  gold |       | 40.37  |        | 89.91 | 88.14 | 89.02 |       |       |
|             | Combined |       |  gold | 40.84  |        | 93.85 | 92.03 | 89.21 |       |       |
|             | Combined |  gold |       | 40.84  |        | 94.01 | 92.12 | 89.26 |       |       |
| Parser-v2   | Alpino   |  gold |  gold | 40.37  |        | 89.76 | 88.01 | 88.92 | 17.44 | 88.92 |
|             | Combined |  gold |  gold | 40.84  |        | 94.47 | 92.58 | 89.75 | 18.51 | 89.75 |
| UDPipe      | Alpino   | 96.57 | 94.99 | 96.59  | 97.33  | 82.97 | 79.50 | 76.69 | 72.10 | 73.64 |
|             | Combined | 97.64 | 96.58 | 97.44  | 98.31  | 86.42 | 83.34 | 78.74 | 74.72 | 76.80 |
| jPTDP       | Alpino   |       |       |        |        |       |       |       |       |       |
|             | Combined |       |       |        |        |       |       |       |       |       |
| StanfordNLP | Alpino   | 97.74 | 96.73 | 97.93  |        | 89.22 | 87.07 | 87.58 | 86.93 | 87.58 |
|             | Combined | 97.83 | 97.03 | 97.94  | 96.59  | 91.74 | 88.95 | 85.15 | 81.41 | 80.36 |
| Spacy       | Alpino   | 80.40 |       | 40.37  |        | 80.15 | 77.28 | 71.79 | 14.99 |  0.00 |
|             | Combined | 81.94 |       | 40.84  |        | 83.81 | 81.17 | 72.56 | 16.45 |  0.00 |


Models retrained on the combined Lassy and Alpino treebanks, always using gold tokenization.
Where applicable, wordvectors from Fasttext trained on the AEM corpus are used.

StanfordNLP:
used predicted POS for training DEP
Lemmas done using original lemmatizer trained on alpino dataset.
check: scores for DEP are for using gold POS

UDPipe:
used predicted POS for training DEP.
scores for the whole pipeline

Spacy:
trained POS and DEP simulateously
scores for the whole pipeline


# Pre-trained word vectors

## Static word vectors

For (re)training some of the tools, we can use word embeddings for an extra few percent performance.
Either glove, word2vec, or fasttext embeddings are used, with a typical dimension of 100.
I trained vectors with each tool on the AEM corpus.

A (simplistic) evaluation of the three vector sets is in the table below, following "Evaluating Unsupervised Dutch Word Embeddings as a Linguistic Resource" by Stephan Tulkens, Chris Emmery, Walter Daelemans (see the README's in the resources directory for more details.)

|                    |  glove   | w2v   | fasttext-50 | fasttext-100 | paper |
|--------------------|----------|-------|-------------|--------------|------ |
|comparative         |  47.90   | 62.94 |   36.22     |  62.44       | 76.6  |
|currency            |   5.51   | 11.40 |    9.56     |  13.60       | 15.0  |
|gender              |  54.71   | 58.33 |   42.21     |  54.53       | 75.9  |
|nationalities       |  14.86   | 26.99 |   24.09     |  31.34       | 21.6  |
|pasttense           |  54.21   | 60.24 |   57.54     |  68.10       | 68.3  |
|superlative         |  12.33   | 28.00 |   15.17     |  29.67       | 39.9  |
|country             |  59.16   | 58.18 |   50.53     |  59.08       | 52.1  |
|diminutives         |  12.32   | 16.85 |   17.75     |  34.06       | 44.9  |
|infinitive          |  24.26   | 33.99 |   28.57     |  45.69       | 65.0  |
|opposites           |   8.68   | 11.58 |   21.32     |  26.84       | 22.1  |
|plural              |  41.09   | 35.03 |   29.50     |  48.31       | 57.4  |
|Total accuracy      |  37.95   | 43.59 |   35.41     |  49.63       | 51.3  |

Questions seen/total: 85.85% (8624/10046)

## Contextualilzed Word vectors

[Exploring the limits of language modeling. CoRR abs/1602.02410](https://arxiv.org/abs/1602.02410)
Rafal Józefowicz, Oriol Vinyals, Mike Schuster, Noam Shazeer, and Yonghui Wu. 2016.

* bigger is better for a language model: two layer LSTM with sufficient parameters (8192 - 1024)

### Elmo

[Deep contextualized word representations](https://arxiv.org/pdf/1802.05365)
Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, Luke Zettlemoyer

* add all layers of a pretrained BiLSTM language model to your task

Many pretrained models are [available here](https://github.com/HIT-SCIR/ELMoForManyLangs/tree/master/elmoformanylangs)

### [Bert](https://github.com/google-research/bert)

BERT, or Bidirectional Encoder Representations from Transformers, is a new method of pre-training language representations which obtains state-of-the-art results on a wide array of Natural Language Processing (NLP) tasks.
Publication, code, and trained networks have been made available by Google Research (Thanks!)

Provides models for English, and multilingual.

### [Flair](https://github.com/zalandoresearch/flair)

[Contextual String Embeddings for Sequence Labeling](https://aclanthology.info/papers/C18-1139/c18-1139)
Alan Akbik | Duncan Blythe | Roland Vollgraf

A very simple framework for state-of-the-art Natural Language Processing (NLP).
Some promising work on Dutch is [here](https://github.com/stefan-it/flair-experiments)
And details on the [Dutch Language Model used are here](https://github.com/stefan-it/flair-lms)
POS from BiLSTM charater models (code - flair)


# State-of-the-art networks (for English)


## POS + Dependency Parsing

[Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations](https://arxiv.org/abs/1603.04351)
Eliyahu Kiperwasser, Yoav Goldberg

* dependency parse from POS using simple BiLSTM network
* Code available, including several reimplementations (pyTorch)

Implemented with some extensions in jPTDT


[Deep Biaffine Attention for Neural Dependency Parsing](https://arxiv.org/abs/1611.01734)
Timothy Dozat, Christopher D. Manning

* graph based dependency parser based on BiLSTM, pretrained wordvectors

Implemented in [Parser-v2](https://github.com/tdozat/Parser-v2).
Also implemented in AllenNLP, but only the dependency parsing.


## SRL

Jointly Predicting Predicates and Arguments in Neural Semantic Role Labeling
Luheng He Kenton Lee Omer Levy Luke Zettlemoyer (no code)

Dependency or Span, End-to-End Uniform Semantic Role Labeling
Zuchao Li 1,2,∗ , Shexia He 1,2,∗ , Hai Zhao 1,2,† , Yiqing Zhang 1,2 , Zhuosheng Zhang 1,2 , Xi Zhou 3 , Xiang Zhou 3

Dependency-based Semantic Role Labeling of PropBank
Richard Johansson and Pierre Nugues

A Simple and Accurate Syntax-Agnostic Neural Model for Dependency-based Semantic Role Labeling
Diego Marcheggiani 1 , Anton Frolov 2 , Ivan Titov 1,3


## Co-Reference resolution


