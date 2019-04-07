# Frog

Build LaMachine:
```
sudo docker pull proycon/lamachine:latest
```

Run LaMachine with the current directory mapped to */data2*:
```
sudo docker run -v `pwd`:/data2 -p 8080:80 -t -i proycon/lamachine:latest
```

# Remapping of tags

## UPOS

*cgn_to_upos_orig.txt*
https://universaldependencies.org/tagset-conversion/nl-cgn-uposf.html

*cgn_to_upos_extra.txt*
a number (not all) of tags that showed up missing when parsing the eval and test treebanks for UD alpino and lassy. Not used.

*cgn_to_upos.txt*
tags used for the actual remapping. At the moment, the same as the original

NOTES:
Frog does not do tokenization the same way alpino (and UD treebanks) do.
Turning off tokenization, and use text tokenized by alpino does not improve (much).
Turning off the mwu option (multi word detection) should help, but crashes frog. Frog needs the mwu for parsing
Un-doing the multiword detection and using gold tokenizer fixes the UPOS scores

working solution:
do a minimal parse on the gold tokenized data to get tokens, upos, xpos
do a full parse to get dependencies
merge the two parses

## DEPREL

Tags used by [Universal Dependencies](https://universaldependencies.org/u/dep/index.html)::

* acl: clausal modifier of noun (adjectival clause)
* advcl: adverbial clause modifier
* advmod: adverbial modifier
* amod: adjectival modifier
* appos: appositional modifier
* aux: auxiliary
* case: case marking
* cc: coordinating conjunction
* ccomp: clausal complement
* clf: classifier
* compound: compound
* conj: conjunct
* cop: copula
* csubj: clausal subject
* dep: unspecified dependency
* det: determiner
* discourse: discourse element
* dislocated: dislocated elements
* expl: expletive
* fixed: fixed multiword expression
* flat: flat multiword expression
* goeswith: goes with
* iobj: indirect object
* list: list
* mark: marker
* nmod: nominal modifier
* nsubj: nominal subject
* nummod: numeric modifier
* obj: object
* obl: oblique nominal
* orphan: orphan
* parataxis: parataxis
* punct: punctuation
* reparandum: overridden disfluency
* vocative: vocative
* xcomp: open clausal complement
* root: root
# Tags used by Frog / Alpino

A table of the dependency labels used by frogs found in [the frog github repo](https://github.com/LanguageMachines/frog/blob/master/docs/source/credits.rst).

| LABEL     | map      |  OMSCHRIJVING                                                   |
| ----------| ---      |  ------------                                                   |
| app       |          |  appositie, bijstelling                                         |
| body      |          |  romp (bij complementizer))                                     |
| cmp       |          |  complementizer                                                 |
| cnj       | conj     |  lid van nevenschikking                                         |
| crd       | cc       |  nevenschikker (als hoofd van conjunctie)                       |
| det       | det      |  determinator                                                   |
| dlink     |          |  discourse-link                                                 |
| dp        |          |  discourse-part                                                 |
| hd        |          |  hoofd                                                          |
| hdf       |          |  afsluitend element van circumpositie                           |
| ld        |          |  locatief of directioneel complement                            |
| me        |          |  maat (duur, gewicht, . . . ) complement                        |
| mod       |          |  bijwoordelijke bepaling                                        |
| mwp       |          |  deel van een multi-word-unit                                   |
| nucl      |          |  kernzin                                                        |
| obcomp    |          |  vergelijkingscomplement                                        |
| obj1      | obj      |  direct object, lijdend voorwerp                                |
| obj2      | iobj     |  secundair object (meewerkend, belanghebbend, ondervindend)     |
| pc        |          |  voorzetselvoorwerp                                             |
| pobj1     |          |  voorlopig direct object                                        |
| predc     |          |  predicatief complement                                         |
| predm     |          |  bepaling van gesteldheid ‘tijdens de handeling’                |
| rhd       |          |  hoofd van een relatieve zin                                    |
| sat       |          |  satelliet; aan- of uitloop                                     |
| se        |          |  verplicht reflexief object                                     |
| su        | nsubj    |  subject, onderwerp                                             |
| sup       |          |  voorlopig subject                                              |
| svp       |          |  scheidbaar deel van werkwoord                                  |
| tag       |          |  aanhangsel, tussenvoegsel                                      |
| vc        |          |  verbaal complement                                             |
| whd       |          |  hoofd van een vraagzin                                         |
| ROOT      | root     |                                                                 |
| punct     | punct    |                                                                 |
