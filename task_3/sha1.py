from task_3.utils import *
from task_3.sha1_constants import *
from task_3.sha1_preprocess import *


def sha1(message: str) -> str:
    bin_message = text_to_bin(message)

    if not 0 <= len(bin_message) < 2 ** 64:
        raise ValueError(f'Message too long: {len(bin_message)} bits.')

    bin_message_padded = pad_message(bin_message)
    bin_message_blocks = split_into_blocks(bin_message_padded)

    h0, h1, h2, h3, h4 = H0, H1, H2, H3, H4

    for bin_block in bin_message_blocks:
        words = split_into_int_words(bin_block)

        a, b, c, d, e = h0, h1, h2, h3, h4
        for t in range(ROUNDS_NUMBER):
            temp = (rotate_left(a, 5, 32) + f(t, b, c, d) + e + k(t) + words[t]) % 2 ** 32
            e = d
            d = c
            c = rotate_left(b, 30, 32)
            b = a
            a = temp

        h0 = (a + h0) % 2 ** 32
        h1 = (b + h1) % 2 ** 32
        h2 = (c + h2) % 2 ** 32
        h3 = (d + h3) % 2 ** 32
        h4 = (e + h4) % 2 ** 32

    hash_result = h0 << 128 | h1 << 96 | h2 << 64 | h3 << 32 | h4
    return hex(hash_result)
