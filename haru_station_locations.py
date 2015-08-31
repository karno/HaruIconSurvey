﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

# "路線コード": {
# "駅コード": (X, Y, Z, "駅名"), ...
# }, ...

station_locations = {
    # harutrak A
    "HA": {
        # 駅共有/相互直通: HBHHH
        "HHH": (-285, 59, 346, "役場前"),
        "NMU": (-369, 70, 115, "中村"),  # 298 blocks
        "MCT": (-370, 70, -45, "メガネケエスタワー前(南)"),  # 161 blocks
        "MCW": (-398, 69, -58, "メガネケエスタワー前(西)"),  # 37 blocks
        "KIS": (-531, 69, -58, "北砂漠"),  # 133 blocks
        "NUM": (-711, 69, -58, "中海町"),  # 180 blocks
        "EEE": (-803, 67, -30, "エターナルフォースブリザード城前"),  # 117 blocks
        # 片側乗入: HGYOZ 198 blocks
    },
    # harutrak B
    "HB": {
        # 駅共有/相互直通: HAHHH
        "HHH": (-285, 59, 346, "役場前"),
        "SIB": (-328, 69, 508, "新橋"),  # 199 blocks
        "JIR": (-328, 69, 713, "辞林"),  # 205 blocks
        "NEM": (-393, 69, 739, "練馬"),  # 92 blocks
        "YYY": (-612, 69, 739, "雪見町"),  # 219 blocks
    },
    # harutrak C
    "HC": {
        # 駅共有/片側乗入(逆側ポイント分岐): MMNNO(MCT方面)
        "NNO": (-266, 70, 84, "中野"),  # MMHHHへ分岐可
        # 路線共有: MMNNO-MMJJJ
        "JJJ": (-76, 72, 85, "城南"),  # 192 blocks
        "AAN": (-22, 57, 101, "空港北"),  # 65 blocks
        "JOT": (195, 77, 98, "城東"),  # 219 blocks
        "TOJ": (206, 69, -17, "藤冶湖"),  # 124 blocks
        "TSI": (206, 69, -142, "津入口"),  # 125 blocks
        "TTT": (202, 69, -363, "津港"),  # 230 blocks
        # 駅共有/相互直通: HDTTT
    },
    # harutrak D
    "HD": {
        # 特殊乗入: MCT
        "MCT": (-354, 72, -58, "メガネケエスタワー前(南)"),
        "MCW": (-370, 69, -56, "メガネケエスタワー前(西)"),
        "MCE": (-354, 72, -58, "メガネケエスタワー前(東)"),  # MM->ME: 24 blocks, MW->ME:44 blocks
        "MEH": (-279, 69, -172, "明北"),  # 187 blocks
        "YAA": (-266, 69, -363, "宿木"),  # 199 blocks
        "YTH": (-21, 69, -364, "宿津平原"),  # 245 blocks
        "TTT": (202, 69, -363, "津港"),  # 221 blocks
        # 駅共有/相互直通: HCTTT
    },
    # harutrak E
    "HE": {
        # 駅共有/片側乗入(逆側ポイント分岐): HDYAA(YT方面)
        "YAA": (-266, 69, -363, "宿木"),
        "YAB": (-279, 73, -473, "北宿木"),  # 126 blocks
        "GEJ": (-279, 73, -708, "善通寺"),  # 238 blocks
        "FUT": (-279, 73, -1012, "古谷"),  # 304 blocks
        "KAD": (-279, 73, -1537, "楓"),  # 526 blocks
        "OMR": (-279, 73, -1885, "大室"),  # 348 blocks
    },
    # harutrak F
    "HF": {
        # 駅共有/片側乗入(逆側ポイント分岐): HBJIR(SB方面)
        "JIR": (-328, 69, 71, "辞林"),
        "JIC": (-183, 71, 734, "中辞林"),  # 165 blocks
        "NIT": (44, 71, 655, "新津"),  # 306 blocks
        "CCC": (353, 65, 655, "長府"),  # 309 blocks
        "TSB": (552, 67, 655, "筑波"),  # 199 blocks
        "TSU": (764, 67, 655, "土浦"),  # 212 blocks
        "SHZ": (866, 67, 743, "下北沢"),  # 187 blocks
        "SHE": (1025, 67, 808, "東北沢"),  # 225 blocks
        "SSS": (1043, 57, 914, "下関"),  # 124 blocks
    },
    # harutrak G
    "HG": {
        # 駅共有/片側乗入(逆側ポイント分岐): HEGEJ(FT方面)
        "GEJ": (-279, 73, -708, "善通寺"),
        "GES": (-275, 73, -542, "南善通寺"),  # 170 blocks
        "YAB": (-299, 67, -467, "北宿木"),  # 98 blocks
        "YAC": (-450, 67, -467, "旧宿木"),  # <夜間通過> 151 blocks
        "YAD": (-616, 67, -467, "西宿木"),  # 166 blocks
        "KAM": (-808, 67, -372, "春日野道"),  # <夜間通過> 284 blocks
        "EEE": (-809, 67, -31, "エターナルフォースブリザード城前"),  # 341 blocks
        "YOZ": (-949, 67, 18, "夜築町"),  # 191 blocks
        "KUY": (-1408, 70, 18, "久野山"),  # 459 blocks
        "ZZZ": (-1703, 73, 4, "<仮駅>"),  # 300 blocks
    },
    # harutrak H
    "HH": {
        # 駅共有/片側乗入(逆側ポイント分岐): HAKAD(FT方面)
        "KAD": (-279, 73, -1537, "楓"),
        "AOH": (268, 73, -1559, "青木ヶ原"),  # <夜間通過> 565 blocks
        "SKV": (574, 73, -1536, "鮭の子村"),  # 323 blocks
        "IKP": (574, 73, -1278, "いくら港"),  # 258 blocks
    },
    # harutrak I
    "HI": {
        # 駅共有/片側乗入(逆側ポイント分岐): HCTSI(TT方面)
        "TSI": (206, 69, -142, "津入口"),
        "OIW": (0, 0, 0, "追分"), # TODO:測量
        "KAN": (1125, 69, 97, "北香住"),  # XXX blocks
    },
    # harutrak J
    "HJ": {
        # 駅共有: HIOIW
        "OIW": (0, 0, 0, "追分"), # TODO:測量
        "OTP": (1125, 69, 97, "大津港"),  # 1154 blocks
    },
    # harutrak 空港連絡線
    "HZ": {
        # 片側乗入: HCAAN(JOT方面)
        "AAN": (-22, 57, 101, "空港北"),
        "AAA": (9, 63, 279, "はる空港"),  # 236 blocks
    },
    # はるレール 南北快速線
    "RN": {
        "GEJ": (-268, 54, -706, "善通寺"),
        "KIM": (-411, 50, -140, "北森"),  # 756 blocks
        "HHH": (-277, 59, 346, "役場前"),  # 612 blocks
        # 駅共有/相互直通: HXHHH
    },
    # はるレール 城南線
    "RJ": {
        "EEE": (-824, 57, -84, "EFB城"),
        "NTS": (-416, 41, 96, "中津"),  # 599 blocks
        "NNC": (-227, 46, 90, "地下鉄中野"),  # 193 blocks
        "JJJ": (-84, 48, 89, "城南"),  # 143 blocks
        "KEE": (-141, 44, 225, "刑務所東"),  # 192 blocks
        "HHH": (-261, 59, 346, "役場前"),  # 314 blocks
        # 駅共有/相互直通: RTHHH
    },
    # はるレール 新津線
    "RT": {
        # 駅共有/相互直通: RJHHH
        "HHH": (-261, 59, 346, "役場前"),
        "GOJ": (-266, 48, 426, "五条"),  # 80 blocks
        "MIN": (-173, 48, 458, "北三原"),  # 122 blocks
        "KOZ": (-51, 51, 485, "古津賀"),  # 141 blocks
        "NIT": (39, 63, 649, "新津"),  # 237 blocks
        "CCC": (333, 61, 689, "長府"),  # 328 blocks
        "TSH": (448, 74, 669, "筑波高原"),  # 129 blocks
        "TSB": (556, 67, 621, "新線筑波"),  # 152 blocks
        # 片側乗入: TRSAT 99 blocks
    },
    # はるレール 城津線(西城線)
    "RS": {
        # 駅共有/相互直通: ENEEE
        "EEE": (-824, 64, -69, "EFB城"),
        "SAB": (-625, 65, 227, "西原"),  # 498 blocks
        "HHH": (-285, 43, 337, "役場前"),  # 536 blocks
        "GOJ": (0, 0, 0, "五条"), # TODO:測量
        "SIB": (0, 0, 0, "新橋"), # TODO:測量
        "MIH": (0, 0, 0, "三原"), # TODO:測量
        # 三原以南未完工
        # "JIC": (0, 0, 0, "中辞林"),
        # "MOS": (0, 0, 0, "森下"),
        # "SUB": (0, 0, 0, "水原"),
        # "KYS": (0, 0, 0, "京ヶ瀬"),
        # "NIT": (0, 0, 0, "新津"),
        # "CCC": (0, 0, 0, "長府"),
    },
    # はる急行鉄道 月沢本線
    "ET": {
        "NMU": (-357, 64, 153, "中村本町"),
        "ICJ": (-496, 76, 184, "一条"),  # 196 blocks
        "SAB": (-621, 75, 230, "西原"),  # 170 blocks
        "TYS": (-562, 72, 416, "月屋根沢"),  # 241 blocks
        "SNM": (-564, 72, 580, "スノーマン前"),  # 163 blocks
        "IBY": (-564, 72, 702, "伊吹山"),  # 122 blocks
        "YYY": (-596, 69, 747, "雪見町"),  # 74 blocks
        "YUO": (-850, 71, 715, "雪見温泉"),  # 299 blocks
        "KAI": (-1013, 77, 747, "上砂"),  # 210 blocks
        "AOM": (-1152, 72, 747, "青宮"),  # 141 blocks
        "TEK": (-1290, 77, 747, "天竜峡"),  # 139 blocks
        "NAF": (-1308, 67, 815, "南海埠頭"),  # 86 blocks
    },
    # はる急行鉄道 月沢急行線
    "EX": {
        # 駅共有/相互直通: RNHHH
        "HHH": (-277, 59, 346, "役場前"),
        "TYS": (-562, 72, 416, "月屋根沢"),  # 361 blocks
        "YYY": (-598, 74, 747, "雪見町"),  # 348 blocks
        "KAI": (-1013, 77, 747, "上砂"),  # 415 blocks
        "NAF": (-1308, 67, 815, "南海埠頭"),  # 356 blocks
    },
    # はる急行鉄道 南海急行線
    "EN": {
        # 駅共有/相互直通: RSEEE
        "EEE": (-824, 64, -69, "EFB城"),
        "YOZ": (-944, 73, 5, "夜築町"),  # 184 blocks
        "KAI": (-998, 70, 747, "上砂"),  # 774 blocks
        "TOT": (-1220, 68, 1115, "鳥取"),  # 498 blocks
        "CTS": (-1648, 680, 1446, "千歳"),  # 578 blocks
        "SAN": (-1669, 64, 1980, "作並"),  # 542 blocks
    },
    # はる急行鉄道 北見線
    "EK": {
        # 駅共有/相互直通: ESTYS
        "TYS": (-553, 72, 416, "月屋根沢"),
        "KOT": (-519, 76, 249, "こむぎこタワー"),  # 214 blocks
        "SAB": (-629, 75, 230, "西原"),  # 125 blocks
        "HIZ": (-834, 64, 190, "雲雀坂"),  # 281 blocks
        "YOZ": (0, 0, 0, "夜築町"),  # TODO:測量(経路変更,駅位置変更)
        "YUB": (0, 0, 0, "結上橋"),  # TODO:測量
        "KIH": (0, 0, 0, "北見平原"),  # TODO:測量
        "HGZ": (0, 0, 0, "星川銀座"),  # TODO:測量
        "WKN": (0, 0, 0, "稚内"),  # TODO:測量
    },
    # はる急行鉄道 参宮線
    "ES": {
        # 駅共有/相互直通: EKTYS
        "TYS": (-553, 72, 416, "月屋根沢"),
        "TSS": (-519, 79, 478, "月山神社"),  # 97 blocks
        "SIB": (-321, 64, 499, "新橋"),  # 243 blocks
    },
    # はる急行鉄道 中部丘陵線
    "EC": {
        # 駅共有/相互直通: ETNMU
        "NMU": (-357, 64, 153, "中村本町"),
        "MCT": (-358, 66, -38, "メガネケエスタワー"),  # 193 blocks
        "MOY": (-233, 65, -73, "守山"),  # 155 blocks
        "JOH": (-78, 67, -73, "城北"),  # 155 blocks
        "TSI": (198, 64, -151, "津入口"),  # 349 blocks
    },
    # はる高速旅客鉄道 中央新幹線
    "SC": {
        "WKN": (0, 0, 0, "稚内"),  # TODO:測量
        "EEE": (-837, 69, -53, "EFB城"),  # XXX blocks
        "HHH": (-287, 54, 377, "新役場"),  # 798 blocks
        "AAA": (44, 54, 275, "はる空港"),  # 375 blocks
        "CCN": (319, 64, 566, "新長府"),  # 431 blocks
        "SSS": (1026, 65, 901, "下関"),  # 852 blocks
        "NGO": (1678, 76, 1443, "名古屋"),  # 892 blocks
    },
    # はる高速旅客鉄道 南北新幹線
    "SN": {
        "TTT": (158, 71, -346, "津港"),
        "JJJ": (-66, 54, 78, "城南"),  # 526 blocks
        "HHH": (-270, 39, 388, "新役場"),  # 396 blocks
        "YYY": (-602, 60, 755, "雪見町"),  # 517 blocks
    },
    # ムメイ高速鉄道 ムメイ高速鉄道本線
    "MM": {
        # 特殊乗入: MCT
        "MCE": (-354, 72, -58, "メガネケエスタワー前(東)"),
        "NNO": (-266, 70, 84, "中野"),  # 228 blocks
        # 路線共有: HCNNO - HCJJJ
        # 駅共有/片側乗入(逆側ポイント分岐): HCJJJ(NNO方面)
        "JJJ": (-76, 72, 85, "城南"),
        "HHH": (-258, 67, 295, "役場前(東梅田)"),  # NK-HH: 230, JJJ->HHH: 388
        "SHK": (-163, 67, 312, "湘南海岸"),  # 112 blocks
        "AAA": (38, 68, 312, "はる空港"),  # 201 blocks
        "TYF": (361, 68, 312, "調布"),  # 322 blocks
        "KAS": (1203, 68, 312, "香住"),  # 843 blocks
    },
    # ムメイ高速鉄道 香住線
    "MK": {
        "KAS": (1187, 64, 312, "香住"),
        "KAN": (1127, 64, 124, "北香住"),  # 249 blocks
    },
    # はる近郊鉄道 内環線
    "NI": {
        "JIR": (-328, 74, 720, "辞林"),  # XXX blocks
        "SAO": (-429, 53, 564, "ささみ温泉"),  # 247 blocks
        "TSS": (-491, 76, 487, "月山神社"),  # 117 blocks
        "KOT": (-502, 76, 249, "こむぎこタワー"),  # 254 blocks
        "TAI": (-432, 69, 199, "絶海池"),  # 97 blocks
        "NTS": (-426, 38, 84, "中津"),  # 121 blocks
        "NMU": (-379, 55, 96, "中村"),  # 51 blocks
        "NNO": (0, 0, 0, "中野"),  # TODO:測量(移設したため)
        "KEE": (-162, 66, 222, "刑務所東"),  # XXX blocks
        "SHK": (-173, 72, 308, "湘南海岸"),  # 91 blocks
        "SHJ": (-173, 47, 411, "しきみ城"),  # XXX blocks
        "MIN": (-175, 53, 449, "北三原"),  # 41 blocks
        "MIH": (0, 0, 0, "三原"),  # TODO:測量(移設したため)
    },
    # はる近郊鉄道 空港線
    "NA": {
        # 駅共有/片側乗入(逆側ポイント分岐): NIKEE(SG方面)
        "KEE": (-162, 66, 222, "刑務所東"),
        "JJJ": (-92, 63, 96, "城南"),  # 193 blocks
        "AAN": (-35, 49, 94, "空港北"),  # 79 blocks
    },
    # こむぎ娘レールウェイ 千歳線
    "KC": {
        "YYY": (-602, 82, 757, "雪見町"),
        "TAS": (-726, 91, 860, "高瀬"),  # 219 blocks
        "DAS": (-1188, 76, 855, "大山"),  # 462 blocks
        "TOT": (-1233, 72, 1123, "鳥取"),  # 319 blocks
        "HIO": (-1442, 98, 1204, "光が丘"),  # <夜間通過> 288 blocks
        "CTS": (-1664, 74, 1430, "千歳"),  # 450 blocks
        "CTM": (-1663, 67, 1596, "南千歳"),  # <夜間通過> 166 blocks
        "SAN": (-1636, 82, 2012, "作並"),  # 517 blocks
    },
    # こむぎ娘レールウェイ 海岸線
    "KK": {
        "CTS": (-1665, 74, 1430, "千歳"),
        "CTK": (-1830, 78, 1446, "千歳海岸"),  # 177 blocks
    },
    # こむぎ娘レールウェイ 作長線
    "KS": {
        "SAN": (-1644, 74, 2006, "作並"),
        "SOG": (-1086, 80, 2000, "蘇我"),  # 562 blocks
        "FUK": (-633, 64, 1920, "船越"),  # 617 blocks
        "OTK": (243, 89, 1691, "大月"),  # 1170 blocks
        "MIS": (251, 73, 1177, "水無瀬"),  # 522 blocks
        "ODW": (349, 76, 901, "小田原"),  # 373 blocks
        "CCC": (333, 61, 682, "長府"),  # 264 blocks
    },
    # こむぎ娘レールウェイ 東海線
    "KT": {
        "OTK": (246, 95, 1678, "大月"),
        "KUM": (949, 70, 1477, "国見"),  # 933 blocks
        "SSS": (1085, 50, 930, "下関"),  # 761 blocks
        "KAS": (1180, 51, 371, "香住"),  # 756 blocks
    },
    # こむぎ娘レールウェイ 東西線
    "KO": {
        "NNO": (0, 0, 0, "中野"),  # TODO:測量
        "KOT": (0, 0, 0, "こむぎこタワー"),  # TODO:測量
        "NIZ": (0, 0, 0, "西塚"),  # TODO:測量
        "AOM": (0, 0, 0, "青宮"),  # TODO:測量
        "DAS": (0, 0, 0, "大山"),  # TODO:測量
    },
    # 東部環状鉄道 東部環状線
    "LT": {
        "HHH": (-269, 59, 346, "役場前"),  # 107 blocks (from LTGOZ)
        "TAI": (-419, 34, 191, "絶海池"),  # 290 blocks
        "NTS": (-418, 34, 78, "中津"),  # 117 blocks
        "KIM": (-419, 50, -141, "北森"),  # 224 blocks
        "YAA": (-266, 69, -357, "宿木"),  # 370 blocks
        "TTT": (216, 69, -329, "津港"),  # 526 blocks
        "JOT": (212, 70, 88, "城東"),  # 423 blocks
        "TYF": (348, 73, 307, "調布"),  # 351 blocks
        "CCN": (370, 56, 592, "新長府"),  # 302 blocks
        "CCC": (333, 61, 670, "長府"),  # 115 blocks
        "NIT": (33, 69, 666, "新津"),  # 301 blocks
        "KYS": (25, 79, 848, "京ヶ瀬"),  # 187 blocks
        "SUB": (-83, 76, 878, "水原"),  # 140 blocks
        "MOS": (-190, 68, 841, "森下"),  # 145 blocks
        "JIC": (-190, 66, 745, "中辞林"),  # 96 blocks
        "MIH": (-190, 52, 540, "三原"),  # 206 blocks
        "SIB": (-287, 46, 515, "新橋"),  # 122 blocks
        "GOJ": (-285, 44, 443, "五条"),  # 74 blocks
    },
    # 筑波臨海高速鉄道 つくば線
    "TT": {
        "CCC": (333, 61, 674, "長府"),
        "CCN": (362, 64, 576, "新長府"),  # 140 blocks
        "SHT": (434, 66, 566, "新都心"),  # 80 blocks
        "TSD": (520, 68, 566, "筑波大学"),  # 86 blocks
        "TSB": (556, 64, 630, "筑波"),  # 90 blocks
        "SAT": (653, 64, 630, "桜土浦"),  # 98 blocks
        "TSU": (0, 0, 0, "土浦"),  # TODO:測量
    },
    # 筑波臨海高速鉄道 りんかい線
    "TR": {
        "YYY": (0, 0, 0, "雪見町"),  # TODO:測量
        "JIR": (0, 0, 0, "辞林"),  # TODO:測量
        "CCN": (0, 0, 0, "新長府"),  # TODO:測量
        "TSB": (0, 0, 0, "筑波"),  # TODO:測量
        "TSU": (0, 0, 0, "土浦"),  # TODO:測量
        "OAR": (764, 67, 447, "大洗"),  # 193 blocks
        "HAS": (765, 64, 310, "浜坂"),  # 137 blocks
        "KAS": (1177, 64, 290, "香住"),  # 425 blocks
    },
    # 筑波臨海高速鉄道 下関線
    "TS": {
        "TSU": (0, 0, 0, "土浦"),  # TODO:測量
        "SHZ": (911, 67, 754, "下北沢"),  # 278 blocks
        "SIM": (911, 68, 863, "東雲"),  # 110 blocks
        "SSS": (1039, 63, 916, "下関"),  # 172 blocks
    },
    # 竜ヶ崎臨海鉄道 竜ヶ崎線
    "GR": {
        "TSB": (535, 64, 635, "筑波"),
        "RYS": (527, 66, 895, "竜ヶ崎"),  # 263 blocks
        "KOS": (619, 66, 984, "神津島"),  # 178 blocks
        "SSS": (1044, 63, 916, "下関"),  # 508 blocks
    },
    # ささみ鉄道 ちくわエクスプレス線
    "CC": {
        "HHH": (-261, 59, 346, "役場前"),
        "DAM": (-323, 89, 400, "大明神前"),  # 196 blocks
        "SAO": (-424, 82, 561, "ささみ温泉"),  # 234 blocks
        "NEM": (-409, 74, 727, "練馬"),  # 176 blocks
        "YYY": (-602, 82, 757, "雪見町"),  # 210 blocks
    },
    # 比那名居電鉄 釧結線
    "WS": {
        "KIM": (-429, 50, -137, "北森"),
        "YAE": (-377, 71, -311, "元宿木"), # 222 blocks
        "TKN": (-397, 58, -350, "筍"), # 61 blocks
        "HGW": (-534, 66, -319, "雛川"), # 162 blocks
        "KAM": (-818, 63, -330, "春日野道"), # 293 blocks
        "YUB": (-962, 65, -340, "結上橋"), # 153 blocks
        "VTX": (-1069, 64, -629, "暴龍天山"), #393 blocks
        "KUS": (-964, 67, -862, "釧路"), # 335 blocks
    },
    # 比那名居電鉄 百合線
    "WY": {
        "KUS": (-949, 51, -874, "釧路"), 
        "KRM": (-801, 71, -875, "桐間"), # 148 blocks
        "TTM": (-581, 72, -876, "戸津美"), # 220 blocks
        "UJM": (-345, 74, -874, "宇治松"), # 236 blocks
        "KFH": (-243, 92, -874, "香風ヶ丘"), # 102 blocks
        "TDB": (9, 63, -868, "天々座湾"), # 256 blocks
        "HTO": (101, 64, -839, "保登"), # 120 blocks
    },
    # 比那名居電鉄 保宿線
    "WH": {
        "HTO": (109, 64, -841, "保登"), 
        "NAG": (-155, 64, -644, "永江池"), # 460 blocks
        "GEJ": (-277, 67, -699, "善通寺"), # 186 blocks
        "GES": (-279, 66, -547, "南善通寺"), # 154 blocks
        "YAA": (-287, 68, -372, "宿木"), # 194 blocks
        "TKN": (-384, 70, -370, "筍"), # 97 blocks
    },
    # はる航空 はる空港-津ヘリポート線
    "AT": {
        "AAA": (34, 64, 272, "はる空港"),
        "TTT": (186, 64, -387, "津ヘリポート")
    },
    # はる航空 はる空港-しきみ島線
    "AS": {
        "AAA": (38, 64, 272, "はる空港"),
        "SHI": (725, 65, -836, "しきみ島空港"),
    },
    # はる航空 はる空港-大室線
    "AO": {
        "AAA": (30, 64, 272, "はる空港"),
        "OMR": (-206, 64, -1926, "大室飛行場"),
    },
    # 船便 ship#1-ship#3線
    "S1": {
        "S01": (0, 0, 0, "ship#1"), #TODO:測量
        "S03": (0, 0, 0, "ship#3"), #TODO:測量
    },
    # 船便 大津港-ship#3線
    "S2": {
        "OTP": (0, 0, 0, "大津港"), #TODO:測量
        "S03": (0, 0, 0, "ship#3"), #TODO:測量
    },
    # 船便 いくら港-ship#3線
    "S3": {
        "IKP": (0, 0, 0, "いくら港"), #TODO:測量
        "S03": (0, 0, 0, "ship#3"), #TODO:測量
    },
    # hu2r railway Capital Line
    "ZC": {
        "FUO": (-195, 72, 344, "藤が丘"),
        "SHJ": (-178, 53, 404, "しきみ城"),  # 78 blocks
        "MIH": (-182, 57, 549, "三原"),  # 148 blocks
    },
    # SRH 外環線
    "ZG": {
        "TSB": (555, 60, 646, "筑波"),
        "NIS": (634, 53, 346, "西砂丘村"),  # 338 blocks
    },
    # かき地下鉄 姫子線
    "ZH": {
        # 駅共有/片側乗入(逆側ポイント分岐): HDYTH(YAA方面)
        "YTH": (-21, 69, -364, "宿津平原"),
        "HII": (-7, 20, -632, "遺跡"),  # 277 blocks
        "HIC": (-7, 20, -937, "姫子市"),  # 305 blocks
    },
    # 遺跡線
    "ZI": {
        "HHH": (0, 0, 0, "役場"), #TODO:測量
        "TSI": (0, 0, 0, "月山神社地下遺跡"), #TODO:測量
    },
    # キルミー鉄道 ゆっくりライン
    "ZK": {
        "HHH": (-288, 35, 337, "役場前"),
        "YUH": (-290, 8, 300, "ゆっくりハウス"),  # 101 blocks
        "HAI": (-221, 9, 300, "はるアイコン"),  # 69 blocks
        "REH": (-142, 8, 291, "れいかハウス"),  # 83 blocks
        "YUK": (-82, 10, 291, "ゆっくりライン貨物ターミナル"),  # 61 blocks
    },
    # 鮭の子村交通局 寿司線
    "ZS": {
        "SKV": (631, 63, -1471, "鮭の子村"),
        "SHI": (754, 65, -868, "しきみ島"),  # 730 blocks
    },
    # はる地下鉄 調布市地下鉄線
    "ZT": {
        "TYF": (407, 49, 336, "調布"),
        "TYE": (528, 49, 336, "東調布"),  # 121 blocks
        "NIS": (614, 49, 336, "西砂丘村"),  # 86 blocks
        "HAS": (775, 49, 323, "浜坂"),  # 170 blocks
    },
    # その他(なし)
    "ZZ": {}
}
