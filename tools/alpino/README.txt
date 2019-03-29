# Installation options

Please see the [Alpino User Guide](https://www.let.rug.nl/vannoord/alp/Alpino/AlpinoUserGuide.html) for instructions. 

The link to pre-built binaries does not work. Use this page to get [pre built binaries](http://www.let.rug.nl/~vannoord/alp/Alpino/versions/binary/) instead.

Alternatively, there is a Docker version [available here](https://github.com/rug-compling/alpino-docker)



* Manually edited the Alpino test and dev sets
* Tokenized using partok from the Alpino docker image (tokenize.sh)
* Parsed using Alpino
```
cat alpino_tst_tokenized.txt | Alpino -flag treebank alpino_tst_parsed debug=1 end_hook=xml user_max=900000 -parse
cat alpino_dev_tokenized.txt | Alpino -flag treebank alpino_dev_parsed debug=1 end_hook=xml user_max=900000 -parse
```

* converted to CoNNL using the lassy2ud scripts (definition universal_dependencies_2.3.xq)
