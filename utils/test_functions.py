from utils import functions


def test_get_read_json():
    file = "test_file_1.json"
    result = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
              {"id": 41428829, "date": "2019-07-03T18:35:29.512364", "description": "Перевод организации"},
              {"id": 939719570, "description": "Перевод организации", "from": "Счет 75106830613657916952",
               "to": "Счет 11776614605963066702"}]
    assert functions.get_read_json(file) == result


def test_get_choice_correct_data():
    list_dict = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                  "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                  "description": "Перевод организации", "from": "Maestro 1596837868705199",
                  "to": "Счет 64686473678894779589"},
                 {"id": 41428829, "state": "STOP", "date": "2019-07-03T18:35:29.512364",
                  "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                  "description": "Перевод организации", "from": "MasterCard 7158300734726758",
                  "to": "Счет 35383033474447895560"},
                 {"id": 939719570, "state": "EXECUTED"}]
    result = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
               "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
               "description": "Перевод организации", "from": "Maestro 1596837868705199",
               "to": "Счет 64686473678894779589"}]
    assert functions.get_choice_correct_data(list_dict) == result


def test_get_sort_by_date():
    unsort_list = [{"id": 441945886, "date": "2019-08-26T10:50:58.294041"},
                   {"id": 41428829, "state": "EXECUTED", "date": "2018-07-03T18:35:29.512364"},
                   {"id": 939719570, "date": "2021-06-30T02:08:58.425572"},
                   {"id": 587085106, "state": "EXECUTED", "date": "2020-03-23T10:45:06.972075"},
                   {"id": 142264268, "date": "2022-04-04T23:20:05.206878"}]
    result = [{"id": 142264268, "date": "2022-04-04T23:20:05.206878"},
          {"id": 939719570, "date": "2021-06-30T02:08:58.425572"}]
    assert functions.get_sort_by_date(unsort_list, 2) == result



def test_get_format_date():
    assert functions.get_format_date("2022-04-04T23:20:05.206878") == "04.04.2022"


def test_get_masking_transaction():
    assert functions.get_masking_transaction("счет 12345678901234567890") == "счет **7890"
    assert functions.get_masking_transaction("карта 123456789012345") == "карта 1234 56**** *2345"
    assert functions.get_masking_transaction("карта 1234567890123456") == "карта 1234 56** **** 3456"
    assert functions.get_masking_transaction("карта 123456789012345678") == "карта 123456** ******5678"
