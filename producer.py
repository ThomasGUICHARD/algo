from pandas import read_csv
import random

fasta = read_csv('proteine.csv', names=[
    'accession', 'length', 'class', 'fasta'])


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'e', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def produce_protein():
    ##### For the Database ####
    for i in range(len(fasta) - 1):
        x = fasta.fasta[i]
        y = fasta.fasta[i+1]
        
        xlen= fasta.length[i]
        ylen= fasta.length[i+1]
        
            
        yield(x, y, xlen,ylen)



def produce_random(count, max_len_x=100, max_len_y=5):
    for _ in range(count):
        x = ''
        y = ''
        for _ in range(random.randint(2, max_len_x)):
            x += letters[random.randint(0, len(letters) - 1)]
        for _ in range(random.randint(2, max_len_y)):
            y += letters[random.randint(0, len(letters) - 1)]
        

        x_len=len(x)
        y_len=len(y)
        yield(x, y, x_len,y_len)


