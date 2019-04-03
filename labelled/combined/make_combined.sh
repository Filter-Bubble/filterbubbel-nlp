#!/usr/bin/bash

cat \
  lassy_restricted.conllu \
  nl_alpino-ud-dev.conllu \
  nl_alpino-ud-train.conllu |
python3  ./check_sentences.py > make_combined.out 2> make_combined.err
