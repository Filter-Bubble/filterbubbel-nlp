#!/usr/bin/bash

cat \
  lassy_restricted.conllu \
  nl_alpino-ud-dev.conllu \
  nl_alpino-ud-train.conllu |
python3  ./check_sentences.py > make_combined.out 2> make_combined.err


# replace "&amp;" with a regular ampersand
for f in dataset_test.conllu dataset_train.conllu dataset_dev.conllu; do
  mv "$f" fix
  cat fix | sed 's/&amp;/\&/g' > "$f"
done


# To improve tokenization, we use the de-tokenization from feature from udpipe
# We supply udpipe with properly detokenized text, and it adds the relevant 'SpaceAfter' and 'SpaceBefore' tags.
# For this we used the first 5000 lines of our wikipedia corpus.

udpipe --detokenize detokenizid_wikinl.txt --outfile dataset_detok_train.conllu dataset_train.conllu
udpipe --detokenize detokenizid_wikinl.txt --outfile dataset_detok_test.conllu  dataset_test.conllu
udpipe --detokenize detokenizid_wikinl.txt --outfile dataset_detok_dev.conllu   dataset_dev.conllu

# finally, create detokenized input
cat  dataset_detok_test.conllu  | ./create_detokenized.py > dataset_detok_input_tst.txt
cat  dataset_detok_train.conllu | ./create_detokenized.py > dataset_detok_input_train.txt
cat  dataset_detok_dev.conllu   | ./create_detokenized.py > dataset_detok_input_dev.txt
