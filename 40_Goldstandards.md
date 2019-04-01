# Decide on format/standard and gold standards

## NER

Schema: 

* WikiNER (Nothman:        PER, ORG, LOC,           MISC, NON, DAB)
* SoNaR (Desmet and Hoste: PER, ORG, LOC, PRO, EVE, MISC, subtypes? literal/metonymical)

no priority

## POS

Schema:

* UD (Alpino, Lassy)
* SoNaR

UPOS uit CoNLL shared tasks

## SRL

Schema:

* SoNaR
* PropBank, FrameNet (english)

Use what sonar does

## Dependencies

* merge UD_Dutch_LassySmall (84K), UD_Dutch_Alpino (187K), and LassySmall (700K unique) -> together 970K.  Done: UD_Dutch_Alpino + newly created lassy_restricted (in CoNLLU format)

CoNLL-UD format

## COREF

Schema:

* SoNaR

Corea
