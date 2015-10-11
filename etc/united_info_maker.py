#!/usr/bin/env python
# -*- coding: utf-8 -*-
# united_info.jsonをある程度まで自動生成
# (直通などは非対応なので手での修正が必要)
# 引数:なし

import sys, os, pprint, json
from haru_station_locations import station_locations
from haru_stations import station_names, station_special_names
from haru_lines import lines, company_author, airline, ship
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

tabsize = 4;
tab1 = (' '*1*tabsize);
tab2 = (' '*2*tabsize);
tab3 = (' '*3*tabsize);
tab4 = (' '*4*tabsize);
tab5 = (' '*5*tabsize);

pp1 = pprint.PrettyPrinter(indent=tabsize*3, width=999, depth=None, stream=None, compact=False);
pp2 = pprint.PrettyPrinter(indent=4, width=80, depth=None, stream=None, compact=False);

fr = open("haru_station_locations.py", "r", encoding="utf-8");
fw = open("united_info_draft.json", "w", encoding="utf-8");

######################################################
# phase1のみ, pprintを用いず手動でjsonを構築しています。
# これは, json中にコメントを残したいため・独自の整形をしたいためです。
print("# phase 1: lines");
flag_initiated = False;
fw.write('{\n');
fw.write('    \"lines\": {\n');
prev_exist_dist_info, exist_dist_info = False, False;
prev_sta_options, sta_options = '', '';
# parse haru_station_location.py manually
for line in fr: # line = 行
    if line.expandtabs(tabsize).startswith(tab2 + '#') :
        fw.write(tab2 + line);
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
                if prev_sta_options == '' :
                    fw.write(tab4 + '\"' + prev_sta_code + '\": { \"connect\": { \"');
                    fw.write(prev_line_code + prev2_sta_code + '\": ' + prev_distance + ' } }\n');
                else :
                    fw.write(tab4 + '\"' + prev_sta_code + '\": {\n');
                    fw.write(prev_sta_options);
                    fw.write(tab5 + '\"connect\": { \"' + prev_line_code + \
                        prev2_sta_code + '\": ' + prev_distance + ' }\n');
                    fw.write(tab4 + '},\n');  
            fw.write(tab3 + '}\n');
            fw.write(tab2 + '},\n');
        fw.write(tab2 + '\"' + line_code + '\": {\n');
        fw.write(tab3 + '\"name\": \"' + line_name + '\",\n');
        fw.write(tab3 + '\"company\": \"' + line_company + '\",\n');
        fw.write(tab3 + '\"author\": \"' + company_author.get(line_company,'(unknown)') + '\",\n');
        fw.write(tab3 + '\"color\": \"' + line_color + '\",\n');
        if line_code in airline :
            fw.write(tab3 + '\"airline\": true\n');
        if line_code in ship :
            fw.write(tab3 + '\"ship\": true\n');    
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
    # station options
    sta_options = '';
    if '<夜間通過>' in comment :
        sta_options += (tab5 + '\"pass_night\": true,\n');
    if '<駅共有/相互直通:' in comment :
        sta_share_list = comment.split('<駅共有/相互直通:',1)[1].split('>',1)[0].strip();
        sta_options += (tab5 + '\"share\": [ ' + sta_share_list + ' ],\n');
    dummy, dummy, comment = comment.rpartition('>'); 
    exist_dist_info = (comment.endswith('blocks') and comment.strip('blocks ').isdecimal());
    if exist_dist_info :
        distance = comment.strip('blocks ');
        # write *previous* station
        if prev_exist_dist_info :
            # when both prev and next distance info exist (distance info continue)
            if prev_sta_options == '' :
                fw.write(tab4 + '\"' + prev_sta_code + '\": { \"connect\": { \"');
                fw.write(line_code + prev2_sta_code + '\": ' + prev_distance + \
                    ', \"' + line_code + sta_code + '\": ' + distance + ' } },\n');
            else :
                fw.write(tab4 + '\"' + prev_sta_code + '\": {\n');
                fw.write(prev_sta_options);
                fw.write(tab5 + '\"connect\": { \"');
                fw.write(line_code + prev2_sta_code + '\": ' + prev_distance + \
                    ', \"' + line_code + sta_code + '\": ' + distance + ' }\n');
                fw.write(tab4 + '},\n');
        else :
            # when distance info begin
            if prev_sta_options == '' :
                fw.write(tab4 + '\"' + prev_sta_code + '\": { \"connect\": { \"');
                fw.write(line_code + sta_code + '\": ' + distance + ' } },\n');
            else :
                fw.write(tab4 + '\"' + prev_sta_code + '\": {\n');
                fw.write(prev_sta_options);
                fw.write(tab5 + '\"connect\": { \"');
                fw.write(line_code + sta_code + '\": ' + distance + ' }\n');
                fw.write(tab4 + '},\n');
        prev2_sta_code = prev_sta_code;
        prev_sta_code, prev_distance = sta_code, distance;
        prev_sta_options, prev_exist_dist_info = sta_options, exist_dist_info;
    else : 
        if prev_exist_dist_info : 
            if prev_sta_options == '' :
                fw.write(tab4 + '\"' + prev_sta_code + '\": { \"connect\": { \"');
                fw.write(line_code + prev2_sta_code + '\": ' + prev_distance + ' } }\n');
            else :
                fw.write(tab4 + '\"' + prev_sta_code + '\": {\n');
                fw.write(prev_sta_options);
                fw.write(tab5 + '\"connect\": { \"');
                fw.write(line_code + prev2_sta_code + '\": ' + prev_distance + ' }\n');
                fw.write(tab4 + '},\n');
            
        prev_sta_code = sta_code;
        prev_sta_options, prev_exist_dist_info = sta_options, exist_dist_info;
        continue;
