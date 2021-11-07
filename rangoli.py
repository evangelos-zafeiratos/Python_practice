def print_rangoli(size):
    # your code goes here
    alphabet_index = size - 1
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    dash_number = (size-1) * 2
    for i in range(size):
        print('-'*dash_number)
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
