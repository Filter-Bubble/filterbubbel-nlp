See some hints on retraining here: https://github.com/allenai/allennlp/issues/2445

wget https://s3-us-west-2.amazonaws.com/allennlp/models/biaffine-dependency-parser-ptb-2018.08.23.tar.gz

```
allennlp train -s model_path config.json
```


Predictions:
```
allennlp predict \
  --silent \
  --include-package conllu-output \
  --use-dataset-reader \
  --output-file alpino_parse_tst.conllu \
  retrain/model.tar.gz \
  ~/Code/ernie/labelled/ud/ud-treebanks-v2.3/UD_Dutch-Alpino/nl_alpino-ud-test.conllu
```

First retrain attempt used gold xpos, and did not predict upos/xpos.
