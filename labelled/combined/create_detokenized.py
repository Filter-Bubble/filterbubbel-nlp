#!/usr/bin/env python
"""
Create detokenized text from a conllu file

Concattenate all token FORMS with optional ' ', depending on SpaceAfter=no in the MISC column.
Prefix each sentence with their sentence ID:
    sent_id|Detokenized sentence.

Read from stdin

Write to stdout
"""

import re
import sys
import random

SPACE_AFTER = re.compile('.*SpaceAfter=No.*', re.IGNORECASE)
HAS_SUBTOKEN = re.compile('\d*\.\d')

sentence = []
line_counter = 0

for line in sys.stdin:
    line = line.rstrip()
    line_counter += 1

    if len(line) == 0:
        # reconstruct the full sentence
        full_sentence = comment_sentid + "|"
        for token in sentence:
            # skip 'invisible' tokens with an index like '10.1'
            if not HAS_SUBTOKEN.match(token[0]):
                full_sentence += token[1]
                if SPACE_AFTER.match(token[9]):
                    # MISC contains SpaceAfter=no
                    pass
                else:
                    full_sentence += " "

        print (full_sentence)
        
        # reset sentence and metadata
        sentence = []
        comment_sentid = None
        comment_text = None
        continue

    if line[0:9] == '# text = ':
        # read the sentence raw text
        comment_text = line
        continue
    if line[0:12] == '# sent_id = ':
        # read the sentence id
        comment_sentid = line[12:]
        continue
    elif line[0] == '#':
        # comments are ignored
        continue

    fields = line.split('\t')
    if len(fields) == 10:
        # the line contains a regular token
        sentence.append(fields)
        continue

    raise ParsingError('Error parsing line {}: "{}"'.format(line_counter, line))
