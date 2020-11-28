import math

def generate_list(n):
    for i in range(1, n+1):
        yield i
    

def generate_prime_numbers_list(list):
    prime_numbers_list = []
    length = len(list)
    for element in range(2,length+1):
        if is_prime(element):
            prime_numbers_list.append(element)
    
    return prime_numbers_list

def is_prime(n):
    numbers = generate_list(n)
    for i in numbers:
        for j in range(2, i+1):
            if j==i:
                yield(i)
            if i % j == 0:
                break

def convert_to_hex(num):
    for i in is_prime(num):
        yield hex(i)
    
def count_hex_values(num):
    hex_dictionary = {}
    for i in convert_to_hex(num):
        for char in i[2:]:
            hex_dictionary[char] = hex_dictionary[char] + 1 if char in hex_dictionary else 1
    return hex_dictionary

def main():
    n = 30
    hex_dictionary = count_hex_values(n)
    print(hex_dictionary)

if __name__ == '__main__':
    main()