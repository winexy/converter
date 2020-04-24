from Number import Number


class Binary(Number):
    def __init__(self):
        Number.__init__(self, 2)

    def convert(self, value, from_decimal):
        value = int(value)
        return Number.convert(self, value, from_decimal)

    def from_decimal(self, value):
        result = ""
        while value != 0:
            has_remainder = value % self.radix != 0
            result += "1" if has_remainder else "0"
            value //= self.radix
        return result[::-1]

    def to_decimal(self, value):
        text_number = str(value)[::-1]
        res = 0
        for index, value in enumerate(text_number):
            res += int(value) * (self.radix ** index)
        return res

    def get_sum_and_carry(self, v1, v2, carry):
        units_counter = int(v1) + int(v2) + carry

        if units_counter == 0:
            return ["0", 0]
        if units_counter == 1:
            return ["1", 0]
        if units_counter == 2:
            return ["0", 1]
        if units_counter == 3:
            return ["1", 1]
        return ["", 0]
