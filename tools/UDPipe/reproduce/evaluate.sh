#!/usr/bin/bash
for dataset in alpino; do
  for datatype in tst; do
    python ../../conll18_ud_eval.py --verbose \
      ../../../labelled/eval/${dataset}_${datatype}.connl \
      ${dataset}_parse_${datatype}.connlu \
      > ${dataset}_eval_${datatype}.txt
  done
done
