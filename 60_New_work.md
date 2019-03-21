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

