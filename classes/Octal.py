from Number import Number


class Octal(Number):
    def __init__(self):
        Number.__init__(self, 8)

    def convert(self, value, from_decimal):
        value = int(value)
        return Number.convert(self, value, from_decimal)

    def to_decimal(self, value):
        res = 0
        value = int(str(value)[::-1])
        while value != 0:
            res += value % 10
            res *= self.radix
            value /= 10
            if value / 10 == 0:
                res += value
                break
        return res

    def from_decimal(self, value):
        result = ""
        while value != 0:
            remainder = value % self.radix
            result += str(remainder)
            value //= self.radix
        return result[::-1]

    def get_sum_and_carry(self, v1, v2, carry):
        sum = int(v1) + int(v2) + carry
        new_carry = 0

        if sum > self.radix - 1:
            sum = sum - self.radix
            new_carry = 1

        return [sum, new_carry]





