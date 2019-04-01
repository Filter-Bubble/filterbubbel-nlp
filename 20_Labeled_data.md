# Labelled data - NL

The datasets are too large to include in this repo (or cannot be shared for other reasons).
Obtaining a copy is up to you.


Dataset             | Year | NER | POS | dep | srl  | coref |
---                 | ---  | --- | --- | --- | ---  | ----- |
CONLL2002           | 2002 |   X | X   |     |      |       |
COREA               | 2008 |     |     |     |      |  X    |
WikiNER             | 2012 |   X |     |     |      |       |
CGN                 | 2013 |     | X   |     |      |       |
Eindhoven           | 2014 |     | X   |     |      |       |
SoNaR-1             | 2015 |   X | X   | X   |  X   |  X    |
LassySmall          | 2016 |     | X   | X   |      |       |
UD Dutch LassySmall | 2016 |     | X   | X   |      |       |
UD Dutch Alpino     | 2017 |     | X   | X   |      |       |


## [CoNLL2002](https://www.clips.uantwerpen.be/conll2002/ner/)

Named Entity Recognition (NER) is a subtask of Information Extraction. Different NER systems were evaluated as a part of the Sixth Message Understanding Conference in 1995 (MUC6). The target language was English. The participating systems performed well. However, many of them used language-specific resources for performing the task and it is unknown how they would have performed on another language than English [PD97].

After 1995 NER systems have been developed for some European languages and a few Asian languages. There have been at least two studies that have applied one NER system to different languages. Palmer and Day [PD97] have used statistical methods for finding named entities in newswire articles in Chinese, English, French, Japanese, Portuguese and Spanish. They found that the difficulty of the NER task was different for the six languages but that a large part of the task could be performed with simple methods. Cucerzan and Yarowsky [CY99] used both morphological and contextual clues for identifying named entities in English, Greek, Hindi, Rumanian and Turkish. With minimal supervision, they obtained overall F measures between 40 and 70, depending on the languages used.

The Dutch data consist of four editions of the Belgian newspaper "De Morgen" of 2000 (June 2, July 1, August 1 and September 1). The data was annotated as a part of the Atranos project at the University of Antwerp.

```bash
wget https://www.clips.uantwerpen.be/conll2002/ner/data/ned.train
wget https://www.clips.uantwerpen.be/conll2002/ner/data/ned.testa
wget https://www.clips.uantwerpen.be/conll2002/ner/data/ned.testb
```

## [COREA Coreferentiecorpus](https://www.aflat.org/~iris/corea.html)

Coreference resolution is a key ingredient for the automatic interpretation of text. It has been studied mainly from a linguistic perspective, with an emphasis on establishing potential antededents for pronouns. Practical applications, such as Information Extraction (IE), summarization and Question Answering (QA), require accurate identification of coreference relations between noun phrases in general. Computational systems for assigning such relations automatically, require the availability of a sufficient amount of annotated data for training and testing. For Dutch, annotated data is scarce and coreference resolution systems are lacking.

In this COREA project, a two-year project which started in July 2005, we aim to develop a robust system for assigning such relations automatically, and we will investigate the effect of making coreference relations explicit on the accuracy of systems for for IE and QA. We will annotate a limited amount of application-specific corpus material, which is required for the evaluation of the coreference resolution system in the context of IE and QA.

Downloaded ```COREA_Corpus_1.0.1p1.zip``` at 2019-03-19.

## [Corpus Gesproken Nederlands](https://ivdnt.org/images/stories/producten/documentatie/cgn_website/doc_English/topics/index.htm)

The Spoken Dutch Corpus project was aimed at the construction of a database of contemporary standard Dutch as spoken by adults in The Netherlands and Flanders. The intended size of the corpus was ten million words (about 1,000 hours of speech), two thirds of which would originate from the Netherlands and one third from Flanders. In this release, the results are presented that have emerged from the project. The total number of words available here is nearly 9 million. Some 3.3 million words were collected in Flanders, well over 5.6 million in The Netherlands.

The corpus comprises a large number of samples of (recorded) spoken text. The entire corpus has been transcribed orthographically, while the transcripts have been linked to the speech files. The orthographic transcription was used as the starting point for the lemmatization and part-of-speech tagging of the corpus. For a selection of one million words, a (verified) broad phonetic transcription has been produced, while for this part of the corpus also the alignment of the transcripts and the speech files has been verified at the word level. In addition, a selection of one million words has been annotated syntactically. Finally, for a more modest part of the corpus, approximately 250,000 words, a prosodic annotation is available.

