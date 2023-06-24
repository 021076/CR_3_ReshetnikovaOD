from utils.functions import get_read_json, get_sort_by_date, get_choice_correct_data, get_format_date, get_masking_transaction

if __name__ == '__main__':
    data = get_read_json("operations.json")
    correct_data = get_choice_correct_data(data)
    sort_data = get_sort_by_date(correct_data, 5)

    for x in sort_data:
        date = get_format_date(x["date"])
        description = x["description"]
        if "from" in x:
            from_transaction = get_masking_transaction(x["from"])
            from_transaction_from = f"{from_transaction} ->"
        else:
            from_transaction_from = ""
        from_transaction_to = get_masking_transaction(x["to"])
        amount = x["operationAmount"]["amount"]
        name = x["operationAmount"]["currency"]["name"]
        print(f"\n{date} {description} \n{from_transaction_from} {from_transaction_to} \n{amount} {name} \n")
