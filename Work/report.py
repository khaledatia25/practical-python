import stock
import tableformat
from fileparse import parse_csv
from portfolio import Portfolio
from typing_extensions import Any


def read_portfolio(name: str) -> Portfolio:
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(name) as file:
        portfolio_array = parse_csv(
            file, select=["name", "shares", "price"], types=[str, int, float]
        )
    portfolio = []
    for port in portfolio_array:
        portfolio.append(stock.Stock(port["name"], port["shares"], port["price"]))
    return Portfolio(portfolio)


def read_prices(name: str) -> dict[str, float]:
    with open(name) as file:
        pricelist = parse_csv(file, types=[str, float], has_headers=False)
        prices: dict[str, float] = dict(pricelist)
    return prices


def make_report(portfolio: Portfolio, prices: dict[str, float]):
    report = []
    for s in portfolio:
        name = s.name
        shares = s.shares
        price = prices[name]
        change = price - s.price
        report.append((name, shares, price, change))
    return report


def profit(portfolio: Portfolio, prices: dict[str, float]):
    current_value = 0.0
    gain = 0.0

    for s in portfolio:
        current_value += prices[s.name] * s.shares
        gain += (prices[s.name] - s.price) * s.shares

    return current_value, gain


def print_report(report, formatter):
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt="txt"):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args: list[str]):
    if len(args) < 3:
        raise SystemExit("invalid number of args")
    portfolio_filename = args[1]
    prices_filename = args[2]
    fmt = "txt"
    if len(args) > 3:
        fmt = args[3]
    portfolio_report(portfolio_filename, prices_filename, fmt)


if __name__ == "__main__":
    import sys

    main(sys.argv)
