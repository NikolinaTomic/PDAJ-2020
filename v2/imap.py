import math
from multiprocessing import Pool
import tracemalloc

def generate_prime_numbers_list(n):
    if is_prime(n):
        return convert_to_hex(n)
    
def is_prime(element):
    flag = True
    for i in range(2, math.floor(math.sqrt(element))+1):
        if element % i == 0:
            flag = False
            break
    return flag

def convert_to_hex(n):
    return hex(n)

def count_hex_values(hex_list):
    hex_dictionary = {}
    for i in hex_list:
        for char in i[2:]:
            if char in hex_dictionary:
                hex_dictionary[char] +=1
            else:
                hex_dictionary[char] = 1
    return hex_dictionary

def main():
    tracemalloc.start()
    n = 500000
    hex_list = []
    with Pool(4) as pool: # 4 je broj korova koji se koristi
        r = pool.imap(generate_prime_numbers_list, range(2,n))
        for i in r:
            if i is not None:
                hex_list.append(i)

        hex_dictionary = count_hex_values(hex_list)
        print(hex_dictionary)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()

if __name__ == '__main__':
    main()