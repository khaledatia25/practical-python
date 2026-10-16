import csv
import sys


def portfolio_cost(filename: str):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        _ = next(rows)
        total_cost: float = 0.0
        for row in rows:
            shares = int(row[1])
            price = float(row[2])
            total_cost += price * shares
        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost}')
