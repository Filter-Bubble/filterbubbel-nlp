# StanfordNLP

Installed library via pip:

```
pip install stanfordnlp
```

Install Dutch language support using built in command:

```python
>>> import stanfordnlp
>>> stanfordnlp.download(lang='nl')
```

# Retraining

See the [official manual](https://stanfordnlp.github.io/stanfordnlp/training.html) for instructions.

## evaluating the tagger

```
python -m stanfordnlp.models.tagger \
  --wordvec_dir .. \
  --eval_file ..\
  --gold_file ..\
  --output_file  .. \
  --lang nl_combined \
  --shorthand nl_combined \
  --batch_size 5000 \
  --mode predict
```
Lemma score:
nl_combined 98.91

