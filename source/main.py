import csv
import operator
import re
import statistics
from copy import deepcopy
import argparse
from tabulate import tabulate
from typing import List, Callable

ops: dict[str, Callable[[str, str], bool]] = {
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
    '=': operator.eq,
    '!=': operator.ne,
    '<>': operator.ne
}  


def is_number(s: str):
    try:
        float(s)
        return True
    except ValueError:
        return False


def read_csv(filename: str) -> List[List[str]]:
    with open(filename, 'r', newline='') as file:
        return list(csv.reader(file))


def parse_condition(condition: str) -> List[str]:
    match = re.match(r'(.+?)(<=|>=|!=|=|<|>)(.+)', condition)
    if match:
        return [match.group(1).strip(), match.group(2), match.group(3).strip()]
    else:
        raise ValueError(f"Incorrect condition: {condition}")


def filter_data(data: List[List[str]], condition: str) -> List[List[str]]:
    header, sign, value = parse_condition(condition)
    header_index: int = data[0].index(header)

    if not re.match(r'^[0-9a-zA-Z]', value):
        raise ValueError("Please enter valid comparison sign")

    filtered: List[List[str]] = []
    value: float | str = float(value) if is_number(value) else value 

    for row in data[1:]:
        if is_number(row[header_index]):
            if ops[sign](float(row[header_index]), value):
                filtered.append(row)
        else:
            if ops[sign](row[header_index], value):
                filtered.append(row)

    return [data[0]] + deepcopy(filtered)


def aggregate_data(data: List[List[str]], expr: str) -> List[List[str]]:
    header, func = expr.split('=')
    header_index: int = data[0].index(header)

    funcs: dict[str, Callable[[List[float]], float]] = {
        'sum': sum,
        'min': min,
        'max': max,
        'avg': statistics.mean,
        'median': statistics.median
    }

    values: List[float] = [float(row[header_index]) for row in data[1:]]
    result: float = round(funcs[func](values), 2)

    return [[func], [result]]


def sort_data(data: List[List[str]], expr: str) -> List[List[str]]:
    if '=' in expr:
        header, order = expr.split('=')
    else:
        header, order = expr, 'asc'

    if order not in ['asc', 'desc']:
        raise ValueError("Ordering should be in ascending or descending order")

    header_index: int = data[0].index(header)
    sorted_rows: List[List[str]] = sorted(
        data[1:],
        key=lambda row: float(row[header_index]),
        reverse=(order == 'desc')
    ) if all(list(map(lambda x: is_number(x), [row[header_index] for row in data[1:]]))) else sorted(
        data[1:],
        key=lambda row: row[header_index],
        reverse=(order == 'desc')
    )

    return [data[0]] + sorted_rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', help='input for csv filename')
    parser.add_argument('--where', help='input for filtering condition')
    parser.add_argument('--order_by', help='input for ordering')
    parser.add_argument('--aggregate', help='input for aggregation')

    args = parser.parse_args()
    if not args.filename:
        raise KeyError("Filename was not found")

    data = read_csv(args.filename)

    if args.where:
        data = filter_data(data, args.where)

    if args.order_by:
        data = sort_data(data, args.order_by)

    if args.aggregate:
        data = aggregate_data(data, args.aggregate)

    print(tabulate(data, headers='firstrow', tablefmt="psql"))


if __name__ == '__main__':
    main()