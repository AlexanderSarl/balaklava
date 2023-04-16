import json
import re

# словарь для каждого элемента из раскладки 'qwerty' и 'keyboard_vyzov', где ключ - символ (буква), значение - кортеж
# (левое число - номер клавиши в 1-ой раскладке, правое число - номер клавиши во 2-ой раскладке)
with open("cyrillic.json", "r", encoding="UTF-8") as my_file:
    cyrillic_json = my_file.read()
cyrillic = json.loads(cyrillic_json)

# словарь раскладки keyboard_vyzov для функции translation()
with open("translation_vyzov.json", "r", encoding="UTF-8") as my_file:
    translation_vyzov_json = my_file.read()
translation_vyzov = json.loads(translation_vyzov_json)

# словарь раскладки qwerty для функции translation()
# возвращает строку, в которой каждый символ сопоставляется с соответствующим символом с таблицей перевода.
with open("translation_standart.json", "r", encoding="UTF-8") as my_file:
    translation_standart_json = my_file.read()
translation_standart = json.loads(translation_standart_json)

# словарь координат
with open("data_dict.json", "r", encoding="UTF-8") as my_file:
    data_dict_json = my_file.read()
data_dict = json.loads(data_dict_json)

lfi1 = (57,)  # кортежи номеров клавиш для каждого пальца
lfi2 = (47, 48, 33, 34, 19, 20, 5, 6)
lfi3 = (46, 32, 18, 4)
lfi4 = (45, 31, 17, 3)
lfi5 = (44, 30, 16, 2, 41, 15, 58, 42, 29)
rfi1 = (57,)
rfi2 = (49, 50, 35, 36, 21, 22, 7, 8)
rfi3 = (51, 37, 23, 9)
rfi4 = (52, 38, 24, 10)
rfi5 = (53, 39, 40, 25, 26, 27, 11, 12, 13, 14, 43, 28, 54)
tr = (41, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 43, 14)  # tr - top row
ur = (16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27)  # ur - up row
hr = (30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40)  # hr - home row
lr = (44, 45, 46, 47, 48, 49, 50, 51, 52, 53)  # lr - low row

final_counter_fingers = {'f5l': 0, 'f4l': 0, 'f3l': 0, 'f2l': 0, 'f1l': 0, 'f1r': 0, 'f2r': 0, 'f3r': 0, 'f4r': 0,
                         'f5r': 0}
final_counter_fingers_qwer = {'f5l': 0, 'f4l': 0, 'f3l': 0, 'f2l': 0, 'f1l': 0, 'f1r': 0, 'f2r': 0, 'f3r': 0, 'f4r': 0,
                              'f5r': 0}


def fingers(a_str, number=0):
    """
    Функция принимает таблицу в качестве параметра и возвращает строку, в которой каждый символ сопоставляется
    с соответствующим символом в соответствии с таблицей перевода
    """
    if number == 1:
        return a_str.translate(translation_vyzov).split(',')
    else:
        return a_str.translate(translation_standart).split(',')


def value_passing_fingers(column, value):
    """
    На вход получает колону и нагрузку
    Заполняет в словарь палец += значение
    """
    match column:
        case 0 | 1:
            final_counter_fingers['f5l'] += value
        case 2:
            final_counter_fingers['f4l'] += value
        case 3:
            final_counter_fingers['f3l'] += value
        case 4 | 5:
            final_counter_fingers['f2l'] += value
        case 6 | 7:
            final_counter_fingers['f2r'] += value
        case 8:
            final_counter_fingers['f3r'] += value
        case 9:
            final_counter_fingers['f4r'] += value
        case 10 | 11 | 12:
            final_counter_fingers['f5r'] += value


def value_passing_fingers_qwer(column, value):
    """
    На вход получает колону и нагрузку
    Заполняет в словарь палец+=значение
    """
    match column:
        case 0 | 1:
            final_counter_fingers_qwer['f5l'] += value
        case 2:
            final_counter_fingers_qwer['f4l'] += value
        case 3:
            final_counter_fingers_qwer['f3l'] += value
        case 4 | 5:
            final_counter_fingers_qwer['f2l'] += value
        case 6 | 7:
            final_counter_fingers_qwer['f2r'] += value
        case 8:
            final_counter_fingers_qwer['f3r'] += value
        case 9:
            final_counter_fingers_qwer['f4r'] += value
        case 10 | 11 | 12:
            final_counter_fingers_qwer['f5r'] += value


