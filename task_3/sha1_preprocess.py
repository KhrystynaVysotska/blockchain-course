from typing import List

from task_3.utils import get_chunk, rotate_left
from task_3.sha1_constants import ROUNDS_NUMBER


def split_into_blocks(bin_message: str):
    bin_message_len = len(bin_message)

    def get_block_chunk(offset: int):
        return get_chunk(string=bin_message, chunk_size=512, offset=offset)

    return map(get_block_chunk, range(bin_message_len // 512))


def split_into_int_words(block: str) -> List[int]:
    words = []
    for t in range(ROUNDS_NUMBER):
        if 0 <= t <= 15:
            word = get_chunk(string=block, chunk_size=32, offset=t)
            words.append(int(word, 2))
        if 16 <= t <= 79:
            word_xor = words[t - 3] ^ words[t - 8] ^ words[t - 14] ^ words[t - 16]
            word_shifted = rotate_left(word_xor, 1, 32)
            words.append(word_shifted)
    return words


def pad_message(bin_message: str) -> str:
    bin_message_len = len(bin_message)

    zero_block_length = 512 - (bin_message_len + 1 + 64) % 512
    zero_block = '0' * zero_block_length

    end_block = f'{bin_message_len:064b}'

    return bin_message + '1' + zero_block + end_block
