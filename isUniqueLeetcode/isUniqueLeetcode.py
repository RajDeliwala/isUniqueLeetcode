'''
Cracking the coding interview
Chapter 1 - Arrays and Strings page 90
Is Unique
implement an algorithmn to determine if a string has all unique characters. What if you cannot use additonal data structures?
    Example: 
        "haha" is not unique because it has repeating "h" and "a"
        "right" is unique because it doesn't have an repeating chracters
        "HAha" is unique because we're not counting capaitalized letters to be the same as undercased letters 
First let's brute force this solution by making an function that loops through the string and compares each character to each other one and whenever it sees 
a equal value from both iterators, we add 1 to the counter. At the end if the counter is == to the size of the string then we have unique characters
'''
#Brute forced solution which has a BigO(N^2)
def compare_string(string):
    counter = 0
    for x in string:
        for y in string:
            print(x,y)
            if (x == y):
                counter += 1
    if (len(string) == counter):
        return print("All unique characters ")
    else:
        return print("No, there are duplicate characters ")

#compare_string("haha")


#Sort the string into an array and compare the outputed lengh to the length of the given string, if they are different it means we got rid of a unique character
def sort_string(string):
   array = sorted(set(string))
   if len(string) != len(array):
       return False
   else:
       return True
   

print(sort_string("yolo") == False)
print(sort_string("doge") == True)
print(sort_string("DOdo") == True)


#Set solution, add each character should be checked if exist within the set and if not add it. If dupes are seen, we know the entire string is no longer unique
#but this solution also breaks the fact we don't want to use another data structure
def hashmap_is_unique(string):
    already_seen = set()
    for char in string:
        if char not in already_seen:
            already_seen.add(char)
        else:
            return False
    return True
    
#print(hashmap_is_unique("yolo") == False)
#print(hashmap_is_unique("rad") == True)
#print(hashmap_is_unique("YOlo") == True)




#Boolean array where we have an array of 128 FALSE and we'll switch each charcter's ASCII value to true
#whenever we loop it in the for loop

def bool_is_unique(string):
    arr = [False] * 128
    for char in string:
        index = ord(char) # This gets us the ASCII value for each char
        if arr[index]:
            return False

        arr[index] = True

    return True


#print(bool_is_unique("yolo") == False)
#print(bool_is_unique("rad") == True)
#print(bool_is_unique("YOlo") == True)