# coding=utf-8
import abc


class Number:
    def __init__(self, radix):
        self.radix = radix

    def get_radix(self):
        return self.radix

    def convert(self, value, from_decimal):
        try:
            if from_decimal:
                print 'Converting from decimal...'
                result = self.from_decimal(value)
            else:
                print 'Converting to decimal...'
                result = self.to_decimal(value)
            return "Result: " + str(result)
        except ValueError:
            return "Error"

    @abc.abstractmethod
    def from_decimal(self, value):
        pass

    @abc.abstractmethod
    def to_decimal(self, value):
        pass

    def plus(self, lhs, rhs):
        [lhs, rhs] = Number.equalize_length(lhs, rhs)
        total = ""
        carry = 0

        for v1, v2 in zip(lhs, rhs)[::-1]:
            [sum, carry] = self.get_sum_and_carry(v1, v2, carry)
            total = str(sum) + total
        if carry == 1:
            total = "1" + total
        return total

    @staticmethod
    def equalize_length(lhs, rhs):
        lengths = map(lambda l: len(l), [lhs, rhs])
        max_length = max(lengths)
        return [
            lhs.zfill(max_length),
            rhs.zfill(max_length)
        ]

    @abc.abstractmethod
    def get_sum_and_carry(self, v1, v2, carry):
        pass
