import json

cyrillic = {"а": (33, 33), "б": (51, 39),
            "в": (32, 16), "г": (22, 25),
            "д": (38, 23), "е": (20, 32),
            "ё": (41, 2), "ж": (39, 26),
            "з": (25, 40), "и": (48, 31),
            "й": (16, 46), "к": (19, 47),
            "л": (37, 22), "м": (47, 51),
            "н": (21, 36), "о": (36, 18),
            "п": (34, 53), "р": (35, 50),
            "с": (46, 38), "т": (49, 37),
            "у": (18, 19), "ф": (30, 52),
            "х": (26, 45), "ц": (17, 27),
            "ч": (45, 30), "ш": (23, 44),
            "щ": (24, 13), "ъ": (27, 43),
            "ы": (31, 17), "ь": (50, 20),
            "э": (40, (42, 32)), "ю": (52, (42, 19)),
            "я": (44, 24), "1": (2, 6),
            "2": (3, 9), "3": (4, 5), "4": (5, 10),
            "5": (6, 4), "6": (7, 11),
            "7": (8, 3), "8": (9, 12),
            "9": (10, 7), "0": (11, 8),
            "-": (12, (42, 48)), "=": (13, (42, 7)),
            " ": (57, 57), "(": ((54, 10), (42, 7)),
            ")": ((54, 11), (54, 9)), "*": ((54, 9), (54, 8)),
            "!": ((42, 2), (54, 12)), ",": ((54, 53), 34),
            ".": (53, 35), " ": (57, 57),
            "<": ((54, 51), (54, 20)), ">": ((54, 52), (54, 21))}

with open("cyrillic.json", "w", encoding="utf-8") as file:
    json.dump(cyrillic, file, ensure_ascii=False)


translation_vyzov = {ord("а"): "lfi2, hr, 33,", ord("б"): "rfi5, hr, 39,",
                     ord("в"): "lfi5, ur, 16,", ord("г"): "rfi5, ur, 25,",
                     ord("д"): "rfi3, ur, 23,", ord("е"): "lfi3, hr, 32,",
                     ord("ё"): "lfi5, tr, 2,", ord("ж"): "rfi5, ur, 26,",
                     ord("з"): "lfi5, hr, 40,", ord("и"): "lfi4, hr, 31,",
                     ord("й"): "lfi3, lr, 46,", ord("к"): "lfi2, lr, 47,",
                     ord("л"): "rfi2, ur, 22,", ord("м"): "rfi3, lr, 51,",
                     ord("н"): "rfi2, hr, 36,", ord("о"): "lfi2, hr, 18,",
                     ord("п"): "rfi5, lr, 53,", ord("р"): "rfi2, lr, 50,",
                     ord("c"): "rfi4, hr, 38,", ord("т"): "rfi3, hr, 37,",
                     ord("у"): "lfi1, ur, 19,", ord("ф"): "rfi4, lr, 52,",
                     ord("х"): "lfi4, lr, 45,", ord("ц"): "lfi5, lr, 27,",
                     ord("ч"): "lfi5, hr, 30,", ord("ш"): "lfi5, lr, 44,",
                     ord("щ"): "rfi5, tr, 13,", ord("ъ"): "rfi5, ur, 43,",
                     ord("ы"): "lfi4, ur, 17,", ord("ь"): "lfi1, ur, 20,",
                     ord("э"): "(lfi5, lfi3), (lr, hr), (42, 32),",
                     ord("ю"): "(lfi5, rfi4), (lr, ur), (42, 19),",
                     ord("я"): "(lfi5, rfi4), (lr, ur), (42, 24),",
                     ord("1"): "lfi1 ,tr, 6,", ord("2"): "rfi3, tr, 9,",
                     ord("3"): "lfi1, tr, 5,", ord("4"): "rfi4, tr, 10,",
                     ord("5"): "lfi3, tr, 4,", ord("6"): "rfi5, tr, 11,",
                     ord("7"): "rfi2, tr, 3,", ord("8"): "rfi3, tr, 12, ",
                     ord("9"): "rfi2, tr, 7,", ord("0"): "rfi2, tr, 8,",
                     ord("-"): "rfi5, tr, (42, 48),", ord(" "): " ",
                     ord("<"): "(lfi5, lfi1), (lr, ur), (42, 20)",
                     ord(">"): "(rfi5, rfi1), (lr, ur), (54, 21)"}

