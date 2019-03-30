#!/usr/bin/bash
for dataset in alpino lassysmall; do
  for datatype in tst dev; do
    python ../conll18_ud_eval.py --verbose \
      ../../labelled/eval/${dataset}_${datatype}.connl \
      ${dataset}_parse_${datatype}.connl \
      > ${dataset}_eval_${datatype}.txt
  done
done
