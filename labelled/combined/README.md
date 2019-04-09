# Combined corpus

This corpus contains all data from the UD treebanks LassySmall and Alpina, aswell as the heldout data from LassySmall.

Original text was lost for the LassySmall data; so an effort to detokenize has been made (following the UDPipe manual).
See also the scripts in this directory.

To make comparison with the Shared Tasks easier, the test dataset of Alpino, nl\_alpino-ud-test.conllu, has been excluded, and can serve as an extra (independent) set.

I could not find the untokenized input text, so all files contain gold tokenization.

## Description of files

Validated, conllu files, build using a 80/10/10 split:
*dataset_train.conllu*
*dataset_dev.conllu*
*dataset_test.conllu*

The tokenized sentences of these sets:
*dataset_tok_input_dev.txt*
*dataset_tok_input_train.txt*
*dataset_tok_input_tst.txt*
