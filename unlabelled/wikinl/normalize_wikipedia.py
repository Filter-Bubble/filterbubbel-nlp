#!/usr/bin/env python
import argparse
import json
import re
import unicodedata

# break up in sentences on a dot (ie. ". " => ".\n")
re_break_on_dot = re.compile("\. ")

# find double newlines (ie. "\n\n" => "\n")
re_double_newlines = re.compile("\n\s*\n")

# find multiple whitespace (ie. "  " => " ")
re_multiple_whitespace = re.compile("[ \t]+")

# find non alphanumeric characters
re_punctuation = re.compile("([.,';:(){}\"])+")

# find numbers, percentages, years, etc.
re_numbers = re.compile("[+-]?\d+(,\d+)*(\.\d+)?%?")

parser = argparse.ArgumentParser()
parser.add_argument("input")
args = parser.parse_args()

with open(args.input, 'r') as f:
    raw_lines = f.readlines()

for line in raw_lines:
    data = json.loads(line)
    bts = unicodedata.normalize('NFKD', data['text'])
    text = bts.encode('ASCII', 'ignore').decode()
    text = text.lower()
    #text = data['text'].lower()

    text = re_numbers.sub("1", text)
    text = re_break_on_dot.sub(". \n", text)
    text = re_double_newlines.sub("\n", text)
    text = re_punctuation.sub(r" \1 ", text)
    text = re_multiple_whitespace.sub(" ", text)
    print(text)
