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
