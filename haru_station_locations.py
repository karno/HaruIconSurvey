# "路線コード": {
# "駅コード": (X, Y, Z, "駅名"), ...
# }, ...

station_locations = {
    # harutrak A
    "HA": {
        # 駅共有/相互直通: HBHH
        "HH": (-285, 59, 346, "役場前"),
        "NV": (-369, 70, 115, "中村"),  # 298 blocks
        "MM": (-370, 70, -45, "メガネケエスタワー前(南)"),  # 161 blocks
        "MW": (-398, 69, -58, "メガネケエスタワー前(西)"),  # 37 blocks
        "KS": (-531, 69, -58, "北砂漠"),  # 133 blocks
        "NU": (-711, 69, -58, "中海町"),  # 180 blocks
        "EE": (-803, 67, -30, "エターナルフォースブリザード城前"),  # 117 blocks
        # 片側乗入: HGYZ 198 blocks
    },
    # harutrak B
    "HB": {
        # 駅共有/相互直通: HAHH
        "HH": (-285, 59, 346, "役場前"),
        "SB": (-328, 69, 508, "新橋"),  # 199 blocks
        "JI": (-328, 69, 713, "辞林"),  # 205 blocks
        "NM": (-393, 69, 739, "練馬"),  # 92 blocks
        "YY": (-612, 69, 739, "雪見町"),  # 219 blocks
    },
    # harutrak C
    "HC": {
        # 駅共有/片側乗入(逆側ポイント分岐): MMNK(MM方面)
        "NK": (-266, 70, 84, "中野"),  # MMHHへ分岐可
        # 路線共有: MMNK-MMJJ
        "JJ": (-76, 72, 85, "城南"),  # 192 blocks
        "KN": (-22, 57, 101, "空港北"),  # 65 blocks
        "JT": (195, 77, 98, "城東"),  # 219 blocks
        "TJ": (206, 69, -17, "藤冶湖"),  # 124 blocks
        "TI": (206, 69, -142, "津入口"),  # 125 blocks
        "TT": (202, 69, -363, "津港"),  # 230 blocks
        # 駅共有/相互直通: HDTT
    },
    # harutrak D
    "HD": {
        # 特殊乗入: MM
        "MM": (-354, 72, -58, "メガネケエスタワー前(南)"),
        "MW": (-370, 69, -56, "メガネケエスタワー前(西)"),
        "ME": (-354, 72, -58, "メガネケエスタワー前(東)"),  # MM->ME: 24 blocks, MW->ME:44 blocks
        "MH": (-279, 69, -172, "明北"),  # 187 blocks
        "YA": (-266, 69, -363, "宿木"),  # 199 blocks
        "YT": (-21, 69, -364, "宿津平原"),  # 245 blocks
        "TT": (202, 69, -363, "津港"),  # 221 blocks
        # 駅共有/相互直通: HCTT
    },
    # harutrak E
    "HE": {
        # 駅共有/片側乗入(逆側ポイント分岐): HDYA(YT方面)
        "YA": (-266, 69, -363, "宿木"),
        "YB": (-279, 73, -473, "北宿木"),  # 126 blocks
        "GJ": (-279, 73, -708, "善通寺"),  # 238 blocks
        "FT": (-279, 73, -1012, "古谷"),  # 304 blocks
        "KD": (-279, 73, -1537, "楓"),  # 526 blocks
        "OM": (-279, 73, -1885, "大室"),  # 348 blocks
    },
    # harutrak F
    "HF": {
        # 駅共有/片側乗入(逆側ポイント分岐): HBJI(SB方面)
        "JI": (-328, 69, 71, "辞林"),
        "NJ": (-183, 71, 734, "中辞林"),  # 165 blocks
        "NT": (44, 71, 655, "新津"),  # 306 blocks
        "CC": (353, 65, 655, "長府"),  # 309 blocks
        "TK": (552, 67, 655, "筑波"),  # 199 blocks
        "TU": (764, 67, 655, "土浦"),  # 212 blocks
        "SK": (866, 67, 743, "下北沢"),  # 187 blocks
        "HK": (1025, 67, 808, "東北沢"),  # 225 blocks
        "SS": (1043, 57, 914, "下関"),  # 124 blocks
    },
    # harutrak G
    "HG": {
        # 駅共有/片側乗入(逆側ポイント分岐): HEGJ(FT方面)
        "GJ": (-279, 73, -708, "善通寺"),
        "MG": (-275, 73, -542, "南善通寺"),  # 170 blocks
        "YB": (-299, 67, -467, "北宿木"),  # 98 blocks
        "YC": (-450, 67, -467, "旧宿木"),  # <夜間通過> 151 blocks
        "YD": (-616, 67, -467, "西宿木"),  # 166 blocks
        "KG": (-808, 67, -372, "春日野道"),  # <夜間通過> 284 blocks
        "EE": (-809, 67, -31, "エターナルフォースブリザード城前"),  # 341 blocks
        "YZ": (-949, 67, 18, "夜築町"),  # 191 blocks
        "KU": (-1408, 70, 18, "久野山"),  # 459 blocks
        "ZZ": (-1703, 73, 4, "<仮駅>"),  # 300 blocks
    },
    # harutrak H
    "HH": {
        # 駅共有/片側乗入(逆側ポイント分岐): HAKD(FT方面)
        "KD": (-279, 73, -1537, "楓"),
        "AK": (268, 73, -1559, 0, 0, "青木ヶ原"),  # <夜間通過> 565 blocks
        "SV": (574, 73, -1536, "鮭の子村"),  # 323 blocks
        "SP": (574, 73, -1278, "鮭の子港"),  # 258 blocks
    },
    # harutrak I
    "HI": {
        # 駅共有/片側乗入(逆側ポイント分岐): HCTI(TT方面)
        "TI": (206, 69, -142, "津入口"),
        "KB": (1125, 69, 97, "北香住"),  # 1154 blocks
    },
    # harutrak 空港連絡線
    "HZ": {
        # 片側乗入: HC(JT方面)
        "KN": (-22, 57, 101, "空港北"),
        "AA": (9, 63, 279, "はる空港"),  # 236 blocks
    },
    # はるレール 南北快速線
    "RN": {
        "GJ": (-268, 54, -706, "善通寺"),
        "KM": (-411, 50, -140, "北森"),  # 756 blocks
        "HH": (-277, 59, 346, "役場前"),  # 612 blocks
        # 駅共有/相互直通: HXHH
    },
    # はるレール 城南線
    "RJ": {
        "EE": (-824, 57, -84, "EFB城"),
        "NA": (-416, 41, 96, "中津"),  # 599 blocks
        "CN": (-227, 46, 90, "地下鉄中野"),  # 193 blocks
        "JJ": (-84, 48, 89, "城南"),  # 143 blocks
        "KH": (-141, 44, 225, "刑務所東"),  # 192 blocks
        "HH": (-261, 59, 346, "役場前"),  # 314 blocks
        # 駅共有/相互直通: RTHH
    },
    # はるレール 新津線
    "RT": {
        # 駅共有/相互直通: RJHH
        "HH": (-261, 59, 346, "役場前"),
        "GZ": (-266, 48, 426, "五条"),  # 80 blocks
        "MN": (-173, 48, 458, "北三原"),  # 122 blocks
        "KC": (-51, 51, 485, "古津賀"),  # 141 blocks
        "NT": (39, 63, 649, "新津"),  # 237 blocks
        "CC": (333, 61, 689, "長府"),  # 328 blocks
        "TH": (448, 74, 669, "筑波高原"),  # 129 blocks
        "TK": (556, 67, 621, "新線筑波"),  # 152 blocks
        # 片側乗入: TRST 99 blocks
    },
    # はるレール 城津線(西城線)
    "RS": {
        # 駅共有/相互直通: ENEE
        "EE": (-824, 64, -69, "EFB城"),
        "SA": (-625, 65, 227, "西原"),  # 498 blocks
        "HH": (-285, 43, 337, "役場前"),  # 536 blocks
        # 役場前以南未完工
        # "GZ": (0, 0, 0, "五条"),
        # "SB": (0, 0, 0, "新橋"),
        # "MR": (0, 0, 0, "三原"),
        # "NJ": (0, 0, 0, "中辞林"),
        # "MS": (0, 0, 0, "森下"),
        # "SU": (0, 0, 0, "水原"),
        # "KY": (0, 0, 0, "京ヶ瀬"),
        # "NT": (0, 0, 0, "新津"),
        # "CC": (0, 0, 0, "長府"),
    },
    # はる急行鉄道 月沢本線
    "ET": {
        "NV": (-357, 64, 153, "中村本町"),
        "IJ": (-496, 76, 184, "一条"),  # 196 blocks
        "SA": (-621, 75, 230, "西原"),  # 170 blocks
        "TY": (-562, 72, 416, "月屋根沢"),  # 241 blocks
        "SM": (-564, 72, 580, "スノーマン前"),  # 163 blocks
        "IB": (-564, 72, 702, "伊吹山"),  # 122 blocks
        "YY": (-596, 69, 747, "雪見町"),  # 74 blocks
        "YO": (-850, 71, 715, "雪見温泉"),  # 299 blocks
        "KI": (-1013, 77, 747, "上砂"),  # 210 blocks
        "AO": (-1152, 72, 747, "青宮"),  # 141 blocks
        "TR": (-1290, 77, 747, "天竜峡"),  # 139 blocks
        "NF": (-1308, 67, 815, "南海埠頭"),  # 86 blocks
    },
    # はる急行鉄道 月沢急行線
    "EX": {
        # 駅共有/相互直通: RNHH
        "HH": (-277, 59, 346, "役場前"),
        "TY": (-562, 72, 416, "月屋根沢"),  # 361 blocks
        "YY": (-598, 74, 747, "雪見町"),  # 348 blocks
        "KI": (-1013, 77, 747, "上砂"),  # 415 blocks
        "NF": (-1308, 67, 815, "南海埠頭"),  # 356 blocks
    },
    # はる急行鉄道 南海急行線
    "EN": {
        # 駅共有/相互直通: RSEE
        "EE": (-824, 64, -69, "EFB城"),
        "YZ": (-944, 73, 5, "夜築町"),  # 184 blocks
        "KI": (-998, 70, 747, "上砂"),  # 774 blocks
        "TO": (-1220, 68, 1115, "鳥取"),  # 498 blocks
        "CT": (-1648, 680, 1446, "千歳"),  # 578 blocks
        "SN": (-1669, 64, 1980, "作並"),  # 542 blocks
    },
    # はる急行鉄道 北見線
    "EK": {
        # 駅共有/相互直通: ESTY
        "TY": (-553, 72, 416, "月屋根沢"),
        "KT": (-519, 76, 249, "こむぎこタワー"),  # 214 blocks
        "SA": (-629, 75, 230, "西原"),  # 125 blocks
        "HB": (-834, 64, 190, "雲雀坂"),  # 281 blocks
        "EE": (-829, 49, -24, "EFB城前"),  # 253 blocks
        "YZ": (-944, 49, -6, "夜築町"),  # 131 blocks
    },
    # はる急行鉄道 参宮線
    "ES": {
        # 駅共有/相互直通: EKTY
        "TY": (-553, 72, 416, "月屋根沢"),
        "TS": (-519, 79, 478, "月山神社"),  # 97 blocks
        "SB": (-321, 64, 499, "新橋"),  # 243 blocks
    },
    # はる高速旅客鉄道 中央新幹線
    "SC": {
        "EE": (-837, 69, -53, "EFB城"),
        "HH": (-287, 54, 377, "新役場"),  # 798 blocks
        "AA": (44, 54, 275, "はる空港"),  # 375 blocks
        "SC": (319, 64, 566, "新長府"),  # 431 blocks
        "SS": (1026, 65, 901, "下関"),  # 852 blocks
        "NG": (1678, 76, 1443, "名古屋"),  # 892 blocks
    },
    # はる高速旅客鉄道 南北新幹線
    "SN": {
        "TT": (158, 71, -346, "津港"),
        "JJ": (-66, 54, 78, "城南"),  # 526 blocks
        "HH": (-270, 39, 388, "新役場"),  # 396 blocks
        "YY": (-602, 60, 755, "雪見町"),  # 517 blocks
    },
    # ムメイ高速鉄道 ムメイ高速鉄道本線
    "MM": {
        # 特殊乗入: MM
        "ME": (-354, 72, -58, "メガネケエスタワー前(東)"),
        "NK": (-266, 70, 84, "中野"),  # 228 blocks
        # 路線共有: HCNK - HCJJ
        # 駅共有/片側乗入(逆側ポイント分岐): HCJJ(NA方面)
        "JJ": (-76, 72, 85, "城南"),
        "HH": (-258, 67, 295, "役場前(東梅田)"),  # NK-HH: 230, JJ->HH: 388
        "SG": (-163, 67, 312, "湘南海岸"),  # 112 blocks
        "AA": (38, 68, 312, "はる空港"),  # 201 blocks
        "TF": (361, 68, 312, "調布"),  # 322 blocks
        "KA": (1203, 68, 312, "香住"),  # 843 blocks
    },
    # ムメイ高速鉄道 香住線
    "MK": {
        "KA": (1187, 64, 312, "香住"),
        "KB": (1127, 64, 124, "北香住"),  # 249 blocks
    },
    # はる近郊鉄道 内環線
    "NI": {
        "JI": (-328, 74, 720, "辞林"),  # 169 blocks (from NINR)
        "SI": (-429, 53, 564, "ささみ温泉"),  # 247 blocks
        "TS": (-491, 76, 487, "月山神社"),  # 117 blocks
        "KT": (-502, 76, 249, "こむぎこタワー"),  # 254 blocks
        "TA": (-432, 69, 199, "絶海池"),  # 97 blocks
        "NA": (-426, 38, 84, "中津"),  # 121 blocks
        "NV": (-379, 55, 96, "中村"),  # 51 blocks
        "NK": (-258, 74, 83, "中野"),  # 157 blocks
        "CN": (-223, 54, 90, "地下鉄中野"),  # 58 blocks
        "KH": (-162, 66, 222, "刑務所東"),  # 189 blocks
        "SG": (-173, 72, 308, "湘南海岸"),  # 91 blocks
        "FU": (-175, 72, 355, "藤が丘東"),  # 48 blocks
        "SJ": (-173, 47, 411, "しきみ城"),  # 56 blocks
        "MN": (-175, 53, 449, "北三原"),  # 41 blocks
        "MR": (-184, 52, 540, "三原"),  # 96 blocks
        "NR": (-249, 47, 654, "中森"),  # 151 blocks
    },
    # はる近郊鉄道 空港線
    "NA": {
        # 駅共有/片側乗入(逆側ポイント分岐): NIKH(SG方面)
        "KH": (-162, 66, 222, "刑務所東"),
        "JJ": (-92, 63, 96, "城南"),  # 193 blocks
        "KN": (-35, 49, 94, "空港北"),  # 79 blocks
    },
    # こむぎ娘レールウェイ 千歳線
    "KC": {
        "YY": (-602, 82, 757, "雪見町"),
        "TE": (-726, 91, 860, "高瀬"),  # 219 blocks
        "DS": (-1188, 76, 855, "大山"),  # 462 blocks
        "TO": (-1233, 72, 1123, "鳥取"),  # 319 blocks
        "HI": (-1442, 98, 1204, "光が丘"),  # <夜間通過> 288 blocks
        "CT": (-1664, 74, 1430, "千歳"),  # 450 blocks
        "MC": (-1663, 67, 1596, "南千歳"),  # <夜間通過> 166 blocks
        "SN": (-1636, 82, 2012, "作並"),  # 517 blocks
    },
    # こむぎ娘レールウェイ 海岸線
    "KK": {
        "CT": (-1665, 74, 1430, "千歳"),
        "CK": (-1830, 78, 1446, "千歳海岸"),  # 177 blocks
    },
    # こむぎ娘レールウェイ 作長線
    "KS": {
        "SN": (-1644, 74, 2006, "作並"),
        "XG": (-1086, 80, 2000, "蘇我"),  # 562 blocks
        "FK": (-633, 64, 1920, "船越"),  # 617 blocks
        "OT": (243, 89, 1691, "大月"),  # 1170 blocks
        "MI": (251, 73, 1177, "水無瀬"),  # 522 blocks
        "OD": (349, 76, 901, "小田原"),  # 373 blocks
        "CC": (333, 61, 682, "長府"),  # 264 blocks
    },
    # こむぎ娘レールウェイ 東海線
    "KT": {
        "OT": (246, 95, 1678, "大月"),
        "QM": (949, 70, 1477, "国見"),  # 933 blocks
        "SS": (1085, 50, 930, "下関"),  # 761 blocks
        "KA": (1180, 51, 371, "香住"),  # 756 blocks
    },
    # 東部環状鉄道 東部環状線
    "LT": {
        "HH": (-269, 59, 346, "役場前"),  # 107 blocks (from LTGZ)
        "TA": (-419, 34, 191, "絶海池"),  # 290 blocks
        "NA": (-418, 34, 78, "中津"),  # 117 blocks
        "KM": (-419, 50, -141, "北森"),  # 224 blocks
        "YA": (-266, 69, -357, "宿木"),  # 370 blocks
        "TT": (216, 69, -329, "津港"),  # 526 blocks
        "JT": (212, 70, 88, "城東"),  # 423 blocks
        "TF": (348, 73, 307, "調布"),  # 351 blocks
        "SC": (370, 56, 592, "新長府"),  # 302 blocks
        "CC": (333, 61, 670, "長府"),  # 115 blocks
        "NT": (33, 69, 666, "新津"),  # 301 blocks
        "KY": (25, 79, 848, "京ヶ瀬"),  # 187 blocks
        "SU": (-83, 76, 878, "水原"),  # 140 blocks
        "MS": (-190, 68, 841, "森下"),  # 145 blocks
        "NJ": (-190, 66, 745, "中辞林"),  # 96 blocks
        "MR": (-190, 52, 540, "三原"),  # 206 blocks
        "SB": (-287, 46, 515, "新橋"),  # 122 blocks
        "GZ": (-285, 44, 443, "五条"),  # 74 blocks
    },
    # 筑波臨海高速鉄道 りんかい線
    "TR": {
        "CC": (333, 61, 674, "長府"),
        "SC": (362, 64, 576, "新長府"),  # 140 blocks
        "SH": (434, 66, 566, "新都心"),  # 80 blocks
        "TD": (520, 68, 566, "筑波大学"),  # 86 blocks
        "TK": (556, 64, 630, "筑波"),  # 90 blocks
        "ST": (653, 64, 630, "桜土浦"),  # 98 blocks
        "TU": (758, 69, 626, "土浦"),  # 97 blocks
        # TRTU -> [TROA, TRSK]
        # TRTU -> TROAへは継続運転. TRTU -> TRSKへは対面乗換
        # TROA, TRSK -> TRTUは継続運転
        "OA": (764, 67, 447, "大洗"),  # 193 blocks
        "HS": (765, 64, 310, "浜坂"),  # 137 blocks
        "KA": (1177, 64, 290, "香住"),  # 425 blocks
        #
        "SK": (911, 67, 754, "下北沢"),  # 278 blocks (from TU)
        "SO": (911, 68, 863, "東雲"),  # 110 blocks
        "SS": (1039, 63, 916, "下関"),  # 172 blocks
    },
    # 竜ヶ崎臨海鉄道 竜ヶ崎線
    "GR": {
        "TK": (535, 64, 635, "筑波"),
        "RS": (527, 66, 895, "竜ヶ崎"),  # 263 blocks
        "KZ": (619, 66, 984, "神津島"),  # 178 blocks
        "SS": (1044, 63, 916, "下関"),  # 508 blocks
    },
    # ささみ鉄道 ちくわエクスプレス線
    "JC": {
        "HH": (-261, 59, 346, "役場前"),
        "DM": (-323, 89, 400, "大明神前"),  # 196 blocks
        "SI": (-424, 82, 561, "ささみ温泉"),  # 234 blocks
        "NM": (-409, 74, 727, "練馬"),  # 176 blocks
        "YY": (-602, 82, 757, "雪見町"),  # 210 blocks
    },
    # はる航空 はる空港-津ヘリポート線
    "AT": {
        "AA": (34, 64, 272, "はる空港"),
        "TT": (186, 64, -387, "津ヘリポート")
    },
    # はる航空 はる空港-しきみ島線
    "AS": {
        "AA": (38, 64, 272, "はる空港"),
        "SL": (725, 65, -836, "しきみ島空港"),
    },
    # はる航空 はる空港-大室線
    "AO": {
        "AA": (30, 64, 272, "はる空港"),
        "OM": (-206, 64, -1926, "大室飛行場"),
    },
    # hu2r railway Capital Line
    "ZC": {
        "FU": (-195, 72, 344, "藤が丘"),
        "SJ": (-178, 53, 404, "しきみ城"),  # 78 blocks
        "MR": (-182, 57, 549, "三原"),  # 148 blocks
    },
    # SRH 外環線
    "ZG": {
        "TK": (555, 60, 646, "筑波"),
        "NS": (634, 53, 346, "西砂丘村"),  # 338 blocks
    },
    # かき地下鉄 姫子線
    "ZH": {
        # 駅共有/片側乗入(逆側ポイント分岐): HDYT(YA方面)
        "YT": (-21, 69, -364, "宿津平原"),
        "HE": (-7, 20, -632, "遺跡"),  # 277 blocks
        "HM": (-7, 20, -937, "姫子市"),  # 305 blocks
    },
    # キルミー鉄道 ゆっくりライン
    "ZK": {
        "HH": (-288, 35, 337, "役場前"),
        "YH": (-290, 8, 300, "ゆっくりハウス"),  # 101 blocks
        "HA": (-221, 9, 300, "はるアイコン"),  # 69 blocks
        "RH": (-142, 8, 291, "れいかハウス"),  # 83 blocks
        "YK": (-82, 10, 291, "ゆっくりライン貨物ターミナル"),  # 61 blocks
    },
    # はる地下鉄 調布市地下鉄線
    "ZT": {
        "TF": (407, 49, 336, "調布"),
        "HT": (528, 49, 336, "東調布"),  # 121 blocks
        "NS": (614, 49, 336, "西砂丘村"),  # 86 blocks
        "HS": (775, 49, 323, "浜坂"),  # 170 blocks
    },
    # その他(なし)
    "ZZ": {}
}
