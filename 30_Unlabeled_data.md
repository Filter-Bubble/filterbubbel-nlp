# Unlabelled data

     lines      words      chars
    107M        1657M   10172847327 AEM/AEM_corpus
     16M        1051M    6846439451 rechtspraak/nl.txt
     28M         868M    5107948386 epub2/nl.txt
     20M         750M    4380707731 epub/nl.txt
    104M         611M    3308363867 opensubtitels2018/nl.txt
     15M         215M    1412983843 wikinl/nl.txt
      1M          50M     327409138 europarl/nl.txt
      4M          44M     281213990 gutenberg/nl.txt

approaching 5B words.

## [DBpedia](https://wiki.dbpedia.org/)

Downloaded from:
http://downloads.dbpedia.org/2016-10/core-i18n/nl/pages_articles_nl.xml.bz2

Arround 243M tokens

## [Europarl corpus v7](http://www.statmt.org/europarl/)

The Europarl parallel corpus is extracted from the proceedings of the European Parliament. It includes versions in 21 European languages: Romanic (French, Italian, Spanish, Portuguese, Romanian), Germanic (English, Dutch, German, Danish, Swedish), Slavik (Bulgarian, Czech, Polish, Slovak, Slovene), Finni-Ugric (Finnish, Hungarian, Estonian), Baltic (Latvian, Lithuanian), and Greek.

For Dutch, we have 2,333,816 sentences, 53,487,257 words.

## Book collections

A large collection of Dutch ebooks, not shareable for copyright reasons.
Collection 1 contains 750M words.
Collection 2 contains 868M words.
The collections have significant overlap.

## Project gutenberg

This contains some 800 dutch ebooks.
About 44M words.
Downloaded 2019-01-29, duplicates removed.
Headers and footers from gutenberg removed.

## [Open subtitles 2018](http://opus.nlpl.eu/OpenSubtitles2018.php)

This is a new collection of translated movie subtitles from http://www.opensubtitles.org/.

Dutch subtitles, 104.7M sentences, 611M words.


## [Court proceedings](https://www.rechtspraak.nl/Uitspraken-en-nieuws/Uitspraken/Paginas/Open-Data.aspx)

Proceedings and decissions by the Dutch courts, as XML.
They have been anonymized before publishing.

Some preprocessing was necessary:

* extract text from the XML
* remove short lines (ie. page headers, database identifiers, and other book keeping information)
* remove empty lines and other non-significant whitespace.
* remove entries from before the year 2000; as these typically not contain much text

Note that this way, a sentence in the corpus corresponds to a paragraph in the original proceedings.

Original size 4.2GB, zipped.
After processing 6.4GB unzipped, 16M sentences 1B words.


## Amsterdam Embedding Model (AEM) Corpus

This corpus contains unique sentences derived from a total of 7441914 Dutch news articles that appeared in print media and online sources. 
The news articles were derived from the INCA database for the time period: 2000-01-01 - 2017-12-31. 

Text has been preprocessed:

* a line corresponds to a single sentence, no further ordering is preserved
* unique lines: duplicate sentences are removed
* lowercased
* punctuation removed
* mapped to ASCII

Low amount of garbage sentences: "robert laffont import nilsson lamm pagina s fl", "esther gerritsen foto patricia borger pcm uitgevers b", found at least 2 in the first 500 lines, so on the order of 1 percent.

1.7B words in 110M sentences.


## [NLCOW14 Corpora from the Web](https://corporafromtheweb.org/nlcow14/)

A webcrawl from nl and be TLDs.
Contains 4.7B tokens in 250M sentences, available after registration via [https://www.webcorpora.org/](https://www.webcorpora.org/)

Text has been extensively processed, for details see the link above.
Sentences are also tagged using TreeTagger.
