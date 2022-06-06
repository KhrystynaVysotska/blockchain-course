def rotate_left(number: int, steps: int, length: int) -> int:
    return ((number << steps) % (1 << length)) | (number >> (length - steps))


def get_chunk(string: str, chunk_size: int, offset: int):
    lower_bound = offset * chunk_size
    upper_bound = (offset + 1) * chunk_size
    return string[lower_bound: upper_bound]


def text_to_bin(text: str):
    return ''.join(f"{ord(char):08b}" for char in text)
