#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 旧駅名コードを自動置換

import sys, os
from scode_mapping import map_table 
# import ../haru_lines.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from haru_lines import lines


def wrap(s):
	return "\"" + s + "\""


argv = sys.argv
if len(argv) != 2:
    print("invalid argument")
    quit()

file = argv[1]
fr = open(file, "r", encoding="utf-8")
fw = open(file + ".repl", "w", encoding="utf-8")

print(file + " to " + file + ".repl ...")

for line in fr:
	# replace simple station id
    for key, value in map_table.items():
        line = line.replace(wrap(key), wrap(value));
    # replace fully-qualified station id
    for key, value in map_table.items():
        for lcode in lines:
            line = line.replace(wrap(lcode + key), wrap(lcode + value));
    fw.write(line)

print("complete.")


