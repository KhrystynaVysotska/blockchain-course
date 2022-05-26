from enum import Enum


class FormatterMode(Enum):
    INPUT = 1
    OUTPUT = 2


class ConverterMode(Enum):
    BIG_ENDIAN = 1
    LITTLE_ENDIAN = 2


class HexadecimalFormatter:
    @staticmethod
    def reverse(input_str: str) -> str:
        return input_str[::-1]

    @staticmethod
    def __format_input(hex_sequence: str) -> str:
        return hex_sequence.replace('0x', '').upper()

    @staticmethod
    def __format_output(hex_sequence: str) -> str:
        return '0x' + hex_sequence.upper()

    @classmethod
    def format(cls, hex_sequence: str, mode: FormatterMode) -> str:
        if mode == FormatterMode.INPUT:
            return cls.__format_input(hex_sequence)
        else:
            return cls.__format_output(hex_sequence)


class HexadecimalConverter:
    hex_to_decimal_map = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    decimal_to_hex_map = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    @classmethod
    def __map_hex_to_decimal(cls, hex_value: str) -> int:
        try:
            decimal_value = int(hex_value)
        except ValueError:
            decimal_value = cls.hex_to_decimal_map.get(hex_value)

        return decimal_value

    @classmethod
    def __map_decimal_to_hex(cls, decimal_value: int) -> str:
        if decimal_value < 10:
            return str(decimal_value)
        else:
            return cls.decimal_to_hex_map.get(decimal_value)

    @classmethod
    def __convert_hex_to_decimal(cls, hex_sequence: str) -> int:
        result = 0
        iterator = len(hex_sequence) - 1
        for hex_value in hex_sequence:
            decimal_value = cls.__map_hex_to_decimal(hex_value)
            result += decimal_value * (16 ** iterator)
            iterator -= 1
        return result

    @classmethod
    def __convert_decimal_to_hex(cls, decimal: int) -> str:
        hex_sequence = ''
        quotient = decimal
        while quotient != 0:
            quotient, remainder = divmod(quotient, 16)
            hex_sequence += cls.__map_decimal_to_hex(remainder)
        return hex_sequence

    @classmethod
    def convert_hex_to_decimal(cls, hex_sequence: str, mode: ConverterMode) -> int:
        prepared_hex_sequence = HexadecimalFormatter.format(hex_sequence, FormatterMode.INPUT)
        if mode == ConverterMode.LITTLE_ENDIAN:
            prepared_hex_sequence = HexadecimalFormatter.reverse(prepared_hex_sequence)
        return cls.__convert_hex_to_decimal(prepared_hex_sequence)

    @classmethod
    def convert_decimal_to_hex(cls, decimal: int, mode: ConverterMode) -> str:
        hex_sequence = cls.__convert_decimal_to_hex(decimal)
        if mode == ConverterMode.BIG_ENDIAN:
            hex_sequence = HexadecimalFormatter.reverse(hex_sequence)
        return HexadecimalFormatter.format(hex_sequence, FormatterMode.OUTPUT)
