import sys
import re


def func_split(s):
    arr = s.split(";")
    text = arr[2].strip()
    if arr[1] == "M":
        text = text[:-2]
        index = 0
    res_list = []
    res_list = re.findall('[a-zA-Z][^A-Z]*', text)
    res = " ".join([i.lower() for i in res_list])
    print(res)


def func_combine(s):
    arr = s.split(";")
    text = arr[2].strip()
    text = text.split(" ")
    if arr[1] == "C":
        res_string = text[0].capitalize()
    else:
        res_string = text[0]
    for i in range(1, len(text)):
        res_string = res_string + text[i].capitalize()
    if arr[1] == "M":
        res_string = res_string + "()"
    print(res_string)


for line in sys.stdin:
    if 'q' == line.rstrip():
        break

    if line[0] == "S":
        func_split(line)
    elif line[0] == "C":
        func_combine(line)