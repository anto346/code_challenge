'''
 Given any string, find the first non-repeating character in it and return its index and char. If it doesn't exist, return -1.
Ex: abc return a and its index here it is 0
Ex: abca return b index is 1
Ex: abcab return c index is 2
Ex: abcabc return -1
'''
my_string = input ("Enter an input\n")
print("The input string is {0}".format(my_string))
string_length = len(my_string)
#print("The string length is {0}".format(int(string_length)))

some_variable="flag_unset"
for i in (my_string):
    count = 0
    for j in range(string_length):
        if my_string[j] == i:
            count = count + 1
        if count > 1:
            #print("Repeating pattern")
            break
    if count == 1:
        #print(my_string.find(i)+1)
        my_index=my_string.find(i)
        print("The first non repeating letter is {0} and index is {1}".format(i,my_index))
        some_variable = "flag_set"
        break
if some_variable=="flag_unset":
    print("Any letter in this string is getting repeated atleast twice")
    print("-1")
