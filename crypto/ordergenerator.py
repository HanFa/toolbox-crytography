from prettytable import PrettyTable
from crypto.utils import factors, isPrime
from collections import namedtuple

OGPairs = namedtuple("OGPairs", ["Orders", "Generators"])

class OrderGenertor:

    def __init__(self, n: int) -> None:
        assert n > 1
        assert isPrime(n)

        self.n = n
        self.factors = factors(n - 1)
        self.pairs = []
        for i in range(1, n - 1):
            order = 1
            while i ** order % n != 1:
                order += 1

            self.pairs.append(OGPairs(Orders=order, Generators=i))

        self.init_table()


    def init_table(self):
        self.table = PrettyTable()
        for pair in self.pairs:
            self.table.add_row(pair)

        self.table.field_names = ["Orders", "Generators"]


    def print_table(self):
        print(str(self.table.get_string(sort_by="Orders")))
