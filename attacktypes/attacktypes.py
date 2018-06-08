from prettytable import PrettyTable
from collections import namedtuple

Attack = namedtuple('Attack', ['Abbrev', 'Fullname', 'Description'])

class AttackTypes():

    def __init__(self):
        self.attacks = []
        self.attacks.append(
            Attack(Abbrev="",
                   Fullname="Ciphertext only",
                   Description="has a copy of the ciphertext"))

        self.attacks.append(
            Attack(Abbrev="KPA",
                   Fullname="Known Plaintext Attack",
                   Description="has a copy of the ciphertext but also of the corresponding plaintext"))

        self.attacks.append(
            Attack(Abbrev="CPA",
                   Fullname="Chosen Plaintext Attack",
                   Description="chooses the plaintext to be encrypted"))

        self.attacks.append(
            Attack(Abbrev="CCA",
                   Fullname="Chosen Ciphertext Attack",
                   Description="chooses the ciphertext to be decrypted"))

        self.attacks.append(
            Attack(Abbrev="CPCA",
                   Fullname="Chosen Plaintext and Ciphertext Attack",
                   Description="chooses any plaintext to be encrypted or ciphertext to be decrypted"))


    def printAttacks(self):
        """Print all listed attack methods."""
        table = PrettyTable()
        for attack in self.attacks:
            table.add_row(attack)

        print(str(table))
