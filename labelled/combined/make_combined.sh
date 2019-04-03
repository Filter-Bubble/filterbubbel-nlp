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
