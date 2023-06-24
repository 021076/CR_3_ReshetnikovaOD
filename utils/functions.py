import json
from datetime import datetime


def get_read_json(file_json):
    with open(file_json, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_choice_correct_data(data):
    correct_data = []
    for x in data:
        if "state" in x and x["state"] == 'EXECUTED'and "id" in x and "date" in x and "operationAmount" in x and "description" in x and "to" in x:
            correct_data.append(x)
    return correct_data


def get_sort_by_date(correct_data, count):
    def key_sort(x):
        return x["date"]

    sort_data = sorted(correct_data, key=key_sort, reverse=True)[:count]
    return sort_data

def get_format_date(date):
    format_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    return format_date

def get_masking_transaction(transaction):
    transaction = transaction.split()
    numbers, text = transaction[-1], " ".join(transaction[:-1])
    if len(numbers) == 15:
        masking = f"{text} {numbers[:4]} {numbers[4:6]}**** *{numbers[-4:]}"
    elif len(numbers) == 16:
        masking = f"{text} {numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
    elif len(numbers) == 18:
        masking = f"{text} {numbers[:6]}** ******{numbers[-4:]}"
    elif len(numbers) == 20:
        masking = f"{text} **{numbers[-4:]}"
    return masking
