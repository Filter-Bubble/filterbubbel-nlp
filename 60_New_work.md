# Relevant work

[Deep contextualized word representations](https://arxiv.org/pdf/1802.05365)
Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, Luke Zettlemoyer

* add all layers of a pretrained BiLSTM language model to your task

[Exploring the limits of language modeling. CoRR abs/1602.02410](https://arxiv.org/abs/1602.02410)
Rafal Józefowicz, Oriol Vinyals, Mike Schuster, Noam Shazeer, and Yonghui Wu. 2016. 

* bigger is better: two layer LSTM with sufficient parameters (8192 - 1024)


[An improved neural network model for joint POS tagging and dependency parsing](https://arxiv.org/abs/1807.03955)
Dat Quoc Nguyen, Karin Verspoor

* combined POS + dependency parsing based on BiLSTM models.

Jointly Predicting Predicates and Arguments in Neural Semantic Role Labeling
Luheng He Kenton Lee Omer Levy Luke Zettlemoyer



# Setup experiments for 'flair'

* reuse trained language model for dutch

## Select data for unsupervised training data of language model

* question: AEM corpus is heavily processed, is that good/bad?


## Train language models

Chose a few sets of hyper parameters

Network desing for LM:
* 4K LSTM in one layer (pretrained model exisits)
* 4K LSTM in two layers
* 2K LSTM in two layers


## Experiment with single task learning

TODO look at examples in flair_dutch.
* Language model + single layer for POS
* Language model + single layer for NER


## Experiment with multi task learning

