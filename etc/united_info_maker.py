#!/usr/bin/env python
# -*- coding: utf-8 -*-
# united_info.jsonをある程度まで自動生成
# (直通などは非対応なので手での修正が必要)
# 引数:なし


import sys, os
from ../haru_stations import stations
from ../haru_lines import lines, company_author, airline, ship
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from haru_lines import lines

tab4 = '                ';
tab5 = '                    ';

def wrap(s):
	return "\"" + s + "\""

fr = open("../haru_station_locations.py", "r", encoding="utf-8");
fw = open("united_info_draft.json", "w", encoding="utf-8");

######################################################

print("phase 1: lines");
flag_initiated = false;
fw.write('{');
fw.write('    \"line\": {');

for line in fr:
    # seek station data line
    line = line.strip();
    if not line.startswith('\"') :
        continue;
    if line.endswith('{') :
        # (railway)line name line (路線名の行)
        # ex)
        #     "ZZ" : { 
        line_code = line.strip('\"');
        line_company, line_name, line_color = lines.line_code;
        if flag_initiated == false:
            flag_initiated = true;
        else:
            # write previous last line
            fw.write('            }');
            fw.write('        },');
        fw.write('        \"'+line+'\"');
        fw.write('            \"name\": \"' + line_name + '\",');
        fw.write('            \"company\": \"' + line_company + '\",');
        fw.write('            \"author\": \"' + company_author.line_company + '\",');
        fw.write('            \"color\": \"' + line_color + '\",');
        fw.write('            \"stations\": {');
        continue;
    sta_code, dummy, line = line.partition(':');
    line, dummy, comment = line.rpartition('#');
    coordinate, dummy, sta_name = line.strip('(),').partition(', \"');
    sta_code = sta_code.strip('\"');
    comment = comment.strip();
    
    # fw.write(tab4+'\"'+sta_code+'\": { \"connect\": { \"'++'\"')

    

# finalize(write last last line)
fw.write('            }');
fw.write('        },');
fw.write('    },');

print("phase 1 complete.");

######################################################

print("phase 2: transfer");

fw.write('{');
fw.write('    \"transfer\": {');
