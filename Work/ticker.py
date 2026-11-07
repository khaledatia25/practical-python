import csv

from follow import follow
from typing_extensions import Any


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def filter_symbols(rows, names, value: Any = "name"):
    for row in rows:
        if row[value] in names:
            yield row


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows


def ticker(portfolioname, stocklogname, fmt):
    lines = follow(stocklogname)
    import report

    portfolio = report.read_portfolio(portfolioname)
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = filter_symbols(rows, portfolio, value=0)
    import tableformat

    formatter = tableformat.create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change"])
    for name, price, change in rows:
        rowdata = [name, f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


if __name__ == "__main__":
    lines = follow("Data/stocklog.csv")
    import report

    portfolio = report.read_portfolio("Data/portfolio.csv")
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)