with open("translation_vyzov.json", "w", encoding="utf-8") as file:
    json.dump(translation_vyzov, file, ensure_ascii=False)

translation_standart = {ord("а"): "lfi2, hr, 33,", ord("б"): "rfi3, lr, 51,",
                        ord("в"): "lfi3, hr, 32,", ord("г"): "rfi2, ur, 22,",
                        ord("д"): "rfi4, hr, 38,", ord("е"): "lfi2, hr, 20,",
                        ord("ё"): "lfi5, tr, 41,", ord("ж"): "rfi5, hr, 39,",
                        ord("з"): "lfi5, ur, 25,", ord("и"): "lfi2, lr, 48,",
                        ord("й"): "lfi5, ur, 16,", ord("к"): "lfi2, ur, 19,",
                        ord("л"): "rfi3, hr, 37,", ord("м"): "lfi2, lr, 47,",
                        ord("н"): "rfi2, ur, 21,", ord("о"): "rfi2, hr, 36,",
                        ord("п"): "lfi2, hr, 34,", ord("р"): "rfi2, hr, 35,",
                        ord("c"): "lfi3, lr, 46,", ord("т"): "rfi2, lr, 49,",
                        ord("у"): "lfi3, ur, 18,", ord("ф"): "lfi5, hr, 30,",
                        ord("х"): "lfi4, ur, 26,", ord("ц"): "lfi4, lr, 17,",
                        ord("ч"): "lfi4, lr, 45,", ord("ш"): "rfi3, ur, 23,",
                        ord("щ"): "rfi3, ur, 24,", ord("ъ"): "rfi5, ur, 27,",
                        ord("ы"): "lfi4, hr, 31,", ord("ь"): "rfi2, lr, 50,",
                        ord("э"): "rfi5, hr, 40,", ord("ю"): "rfi4, lr, 52,",
                        ord("я"): "lfi5, lr, 44,", ord("1"): "lfi5, tr, 2,",
                        ord("2"): "lfi4, tr, 3,", ord("3"): "lfi3, tr, 4,",
                        ord("4"): "lfi2, tr, 5,", ord("5"): "lfi2, tr, 6,",
                        ord("6"): "rfi2, tr, 7,", ord("7"): "rfi2, tr, 8,",
                        ord("8"): "rfi3, tr, 9,", ord("9"): "rfi4, tr, 10,",
                        ord("0"): "rfi5, tr, 11,", ord("-"): "rfi5, tr, 12,",
                        ord("="): "rfi5, tr, 13,", ord(" "): " ",
                        ord("<"): "(rfi5, rfi3), (lr, lr), (42, 51)", ord(">"): "(rfi5, rfi4), (lr, lr), (54, 52)"}

with open("translation_standart.json", "w", encoding="utf-8") as file:
    json.dump(translation_standart, file, ensure_ascii=False)


