#----------- STRING MANIPULATION TOOL --------
# --------------------------------------------
# Parameters expected : a string(string) and
# number of substring(k) which is a factor of len(string)
# The function splits the string and returns the
# substrings after removing all duplicate values

def merge_the_tools(string, k):
    # your code goes here
    string_list = list()
    new_string_list = list()
    no_chars = k
    new_string=''
    for i in range(len(string)):
        new_string = new_string + string[i]
        if (i+1) % no_chars == 0:
            string_list.append(new_string)
            new_string = ''
    for item in string_list: # Loop through the sliced strings
        index = 0
        while index < len(item):
            char_occurences = item.count(item[index])
            while char_occurences > 1:
                duplicate_index = item.find(item[index], index+1)
                if duplicate_index >= 0:
                    item = item[:duplicate_index] + item[duplicate_index+1:]
                    char_occurences = char_occurences - 1
            index = index + 1

        new_string_list.append(item)
    for item in new_string_list:
        print(item)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
