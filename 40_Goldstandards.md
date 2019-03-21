# Decide on format/standard and gold standards

## NER

Schema: 

* WikiNER (Nothman:        PER, ORG, LOC,           MISC, NON, DAB)
* SoNaR (Desmet and Hoste: PER, ORG, LOC, PRO, EVE, MISC, subtypes? literal/metonymical)


## POS

Schema:

* UD (Alpino, Lassy)
* SoNaR


## SRL

Schema:

* SoNaR
* PropBank, FrameNet (english)


## Dependencies

* merge UD_Dutch_LassySmall (84K), UD_Dutch_Alpino (187K), and LassySmall (700K unique) -> together 970K.  Done: UD_Dutch_Alpino + newly created lassy_restricted (in CoNLLU format)


## COREF

Schema:

* SoNaR
