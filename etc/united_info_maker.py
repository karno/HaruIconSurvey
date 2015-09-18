#!/usr/bin/env python
# -*- coding: utf-8 -*-
# united_info.jsonをある程度まで自動生成
# (直通などは非対応なので手での修正が必要)
# 引数:なし


import sys
import os
from haru_stations import stations
from haru_lines import lines, company_author, airline, ship
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

tabsize = 4;
tab1 = '\t'.expandtabs(tabsize);
tab2 = '\t\t'.expandtabs(tabsize);
tab3 = '\t\t\t'.expandtabs(tabsize);
tab4 = '\t\t\t\t'.expandtabs(tabsize);
tab5 = '\t\t\t\t\t'.expandtabs(tabsize);

def wrap(s):
	return "\"" + s + "\"";

def writeln(s):
    write(s+'\n');
    return;

fr = open("haru_station_locations.py", "r", encoding="utf-8");
fw = open("united_info_draft.json", "w", encoding="utf-8");

######################################################

print("# phase 1: lines");
flag_initiated = False;
fw.write('{\n');
fw.write('    \"lines\": {\n');
prev_exist_dist_info, exist_dist_info = False, False;

for line in fr:
    if line.expandtabs(tabsize).startswith(tab2+'#') :
        fw.write(tab2+line);
    # seek station data line
    line = line.strip();
    if not line.startswith('\"') :
        continue;
    if line.endswith('{') :
        # (railway)line name line (路線名の行)
        # ex)
        #     "ZZ" : { 
        line_code = line.strip('\": {');
        line_company, line_name, line_color = lines[line_code];
        if not flag_initiated :
            flag_initiated = True;
        else :
            # write previous last line
            if prev_exist_dist_info :
                fw.write(tab4 + '\"' + prev_sta_code + '\": { \"connect\": { \"' + \
                prev_line_code + prev2_sta_code + '\": ' + prev_distance + ' } }\n');
            else :
                # when no distance info at the line(路線)
                fw.write(tab4 + "# fixme\n");
            fw.write(tab3 + '}\n');
            fw.write(tab2 + '},\n');
        fw.write(tab2 + '\"' + line_code + '\": {\n');
        fw.write(tab3 + '\"name\": \"' + line_name + '\",\n');
        fw.write(tab3 + '\"company\": \"' + line_company + '\",\n');
        fw.write(tab3 + '\"author\": \"' + company_author.get(line_company,'(unknown)') + '\",\n');
        fw.write(tab3 + '\"color\": \"' + line_color + '\",\n');
        fw.write(tab3 + '\"stations\": {\n');
        prev_exist_dist_info, exist_dist_info = False, False;
        continue;
    prev_line_code = line_code;
    sta_code, dummy, line = line.partition(':');
    line, dummy, comment = line.rpartition('#');
    if line == '':
        line = comment;
        comment = '';
    coordinate, dummy, sta_name = line.strip('(), ').partition(', \"');
    sta_code = sta_code.strip('\"');
    comment = comment.strip();
    sta_name = sta_name.strip('\"');
    station_options = '';
    if comment.startswith('<夜間通過>') :
        station_options += (tab4 + '\"pass_night\": true\n');
    exist_dist_info = (comment.endswith('blocks') and comment.strip('blocks ').isdecimal());
    if exist_dist_info :
        distance = comment.strip('blocks ');
        # write *previous* station
        if prev_exist_dist_info :
            # when both prev and next distance info exist (distance info continue)
            fw.write(tab4 + '\"' + prev_sta_code + '\": { \"connect\": { \"' + \
            line_code + prev2_sta_code + '\": ' + prev_distance + ', \"' + \
            line_code + sta_code + '\": ' + distance + ' } },\n');
        else :
            # when distance info begin
            fw.write(tab4 + '\"' + prev_sta_code + '\": { \"connect\": { \"' + \
            line_code + sta_code + '\": ' + distance + ' } },\n');
        prev2_sta_code = prev_sta_code;
        prev_sta_code, prev_distance = sta_code, distance;
        prev_exist_dist_info = exist_dist_info;
    else : 
        if prev_exist_dist_info : 
            fw.write(tab4 + '\"' + prev_sta_code + '\": { \"connect\": { \"' + \
            line_code + prev2_sta_code + '\": ' + prev_distance + ' } }\n');
        prev_sta_code = sta_code;
        prev_exist_dist_info = exist_dist_info;
        continue;

# finalize(write last last line)
fw.write(tab3 + '}\n');
fw.write(tab2 + '}\n');
fw.write(tab1 + '},\n');

print("# phase 1 complete.");

######################################################

print("# phase 2: transfer");

fw.write('    \"transfer\": {\n');
