# Decide on format/standard and gold standards

## NER

Schema: 

* WikiNER (Nothman:        PER, ORG, LOC,           MISC, NON, DAB)
* SoNaR (Desmet and Hoste: PER, ORG, LOC, PRO, EVE, MISC, subtypes? literal/metonymical)

NER is no priority at the moment.

## POS

UPOS uit CoNLL shared tasks

## SRL

From the Sonar documentation:

> All data in the 500K subset were annotated with semantic roles following the PropBank approach (Palmer, Gildea, and Kingsbury, 2005).
> Semantic roles are indicated at clause level and a distinction is made between a predicate and its arguments.
> The predicate is the semantic head of a sentence and in the case of SoNaR this is always a verb.
> The arguments are elements related by this predicate.
> Besides these two elements, modifiers, which add additional semantic information, are also labeled.
> The guidelines followed were developed during the D-Coi project (Trapman and Monachesi, 2006).
>
> Because of the close link between semantic and syntactic analysis we start all semantic annotation from the manually verified syntactic trees of the Lassy Klein corpus.
> For the semantic role annotation task the propbank labels are added as additional attributes to the Alpino-xml trees.

Counting the *pb* tags in the Sonar1 dataset, ie. all xml files in *SoNaRCorpus_NC_1.2/SONAR1/SRL/SONAR_1_SRL/MANUAL500*

| pb             |      count |
| -------------- | ---------- |
| Arg0           |    18323   |
| Arg1 (space)   |        1   |
| Arg1           |    31536   |
| Arg2           |     7079   |
| Arg3           |      506   |
| Arg4           |      601   |
| Arg5           |        2   |
| ArgM-ADV       |     5155   |
| ArgM-CAU       |     1590   |
| ArgM-DIR       |      556   |
| ArgM-DIS       |     5342   |
| ArgM-EXT       |      922   |
| ArgM-LOC       |     6777   |
| ArgM=MNR       |        1   |
| ArgM-MNR       |     4904   |
| ArgM-MOD       |     5931   |
| ArgM-NEG       |     2947   |
| ArgM-PNC       |     1803   |
| ArgM-PRD       |     1164   |
| ArgM-REC       |     1205   |
| ArgM-STR       |        5   |
| ArgM-TMP       |    10097   |
| come.01        |        2   |
| correspond.02  |        1   |
| decide.01      |        1   |
| die.01         |        1   |
| Dunno          |        1   |
| envisage.01    |        1   |
| get.03         |        2   |
| grasp.01       |        1   |
| keep.01        |        1   |
| make.01        |        2   |
| pin.01         |        1   |
| present.01     |        1   |
| rel            |    36978   |
| shame.01       |        1   |
| start.01       |        2   |
| SYNT           |      368   |

Some small corrections:
 * the *Arg1* with extra space
 * the *ArgM=MNR*
 * replace the 10s of frames with the generic 'rel'
 * remove the SYNT sentences, these have 'mismatch in syntactic structure'


## Dependencies

CoNLL-UD format

## COREF

Schema:

* SoNaR
* Corea

find out what is useful/needed