data_dict = {"2": {"key": "ё", "qwer": "1", "raw": 0, "column": 1},
             "3": {"key": "7", "qwer": "2", "raw": 0, "column": 2},
             "4": {"key": "5", "qwer": "3", "raw": 0, "column": 3},
             "5": {"key": "3", "qwer": "4", "raw": 0, "column": 4},
             "6": {"key": "1", "qwer": "5", "raw": 0, "column": 5},
             "7": {"key": "9", "qwer": "6", "raw": 0, "column": 6},
             "8": {"key": "0", "qwer": "7", "raw": 0, "column": 7},
             "9": {"key": "2", "qwer": "8", "raw": 0, "column": 8},
             "10": {"key": "4", "qwer": "9", "raw": 0, "column": 9},
             "11": {"key": "6", "qwer": "0", "raw": 0, "column": 10},
             "12": {"key": "8", "qwer": "-", "raw": 0, "column": 11},
             "13": {"key": "=", "qwer": "=", "raw": 0, "column": 12},
             "14": {"key": "щ", "qwer": "", "raw": 0, "column": 0},
             "15": {"key": "*", "qwer": "", "raw": 0, "column": 0},
             "16": {"key": "в", "qwer": "й", "raw": 1, "column": 1},
             "17": {"key": "ы", "qwer": "ц", "raw": 1, "column": 2},
             "18": {"key": "о", "qwer": "у", "raw": 1, "column": 3},
             "19": {"key": "у", "qwer": "к", "raw": 1, "column": 4},
             "20": {"key": "ь", "qwer": "е", "raw": 1, "column": 5},
             "21": {"key": "ё", "qwer": "н", "raw": 1, "column": 6},
             "22": {"key": "л", "qwer": "г", "raw": 1, "column": 7},
             "23": {"key": "д", "qwer": "ш", "raw": 1, "column": 8},
             "24": {"key": "я", "qwer": "щ", "raw": 1, "column": 9},
             "25": {"key": "г", "qwer": "з", "raw": 1, "column": 10},
             "26": {"key": "ж", "qwer": "х", "raw": 1, "column": 11},
             "27": {"key": "ц", "qwer": "ъ", "raw": 1, "column": 12},
             "28": {"key": "ъ", "qwer": "", "raw": 0, "column": 0},
             "29": {"key": "ц", "qwer": ",", "raw": 0, "column": 0},
             "30": {"key": "ч", "qwer": "ф", "raw": 2, "column": 1},
             "31": {"key": "и", "qwer": "ы", "raw": 2, "column": 2},
             "32": {"key": "е", "qwer": "в", "raw": 2, "column": 3},
             "33": {"key": "э", "qwer": "а", "raw": 2, "column": 4},
             "34": {"key": "а", "qwer": "п", "raw": 2, "column": 5},
             "35": {"key": ",", "qwer": "р", "raw": 2, "column": 6},
             "36": {"key": ".", "qwer": "о", "raw": 2, "column": 7},
             "37": {"key": "н", "qwer": "л", "raw": 2, "column": 8},
             "38": {"key": "щ", "qwer": "д", "raw": 2, "column": 9},
             "39": {"key": "т", "qwer": "ж", "raw": 2, "column": 10},
             "40": {"key": "с", "qwer": "э", "raw": 2, "column": 11},
             "41": {"key": "б", "qwer": "ё", "raw": 0, "column": 0},
             "42": {"key": "з", "qwer": "", "raw": 0, "column": 0},
             "43": {"key": "э", "qwer": "", "raw": 0, "column": 0},
             "44": {"key": "ш", "qwer": "я", "raw": 3, "column": 1},
             "45": {"key": "х", "qwer": "ч", "raw": 3, "column": 2},
             "46": {"key": "й", "qwer": "с", "raw": 3, "column": 3},
             "47": {"key": "к", "qwer": "м", "raw": 3, "column": 4},
             "48": {"key": "-", "qwer": "и", "raw": 3, "column": 5},
             "49": {"key": "р", "qwer": "т", "raw": 3, "column": 6},
             "50": {"key": "м", "qwer": "ь", "raw": 3, "column": 7},
             "51": {"key": "ф", "qwer": "б", "raw": 3, "column": 8},
             "52": {"key": "п", "qwer": "ю", "raw": 3, "column": 9},
             "53": {"key": "ц", "qwer": ".", "raw": 3, "column": 10},
             "54": {"key": "=", "qwer": "", "raw": 3, "column": 10},
             "55": {"key": "-", "qwer": "", "raw": 0, "column": 0},
             "56": {"key": "", "qwer": "", "raw": 0, "column": 0},
             "57": {"key": " ", "qwer": " ", "raw": 0, "column": 0},
             "58": {"key": "", "qwer": "", "raw": 0, "column": 0}}

with open("data_dict.json", "w", encoding="utf-8") as file:
    json.dump(data_dict, file, ensure_ascii=False)