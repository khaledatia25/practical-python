import sys

from report import read_portfolio


def portfolio_cost(filename: str):
    """Computes the total cost (shares*price) of a portfolio file"""
    portfolio = read_portfolio(filename)
    return portfolio.total_cost


def main(args: list[str]):
    if len(args) < 2:
        raise SystemExit("invalid number of args")
    filename = args[1]
    cost = portfolio_cost(filename)
    print(f"Total cost {cost}")


if __name__ == "__main__":
    import sys

    main(sys.argv)