def get_cord(symbol) -> list:
    """
     На вход получаем символ,
     на выход список из ряда и колоны
    """
    for key in data_dict:
        for value in data_dict[key]['key']:
            if value == symbol:
                return [data_dict[key]['raw'], data_dict[key]['column']]


def get_cord_qwer(symbol) -> list:
    """
     На вход получаем символ,
     на выход список из ряда и колоны
    """
    for key in data_dict:
        for value in data_dict[key]['qwer']:
            if value == symbol:
                return [data_dict[key]['raw'], data_dict[key]['column']]


def count_loading(first_sim, second_sim):
    """
    функция подсчета шагов
    на вход символ и след символ
    """
    if get_cord(first_sim)[1] == get_cord(second_sim)[1]:
        value_passing_fingers(get_cord(second_sim)[1],
                              abs(get_cord(first_sim)[0] - get_cord(second_sim)[0]))
    else:
        if get_cord(first_sim)[0] != get_cord(second_sim)[0]:
            match get_cord(second_sim)[1]:
                case 5 | 6:
                    if get_cord(second_sim)[0] == 2:
                        value_passing_fingers(get_cord(second_sim)[1], 1)
                    else:
                        value_passing_fingers(get_cord(second_sim)[1],
                                              abs(get_cord(first_sim)[0] - get_cord(second_sim)[
                                                  0]) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    if get_cord(second_sim)[0] == 2:
                        pass
                    else:
                        value_passing_fingers(get_cord(second_sim)[1],
                                              abs(get_cord(first_sim)[0] - get_cord(second_sim)[
                                                  0]))
                case 11:
                    value_passing_fingers(get_cord(second_sim)[1],
                                          abs(get_cord(first_sim)[0] - get_cord(second_sim)[
                                              0]) + 1)
                case 12:
                    value_passing_fingers(get_cord(second_sim)[1],
                                          abs(get_cord(first_sim)[0] - get_cord(second_sim)[
                                              0]) + 2)
        if get_cord(first_sim)[0] == get_cord(second_sim)[0]:
            match get_cord(second_sim)[1]:
                case 5 | 6 | 11:
                    value_passing_fingers(get_cord(second_sim)[1],
                                          abs(get_cord(second_sim)[0] - 2) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    value_passing_fingers(get_cord(second_sim)[1],
                                          abs(get_cord(second_sim)[0] - 2))
                case 12:
                    value_passing_fingers(get_cord(second_sim)[1],
                                          abs(get_cord(second_sim)[0] - 2) + 2)


def load_space_final_counter(text1):
    """
    Функция считает кол-во пробелов в тексте
    """
    text1 = re.sub(r'[^" "]', '', text1)
    final_counter_fingers_qwer['f1l'] += int(len(text1) * 0.6)
    final_counter_fingers_qwer['f1r'] += int(len(text1) * 0.4)
    final_counter_fingers['f1l'] += int(len(text1) * 0.55)
    final_counter_fingers['f1r'] += int(len(text1) * 0.45)


def count_loading_qwer(first_sim, second_sim):
    """
    На вход получает колону и нагрузку
    Заполняет в словарь палец += значение
    """
    if get_cord_qwer(first_sim)[1] == get_cord_qwer(second_sim)[1]:
        value_passing_fingers_qwer(get_cord_qwer(second_sim)[1],
                                   abs(get_cord_qwer(first_sim)[0] - get_cord_qwer(second_sim)[
                                       0]))
    else:
        if get_cord_qwer(first_sim)[0] != get_cord_qwer(second_sim)[0]:
            match get_cord_qwer(second_sim)[1]:
                case 5 | 6:
                    if get_cord_qwer(second_sim)[0] == 2:
                        value_passing_fingers_qwer(get_cord_qwer(second_sim)[1], 1)
                    else:
                        value_passing_fingers_qwer(get_cord_qwer(second_sim)[1],
                                                   abs(get_cord_qwer(first_sim)[0] -
                                                       get_cord_qwer(second_sim)[
                                                           0]) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    if get_cord_qwer(second_sim)[0] == 2:
                        pass
                    else:
                        value_passing_fingers_qwer(get_cord_qwer(second_sim)[1],
                                                   abs(get_cord_qwer(first_sim)[0] -
                                                       get_cord_qwer(second_sim)[0]))
                case 11:
                    value_passing_fingers_qwer(get_cord_qwer(second_sim)[1],
                                               abs(get_cord_qwer(first_sim)[0] -
                                                   get_cord_qwer(second_sim)[0]) + 1)
                case 12:
                    value_passing_fingers_qwer(get_cord_qwer(second_sim)[1],
                                               abs(get_cord_qwer(first_sim)[0] -
                                                   get_cord_qwer(second_sim)[0]) + 2)
        if get_cord_qwer(first_sim)[0] == get_cord_qwer(second_sim)[0]:
            match get_cord_qwer(second_sim)[1]:
                case 5 | 6 | 11:
                    value_passing_fingers_qwer(get_cord_qwer(second_sim)[1],
                                               abs(get_cord_qwer(second_sim)[0] - 2) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    value_passing_fingers_qwer(get_cord_qwer(second_sim)[1],
                                               abs(get_cord_qwer(second_sim)[0] - 2))
                case 12:
                    value_passing_fingers_qwer(get_cord_qwer(second_sim)[1],
                                               abs(get_cord_qwer(second_sim)[0] - 2) + 2)


def final_counter(text, number=0):
    """
    Функция подсчитывает количество нажатий каждого пальца (левой и правой рук)

    параметр text: вводимый текст с клавиатуры
    параметр number: определяет номер раскладки клавиатуры, number = 1 - keyboard_vyzov, number = 0 - standart
    return: функция ничего не возвращает, а записывает значения в final_counter_fingers
    """
    final_counter_fingers = {'lf5': 0, 'lf4': 0, 'lf3': 0, 'lf2': 0, 'lf1': 0, 'rf1': 0, 'rf2': 0, 'rf3': 0, 'rf4': 0,
                             'rf5': 0}
    # словарь для подсчета количества шагов, пройденных каждым пальцем
    flist = [lfi5, lfi4, lfi3, lfi2, lfi1, rfi1, rfi2, rfi3, rfi4, rfi5]
    last_finger_index = 0
    for word in text:
        if cyrillic[word][number] == 57:  # По правилу слепой печати пробел будет нажиматься той рукой, которая не была
            if last_finger_index <= 4:  # задействована при наборе последней буквы перед нажатием пробела
                final_counter_fingers['rf1'] += 1
            else:
                final_counter_fingers['lf1'] += 1
        else:
            for finger in flist:
                if cyrillic[word][number] in finger:
                    # обновляет значения словаря final_counter_fingers для каждого пальца
                    final_counter_fingers[list(final_counter_fingers.keys())[flist.index(finger)]] += 1
                    last_finger_index = flist.index(finger)
    return final_counter_fingers


def print_results():
    print(f'\t\tВЫЗОВ\t\t\t\t\t\t\tЙЦУКЕН')
    print(
        f'f1l - {final_counter_fingers["f1l"]}\tf1r - {final_counter_fingers["f1r"]}\t\t\tf1l - '
        f'{final_counter_fingers_qwer["f1l"]}\tf1r '
        f'- {final_counter_fingers_qwer["f1r"]}')
    print(
        f'f2l - {final_counter_fingers["f2l"]}\tf2r - {final_counter_fingers["f2r"]}\t\t\tf2l - '
        f'{final_counter_fingers_qwer["f2l"]}\tf2r '
        f'- {final_counter_fingers_qwer["f2r"]}')
    print(
        f'f3l - {final_counter_fingers["f3l"]}\tf3r - {final_counter_fingers["f3r"]}\t\t\tf3l - '
        f'{final_counter_fingers_qwer["f3l"]}\tf3r '
        f'- {final_counter_fingers_qwer["f3r"]}')
    print(
        f'f4l - {final_counter_fingers["f4l"]}\tf4r - {final_counter_fingers["f4r"]}\t\t\tf4l - '
        f'{final_counter_fingers_qwer["f4l"]}\tf4r '
        f'- {final_counter_fingers_qwer["f4r"]}')
    print(
        f'f5l - {final_counter_fingers["f5l"]}\tf5r - {final_counter_fingers["f5r"]}\t\t\tf5l - '
        f'{final_counter_fingers_qwer["f5l"]}\tf5r '
        f'- {final_counter_fingers_qwer["f5r"]}')


def main():
    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    load_space_final_counter(text)
    text = re.sub(r'[^А-Яа-яёЁ1-9,0]', '', text)
    text = list(text)
    list_upper_case = [i for i in text if i.isupper()]

    value_passing_fingers(0, (len(list_upper_case) * 2))
    value_passing_fingers_qwer(0, (len(list_upper_case) * 2))
    text = ''.join(text)
    text = [i.lower() for i in text]
    for i in range(1, len(text)):
        count_loading(text[i - 1], text[i])
        count_loading_qwer(text[i - 1], text[i])
    print_results()


if __name__ == "__main__":
    main()