# for end (for line in fr)

# finalize(write last last line)
fw.write(tab3 + '}\n');
fw.write(tab2 + '}\n');
fw.write(tab1 + '},\n');

print("# phase 1 complete.");

######################################################

print("# phase 2: transfer");
ui_transfer = {};
for line_code in station_locations.keys() :
    for sta_code in station_locations[line_code].keys() :
        if not sta_code in ui_transfer :
            ui_transfer[sta_code] = [];
        ui_transfer[sta_code].append(line_code + sta_code);
# delete no transfer station
ui_transfer = { k : v for k,v in ui_transfer.items() if len(v)>=2}
fw.write(tab1 + '\"transfer\": ');
fw.write((pp1.pformat(ui_transfer)).replace('{', '{\n ') \
    .replace('}', '\n'+ tab1 +'},\n').replace('\'', '\"'));
print("# phase 2 complete.");

######################################################

print("# phase 3: stations");
ui_stations = {};
for line_code in station_locations :
    ui_stations[line_code] = {};
    for sta_code in station_locations[line_code].keys():
        ui_stations[line_code][sta_code] = list(station_locations[line_code][sta_code]);
        ui_stations[line_code][sta_code].pop(); #ignore station name
        sta_name, sta_name_yomi = station_special_names.get(line_code, ({})) \
        .get(sta_code, station_names.get(sta_code, ('unknown', 'unknown')));
        ui_stations[line_code][sta_code].append(sta_name);
        ui_stations[line_code][sta_code].append(sta_name_yomi);
fw.write(tab1 + '\"stations\": ');
fw.write(
    (pp2.pformat(ui_stations)) \
    .replace(': {' + ' '*3, ': {\n' + tab3) \
    .replace(']},\n' + tab1, ']\n'+ tab2 +'},\n' + tab2) \
    .replace(' '*14, tab3) \
    .replace('\'', '\"') \
    .replace('{   ', '{\n' + tab2)
    .replace('}}', '}\n' + tab1 + '}\n')
);
fw.write('}\n');
print("# phase 3 complete.");

######################################################
