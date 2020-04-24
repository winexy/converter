from Number import Number


class Hexadecimal(Number):
    dec_to_hex = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    hex_to_dec = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    def __init__(self):
        Number.__init__(self, 16)

    def from_decimal(self, value):
        value = int(value)
        result = ""
        while value != 0:
            remainder = value % self.radix
            result += str(self.dec_to_hex.get(remainder, remainder))
            value //= self.radix
        return result[::-1]

    def to_decimal(self, value):
        value = value.upper()
        text_number = value[::-1]
        res = 0
        for index, number in enumerate(text_number):
            res += int(self.hex_to_dec.get(number, number)) * (self.radix ** index)
        return res

    def get_sum_and_carry(self, v1, v2, carry):
        v1 = str(v1).upper()
        v2 = str(v2).upper()

        v1 = self.hex_to_dec.get(v1, v1)
        v2 = self.hex_to_dec.get(v2, v2)

        v1 = int(v1)
        v2 = int(v2)

        sum = v1 + v2 + carry
        new_carry = 0

        if sum > self.radix:
            sum = sum - self.radix
            new_carry = 1
        sum = self.dec_to_hex.get(sum, sum)

        return [sum, new_carry]
