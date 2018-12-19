#!/usr/bin/env python

import re

"""
AI 核心代码，估值一个亿
"""
while True:
    print(re.sub(r'["吗", "?", "？"]', "!", input('>>>')))