The "Instituut voor de Nederlandse Taal" offers a [download link on their website](https://ivdnt.org/downloads/taalmaterialen/tstc-cgn-annotaties)

Downloaded version 2.0.3 at 2019-03-19.

The POS tags need to be mapped to UPOS for evaluation on the universal dependencies.
Suggested mapping is [here](https://universaldependencies.org/tagset-conversion/nl-cgn-uposf.html)


## [Eindhoven corpus](https://ivdnt.org/downloads/taalmaterialen/tstc-eindhoven-corpus)

Het Eindhoven-corpus (VU-versie) is een verzameling Nederlandstalige geschreven en getranscribeerde gesproken teksten uit de periode van 1960 tot 1976. Het corpus bevat ca. 768.000 tokens.

About 60k sentences, with labelled words.

VU-version from 1975
Downloaded v 2.0.1 at 2019-03-19



## [Lassy](http://www.let.rug.nl/~vannoord/Lassy/)

LASSY (Large Scale Syntactic Annotation of written Dutch) was a STEVIN project. STEVIN was the Flemish-Dutch Language and Speech Processing Technology Programme launched by de Nederlandse Taalunie.

A large corpus of written Dutch texts (1,000,000 words) has been syntactically annotated (manually corrected), based on CGN and D-COI. In addition, a very large corpus (more than 700,000,000 words) has been syntactically annotated automatically. The project extends the available syntactically annotated corpora for Dutch both in size as well as with respect to the various text genres and topical domains. In addition, various browse and search tools for syntactically annotated corpora have been developed and made available. Their potential for applications in corpus linguistics and information extraction is illustrated and evaluated in a series of case studies.

Downloaded Lassy Small v4.0 at 2019-03-19

890K words

Around 20% of this corpus has been included in the Universal Dependencies
700K unique words.

## [SoNaR](http://lands.let.ru.nl/projects/SoNaR/)

Het SoNaR-corpus is een tekstcorpus dat bestaat uit twee delen, nl. SoNaR-500 en SoNaR-1.

SONAR-500 bevat meer dan 500 miljoen woorden tekst afkomstig uit uiteenlopende domeinen en genres. Alle teksten werden getokeniseerd, ge-POS-tagd en gelemmatiseerd. Ook de named entities werden gelabeld. Alle annotaties van SoNaR-500 werden automatisch geproduceerd.

SoNaR-1 is grotendeels een subset van SoNaR-500 en bevat 1 miljoen woorden. SoNaR-1 werd voorzien van verschillende soorten semantische annotaties, nl. named entity labelling, coreferentieannotatie en de annotatie van spatiële en temporele relaties. Alle annotaties van SoNaR-1 werden manueel geverifieerd.

De nieuwemediateksten (tweets, chats en sms'en), die ook verzameld werden in het kader van het STEVIN-project SoNaR maken geen deel uit van het SoNaR-corpus 1.0. en zijn apart als het SoNar Nieuwe Media Corpus beschikbaar.

Downloaded ```20150602_SoNaRCorpus_NC_1.2.1.tgz``` at 2019-03-19.


## [Universal Dependencies](https://universaldependencies.org/)

Universal Dependencies (UD) is a framework for cross-linguistically consistent grammatical annotation and an open community effort with over 200 contributors producing more than 100 treebanks in over 70 languages.

Treebank including Dutch available on their website, containing parts of:

* ```UD_Dutch-Alpino```:  Alpino, and WR-P-P-H  and WR-P-P-L sections of LassySmall. 187K words
* ```UD_Dutch-LassySmall```: wiki section of LassySmall. 84K words.

Conversion scripts from Alpino and Lassy to the UD format [available here](https://github.com/gossebouma/lassy2ud)


## [WikiNER](https://github.com/dice-group/FOX/tree/master/input/Wikiner)

From their paper:

We automatically create enormous, free and multilingual silver-standard training annotations for named entity recognition (ner) by exploiting the text and structure of Wikipedia.
Most ner systems rely on statistical models of annotated data to identify and classify names of people, locations and organisations in text. This dependence on expensive annotation is the knowledge bottleneck our work overcomes.



# Labelled data - EN

For inspiration.

## [GLUE](https://gluebenchmark.com/)

The General Language Understanding Evaluation (GLUE) benchmark is a collection of resources for training, evaluating, and analyzing natural language understanding systems. GLUE consists of:

* A benchmark of nine sentence- or sentence-pair language understanding tasks built on established existing datasets and selected to cover a diverse range of dataset sizes, text genres, and degrees of difficulty,
* A diagnostic dataset designed to evaluate and analyze model performance with respect to a wide range of linguistic phenomena found in natural language, and
* A public leaderboard for tracking performance on the benchmark and a dashboard for visualizing the performance of models on the diagnostic set.

The format of the GLUE benchmark is model-agnostic, so any system capable of processing sentence and sentence pairs and producing corresponding predictions is eligible to participate. The benchmark tasks are selected so as to favor models that share information across tasks using parameter sharing or other transfer learning techniques. The ultimate goal of GLUE is to drive research in the development of general and robust natural language understanding systems.



## Timeline

Eindhoven corpus
  * dagbladen component CDBL (10% of total) is merged into the Alpino Treebank
  * there is more POS annotation, but without DEP

CGN
  * part of it is merged into Lassy, the Lassy Large (automatically annotated parts)

Alpino
  * Text comes from Eindhoven corpus, some parts of LassySmall, and other collections

Lassy
  * Text comes from DPC (Dutch Parallel Corpus), D-Coi, Wikipedia
  * Lassy Small is merged into Sonar and parts of it to Alpino

COREA
  * Text comes from DCOI, CGN, and Winkler Prins Medische Encyclopedie

SONAR
  * Text comes from Lassy Small

Use:
 * UD lassysmall, UD alpino, and a subset of lassysmall for POS, DEP
 * Overlap between sonar / corea. TODO: how much? is it a problem?

# Datasets not suitable to our tasks

## DAESO Corpus: Parallelle Nederlandstalige monolinguale treebank

Het DAESO-corpus is een parallelle monolinguale treebank van Nederlandse teksten en het corpus bevat meer dan 2,1 miljoen woorden parallelle en vergelijkbare tekst. Ongeveer 678.000 woorden werden handmatig opgelijnd en ongeveer 1,5 miljoen woorden automatisch. Er werd een semantische relatie aan de opgelijnde woorden/zinsdelen toegevoegd.

Link to dataset description [on ivdnt](https://ivdnt.org/downloads/taalmaterialen/tstc-daeso-corpus-parallelle-nederlandstalige-monolinguale-treebank)

POS tagging and semantic relations were done with Alpino.
