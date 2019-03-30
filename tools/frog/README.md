# Frog

Build LaMachine:
```
sudo docker pull proycon/lamachine:latest
```

Run LaMachine with the current directory mapped to */data2*:
```
sudo docker run -v `pwd`:/data2 -p 8080:80 -t -i proycon/lamachine:latest
```

Remapping of tags:
*cgn_to_upos_orig.txt*
https://universaldependencies.org/tagset-conversion/nl-cgn-uposf.html

*cgn_to_upos_extra.txt*
a number (not all) of tags that showed up missing when parsing the eval and test treebanks for UD alpino and lassy. Not used.

*cgn_to_upos.txt*
tags used for the actual remapping. At the moment, the same as the original

TODO:
frog does not do tokenization the same way alpino (and UD treebanks) do.
Turning off tokenization, and use text tokenized by alpino does not improve (much).
Turning off the mwu option (multi word detection) should help, but crashes frog.
