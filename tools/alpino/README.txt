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
cat alpino_dev_tokenized.txt | Alpino -flag treebank alpino_dev_parsed debug=1 end_hook=xml user_max=900000 -parse
```

* converted to CoNNL using the lassy2ud scripts (definition universal_dependencies_2.3.xq)


cat dataset_tok_input_tst.txt | Alpino -flag treebank alpino_dev_parsed debug=1 end_hook=xml user_max=900000 -parse


Sentences where alpino failed to create a parse (xml file)

WS-U-E-A-0000000009.p.14.s.1
WS-U-E-A-0000000212.p.19.s.1
WS-U-E-A-0000000217.p.14.s.3

[ CA 2 ] ] Ietwat minder dreiging in de Verenigde Staten .
] ] CAM 44444444 ] ] Morgen deel 2 van de serie reportages die de Journaalploeg in Tsjaad heeft gemaakt .
Maar voorlopig staat ie op een parkeerplaats langs de A8 . [ voxpop ] [ ik schaam de dood , mensen langs snelweg . iedereen kijkt ] .


after WS-U-E-A-0000000009.p.11.s.17:
# sent_id = WS-U-E-A-0000000009.p.14.s.1
# text = [ CA 2 ] ] Ietwat minder dreiging in de Verenigde Staten .
1	[	[	_	_	_	_	_	_	_
2	CA	CA	_	_	_	_	_	_	_
3	2	2	_	_	_	_	_	_	_
4	]	]	_	_	_	_	_	_	_
5	]	]	_	_	_	_	_	_	_
6	Ietwat	ietwat	_	_	_	_	_	_	_
7	minder	weinig	_	_	_	_	_	_	_
8	dreiging	dreiging	_	_	_	_	_	_	_
9	in	in	_	_	_	_	_	_	_
10	de	de	_	_	_	_	_	_	_
11	Verenigde	verenigen	_	_	_	_	_	_	_
12	Staten	staat	_	_	_	_	_	_	_
13	.	.	_	_	_	_	_	_	_


after WS-U-E-A-0000000212.p.15.s.4:
# sent_id = WS-U-E-A-0000000212.p.19.s.1
# text = ] ] CAM 44444444 ] ] Morgen deel 2 van de serie reportages die de Journaalploeg in Tsjaad heeft gemaakt .
1	]	]	_	_	_	_	_	_	_
2	]	]	_	_	_	_	_	_	_
3	CAM	CAM	_	_	_	_	_	_	_
4	44444444	44444444	_	_	_	_	_	_	_
5	]	]	_	_	_	_	_	_	_
6	]	]	_	_	_	_	_	_	_
7	Morgen	morgen	_	_	_	_	_	_	_
8	deel	deel	_	_	_	_	_	_	_
9	2	2	_	_	_	_	_	_	_
10	van	van	_	_	_	_	_	_	_
11	de	de	_	_	_	_	_	_	_
12	serie	serie	_	_	_	_	_	_	_
13	reportages	reportage	_	_	_	_	_	_	_
14	die	die	_	_	_	_	_	_	_
15	de	de	_	_	_	_	_	_	_
16	Journaalploeg	journaalploeg	_	_	_	_	_	_	_
17	in	in	_	_	_	_	_	_	_
18	Tsjaad	Tsjaad	_	_	_	_	_	_	_
19	heeft	hebben	_	_	_	_	_	_	_
20	gemaakt	maken	_	_	_	_	_	_	_
21	.	.	_	_	_	_	_	_	_


after WS-U-E-A-0000000217.p.13.s.1:
# sent_id = WS-U-E-A-0000000217.p.14.s.3
# text = Maar voorlopig staat ie op een parkeerplaats langs de A8 . [ voxpop ] [ ik schaam de dood , mensen langs snelweg . iedereen kijkt ] .
1	Maar	maar	_	_	_	_	_	_	_
2	voorlopig	voorlopig	_	_	_	_	_	_	_
3	staat	staan	_	_	_	_	_	_	_
4	ie	hij	_	_	_	_	_	_	_
5	op	op	_	_	_	_	_	_	_
6	een	een	_	_	_	_	_	_	_
7	parkeerplaats	parkeerplaats	_	_	_	_	_	_	_
8	langs	langs	_	_	_	_	_	_	_
9	de	de	_	_	_	_	_	_	_
10	A8	A8	_	_	_	_	_	_	_
11	.	.	_	_	_	_	_	_	_
12	[	[	_	_	_	_	_	_	_
13	voxpop	voxpop	_	_	_	_	_	_	_
14	]	]	_	_	_	_	_	_	_
15	[	[	_	_	_	_	_	_	_
16	ik	ik	_	_	_	_	_	_	_
17	schaam	schamen	_	_	_	_	_	_	_
18	de	de	_	_	_	_	_	_	_
19	dood	dood	_	_	_	_	_	_	_
20	,	,	_	_	_	_	_	_	_
21	mensen	mens	_	_	_	_	_	_	_
22	langs	langs	_	_	_	_	_	_	_
23	snelweg	snelweg	_	_	_	_	_	_	_
24	.	.	_	_	_	_	_	_	_
25	iedereen	iedereen	_	_	_	_	_	_	_
26	kijkt	kijken	_	_	_	_	_	_	_
27	]	]	_	_	_	_	_	_	_
28	.	.	_	_	_	_	_	_	_
