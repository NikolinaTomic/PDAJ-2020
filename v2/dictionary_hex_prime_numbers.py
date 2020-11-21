import math

def generate_list(n):
    list = []
    for i in range(1, n+1):
        list.append(i)
    
    return list

def generate_prime_numbers_list(list):
    prime_numbers_list = []
    length = len(list)
    for element in range(2,length+1):
        if is_prime(element):
            prime_numbers_list.append(element)
    
    return prime_numbers_list

def is_prime(element):
    flag = True
    for i in range(2, math.floor(math.sqrt(element))+1):
        if element % i == 0:
            flag = False
            break
    return flag

def convert_to_hex(list):
    hex_prime_numbers = []
    for i in list:
        hex_prime_numbers.append(hex(i))
    
    return hex_prime_numbers

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
    n = 30
    list = generate_list(n)
    prime_numbers_list = generate_prime_numbers_list(list)
    hex_prime_numbers_list = convert_to_hex(prime_numbers_list)
    hex_dictionary = count_hex_values(hex_prime_numbers_list)
    print(hex_dictionary)

if __name__ == '__main__':
    main()