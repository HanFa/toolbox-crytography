from prettytable import PrettyTable

class Caesar():

    def __init__(self, plaintext: str) -> None:
        """Constructor takes the plaintext/Ciphertext as argument"""
        self.text = str(plaintext).lower()
        if not self.text.isalpha() or not self.text:
            print("The input text is not valid.")
            assert False

        self.table = PrettyTable(field_names=["Key", "Shifted text"])

        for shift in range(26):
            self.table.add_row((shift, self.shift_text_by(shift)))


    def shift_text_by(self, key: int) -> str:
        """Shift the input text by a certain amount, return the shifted text."""
        res = ""
        for ch in self.text:
            if ch.isalpha():
                stayInAlphabet = ord(ch) + key
                if stayInAlphabet > ord('z'):
                    stayInAlphabet -= 26
                finalLetter = chr(stayInAlphabet)
                res += finalLetter

        return res


    def print_all_keys(self) -> None:
        """Print all possible keys. Return None."""
        print(str(self.table))
        return