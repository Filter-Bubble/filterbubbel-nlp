#!/usr/bin/env python
from allennlp.predictors.predictor import Predictor

#  'arc_loss': -0.0,
#  'tag_loss': -0.0,
#  'loss': -0.0,
#  'words': ['Het', 'zorgt', 'voor', 'ontwikkeling', '.'],
#  'pos': [
#      'VNW|pers|pron|stan|red|3|ev|onz',
#      'WW|pv|tgw|met-t',
#      'VZ|init',
#      'N|soort|ev|basis|zijd|stan',
#      'LET'
#      ],
#  'predicted_dependencies': [
#      'nsubj',
#      'root',
#      'case',
#      'obl',
#      'punct'
#      ],
#  'predicted_heads': [2, 0, 4, 2, 2],

def dump_line(self, outputs):
    # Conllu format:
    # index form lemma upos xpos feats head deprel deps misc
    result = ""
    for index in range(len(outputs['words'])):
        line = []
        line.append('{}'.format(index + 1))
        line.append('{}'.format(outputs['words'][index]))
        line.append('_')
        line.append('_')
        line.append('{}'.format(outputs['pos'][index]))
        line.append('_')
        line.append('{}'.format(outputs['predicted_heads'][index]))
        line.append('{}'.format(outputs['predicted_dependencies'][index]))
        line.append('_')
        line.append('_')
        result += "\t".join(line) + "\n"

    return result + "\n"

Predictor.dump_line = dump_line
