import itertools
import hashlib
import string
import time

print('Getting ready...')

# CONFIGURATION
LENGTH = 5
CHARACTERS = string.ascii_lowercase + string.digits
INPUT_HASH = 'efc89cd82e7de19fcb13ffb6312aaf60'

start = time.time()
# The length of all possible words are 5 characters long in this case
keywords = [''.join(i) for i  in itertools.product(CHARACTERS, repeat = LENGTH)]

print(f'Possible words generated: {time.time() - start} seconds passed')
start = time.time()

for word in keywords:
    # In this case the algoritem is MD4
    possible_hash = hashlib.new('md4', word.encode('utf-8')).hexdigest()
    if possible_hash == INPUT_HASH:
        print(f'>>> {word}')
        break

print(f'Finished: {time.time() - start} seconds passed')