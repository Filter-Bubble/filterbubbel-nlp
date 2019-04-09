#!/usr/bin/bash

cat \
  lassy_restricted.conllu \
  nl_alpino-ud-dev.conllu \
  nl_alpino-ud-train.conllu |
python3  ./check_sentences.py > make_combined.out 2> make_combined.err


# replace "&amp;" with a regular ampersand
# truncate sentence id
for f in dataset_test.conllu dataset_train.conllu dataset_dev.conllu; do
  mv "$f" fix
  cat fix | sed 's/&amp;/\&/g' | sed 's/^# sent_id = .*\/\([^|]\)/# sent_id = \1/' > "$f" 
done

# create tokenized input
cat  dataset_test.conllu  | ./create_tokenized.py > dataset_tok_input_tst.txt
cat  dataset_train.conllu | ./create_tokenized.py > dataset_tok_input_train.txt
cat  dataset_dev.conllu   | ./create_tokenized.py > dataset_tok_input_dev.txt
