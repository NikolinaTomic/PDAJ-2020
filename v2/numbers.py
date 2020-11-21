def generate_list(n):
    list = []
    for i in range(1, n+1):
        list.append(i)
    
    return list

def main():
	list = generate_list(30)
	print(list)
	

if __name__ == '__main__':
    main()