import random
from time import time

sequences = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]


def print_possible_keys_number_for(sequence_length):
    # based on arrangements with repetition formula
    possible_keys_number = 2 ** sequence_length
    print(f"{sequence_length} bits: {possible_keys_number} unique keys")


def get_random_key_within(sequence_length):
    key = random.randint(0, 2 ** sequence_length - 1)
    print(f"Random {sequence_length} bits key: {bin(key)}")
    return key


def brute_force(expected_key):
    key = 0
    while key != expected_key:
        key += 1
    return key


def timer_wrapper(func, *args):
    start_time_in_ms = time() * 1000
    result = func(*args)
    end_time_in_ms = time() * 1000

    return result, end_time_in_ms - start_time_in_ms


if __name__ == "__main__":
    for sequence in sequences:
        print_possible_keys_number_for(sequence)

    print("-" * 100)

    keys = {}
    for sequence in sequences:
        keys[sequence] = get_random_key_within(sequence)

    print("-" * 100)

    for sequence in sequences:
        print(f"Started brute-force: {sequence} bits key...")
        founded_key, duration = timer_wrapper(brute_force, keys[sequence])
        print(f"Expected key: {bin(keys[sequence])}")
        print(f"Brute-force founded key: {bin(founded_key)}")
        print(f"Brute-force time: {duration} ms")

        print("-" * 100)
