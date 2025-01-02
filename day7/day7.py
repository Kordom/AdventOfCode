import requests
from cookies import cookie

url = "https://adventofcode.com/2024/day/7/input"
cookies = {
    'session': cookie
}

r = requests.get(url, cookies=cookies)

OPERATORS = ['+', '*']


def split_and_make_dict(contents):
    list_of_dict = []
    for item in contents:
        key, value = item.split(": ")
        result_dict = {key: value}
        list_of_dict.append(result_dict)

    return list_of_dict


def get_values_out_of_dict(dictionary):
    key = ''
    val = ''
    for k, v in dictionary.items():
        key = k
        val = v
    return key, val


if r.status_code == 200:
    content = r.text.splitlines()
    equations = split_and_make_dict(content)

    while True:
        for elem in equations:
            values = get_values_out_of_dict(elem)
            evaluation = ''

            for i in values[1]:
                if i != " ":
                    evaluation += i
                if i == " ":
                    evaluation += OPERATORS[0]


            # evaluation = eval(values[1].replace(" ", OPERATORS[0]))
            # evaluation2 = eval(values[1].replace(" ", OPERATORS[1]))
            # if int(values[0]) == evaluation:
            #     break
            # if int(values[0]) == evaluation2:
            #     break

