import math

def generate_list(n):
    return [i for i in range(1,n)]

def generate_prime_numbers_list(list):
    length = len(list)
    return [i for i in range(2,length+1) if is_prime(i)]

def is_prime(element):
    flag = True
    for i in range(2, math.floor(math.sqrt(element))+1):
        if element % i == 0:
            flag = False
            break
    return flag

def convert_to_hex(list):
    return [hex(i) for i in list]

def count_hex_values(hex_list):
    hex_dictionary = {}
    for i in hex_list:
        for char in i[2:]:
            hex_dictionary[char] = hex_dictionary[char] + 1 if char in hex_dictionary else 1

    return hex_dictionary

def main():
    n = 30
    list = generate_list(n)
    prime_numbers_list = generate_prime_numbers_list(list)
    hex_prime_numbers_list = convert_to_hex(prime_numbers_list)
    hex_dictionary = count_hex_values(hex_prime_numbers_list)
    print(hex_dictionary)

if __name__ == '__main__':
    main()