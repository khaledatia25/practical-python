class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + "") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in scv format.
    """

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in html format.
    """

    def headings(self, headers):
        content = "".join([f"<th>{h}</th>" for h in headers])
        print(f"<tr>{content}</tr>")

    def row(self, rowdata):
        content = "".join([f"<td>{d}</td>" for d in rowdata])
        print(f"<tr>{content}</tr>")


class FormatError(Exception):
    pass


def create_formatter(fmt):
    if fmt == "txt":
        return TextTableFormatter()
    elif fmt == "csv":
        return CSVTableFormatter()
    elif fmt == "html":
        return HTMLTableFormatter()
    else:
        raise FormatError(f"Unknown format {fmt}")


def print_table(portfolio, attr, formatter):
    """
    Print a nicely formatted table from a list of attrs tuples.
    """
    formatter.headings(attr)
    for s in portfolio:
        values = []
        for a in attr:
            values.append(f"{getattr(s, a)}")
        formatter.row(values)
