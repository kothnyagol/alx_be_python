#!/usr/bin/python3
class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print("Calculation type: {}".format(cls.calculation_type))
        return a * b
