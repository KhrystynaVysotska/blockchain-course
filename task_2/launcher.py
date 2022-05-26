from task_2.converter import HexadecimalConverter, ConverterMode

if __name__ == "__main__":
    hex_seq = "0xff00000000000000000000000000000000000000000000000000000000000000"
    le_decimal = HexadecimalConverter.convert_hex_to_decimal(hex_seq, ConverterMode.LITTLE_ENDIAN)
    be_decimal = HexadecimalConverter.convert_hex_to_decimal(hex_seq, ConverterMode.BIG_ENDIAN)
    print(f"HEX -> LITTLE ENDIAN DECIMAL: {hex_seq} -> {le_decimal}")
    print(f"HEX -> BIG ENDIAN DECIMAL: {hex_seq} -> {be_decimal}")

    print('-' * 100)

    decimal = 4294967295
    le_hex = HexadecimalConverter.convert_decimal_to_hex(decimal, ConverterMode.LITTLE_ENDIAN)
    be_hex = HexadecimalConverter.convert_decimal_to_hex(decimal, ConverterMode.BIG_ENDIAN)
    print(f"LITTLE ENDIAN DECIMAL -> HEX: {decimal} -> {le_hex}")
    print(f"BIG ENDIAN DECIMAL -> HEX: {decimal} -> {be_hex}")
