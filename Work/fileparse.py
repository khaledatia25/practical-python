import csv


def parse_csv(
    lines,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
):
    """
    Parse a csv lines into a list of records
    """
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(lines, delimiter=delimiter)
    headers = []
    if has_headers:
        headers = next(rows)
    indicies = []
    if select:
        indicies = [headers.index(name) for name in select]
        headers = select
    records = []
    row_num = 1
    for row in rows:
        try:
            if not row:
                continue
            if indicies:
                row = [row[index] for index in indicies]
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                records.append(dict(zip(headers, row)))
            else:
                records.append(tuple(row))
        except ValueError as e:
            if not silence_errors:
                print(f"Row {row_num}: Couldn't convert {row}")
                print(f"Row 4: Reason {e}")
        row_num += 1
    return records
