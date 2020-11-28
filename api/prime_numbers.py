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



def main():
    n = 30
    list = generate_list(n)
    prime_numbers_list = generate_prime_numbers_list(list)
    print("Prime numbers from 1 to ", n,": ", prime_numbers_list)

if __name__ == '__main__':
    main()