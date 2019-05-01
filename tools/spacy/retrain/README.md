
Following the [instructions on the Spacy website](https://spacy.io/usage/training)

Create train and dev datasets in the JSON format:
```bash
 $ python -m spacy convert dataset_train.conllu dataset-json --file-type json
 $ python -m spacy convert dataset_dev.conllu dataset-json --file-type json
```
The dataset contains a few sentencens with cyclic dependencies, which lead infinite loops in SpaCy.
I manually removed: WR-P-E-I-0000050381.p.1.s.682.2, dpc-med-000686-nl-sen.p.8.s.1, and WR-P-E-I-0000049645.p.1.s.156 from the training set.
And one sentence (WR-P-P-C-0000000001.p.134.s.1) from the dev set.

Note: the test set contains 1 sentence with cyclic dependencies (WR-P-P-G-0000000020.p.19.s.2), which is left as-is.

Initialize an empty model containing the Fasttext wordvectors
```
python -m spacy init-model nl ../model-vectors --vectors ../spacy_vectors.txt 
```

Train the model
```
python -m spacy train -p tagger,parser -v ../model-vectors -n 50 -G --verbose nl ../retrain-dataset ../dataset-json/dataset_train.json ../dataset-json/dataset_dev.json
```
