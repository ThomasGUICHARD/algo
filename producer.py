
from pandas import read_csv
import random

fasta = read_csv('protein.csv', names=[
    'accession', 'class', 'length', 'fasta']).fasta

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'e', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def produce_protein():
    ##### For the Database ####
    for i in range(len(fasta) - 1):
        x = fasta[i]
        y = fasta[i+1]
        yield(x, y)


def produce_random(count, max_len_x=100, max_len_y=5):
    for _ in range(count):
        x = ''
        y = ''
        for _ in range(random.randint(2, 100)):
            x += letters[random.randint(0, len(letters) - 1)]
        for _ in range(random.randint(2, 5)):
            y += letters[random.randint(0, len(letters) - 1)]
        yield(x, y)
