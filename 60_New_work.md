# Research tools

Recent papers and software to investigate:
Bert
Flair
ELMO

TODO:
AllenNLP
CoreNLP


## [Bert](https://github.com/google-research/bert)

BERT, or Bidirectional Encoder Representations from Transformers, is a new method of pre-training language representations which obtains state-of-the-art results on a wide array of Natural Language Processing (NLP) tasks.
Publication, code, and trained networks have been made available by Google Research (Thanks!)

Provides models for English, and multilingual.


# Relevant work

## Lanuage models

[Exploring the limits of language modeling. CoRR abs/1602.02410](https://arxiv.org/abs/1602.02410)
Rafal Józefowicz, Oriol Vinyals, Mike Schuster, Noam Shazeer, and Yonghui Wu. 2016.

* bigger is better: two layer LSTM with sufficient parameters (8192 - 1024)


### Elmo

[Deep contextualized word representations](https://arxiv.org/pdf/1802.05365)
Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, Luke Zettlemoyer

The Elmo paper
* add all layers of a pretrained BiLSTM language model to your task

Many pretrained models are [available here](https://github.com/HIT-SCIR/ELMoForManyLangs/tree/master/elmoformanylangs)


## POS

[Contextual String Embeddings for Sequence Labeling](https://aclanthology.info/papers/C18-1139/c18-1139)
Alan Akbik | Duncan Blythe | Roland Vollgraf

* POS from BiLSTM charater models (code - flair)

An implementation is available: [Flair](https://github.com/zalandoresearch/flair)

A very simple framework for state-of-the-art Natural Language Processing (NLP).
Some promising work on Dutch is [here](https://github.com/stefan-it/flair-experiments)
And details on the [Dutch Language Model used are here](https://github.com/stefan-it/flair-lms)


## Dependency Parsing

[Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations](https://arxiv.org/abs/1603.04351)
Eliyahu Kiperwasser, Yoav Goldberg

* dependency parse from POS using simple BiLSTM network
* Code available, including several reimplementations (pyTorch)


## POS + Dependency

[Deep Biaffine Attention for Neural Dependency Parsing](https://arxiv.org/abs/1611.01734)
Timothy Dozat, Christopher D. Manning

* graph based dependency parser based on BiLSTM, pretrained wordvectors
* code available (Parser-v1), based on tenforflow


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

