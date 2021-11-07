def print_rangoli(size):
    # your code goes here
    lines_list = list()
    alphabet_index = size - 1
    reversed_alphabet = 'zyxwvutsrqponmlkjihgfedcba'
    dashes = (size - 1) * 2
    alphabet_index = size - 1

    for line_no in range(size):
        line = ''
        sliced_alphabet = reversed_alphabet[26 - size:]
        line = line + '-' * dashes
        #print('-'* dashes, end='')
        for j in range(line_no):
            line = line + sliced_alphabet[j] + '-'
        line = line + sliced_alphabet[line_no]
        dashes = dashes - 2

        reversed_line = ''
        for index in range(len(line) - 1):  # Create a reverse line string including all the characters except for the last which does not need to be repeated
            reversed_line = line[index] + reversed_line
        lines_list.append(line+reversed_line) # Merge the line & reversed version and send them to the list
    for line in lines_list:
        print(line)
    del lines_list[-1]
    for line in reversed(lines_list):
        print(line)



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
