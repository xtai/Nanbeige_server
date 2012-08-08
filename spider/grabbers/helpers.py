# -*- coding: utf-8 -*-

import yaml

chinese_week_numbers = {
    u'一': 1,
    u'二': 2,
    u'三': 3,
    u'四': 4,
    u'五': 5,
    u'六': 6,
    u'七': 7,
    u'日': 7,
    u'天': 7,
}

def pretty_print(obj):
    print yaml.dump(obj, allow_unicode=True)
