###############################################
# Python Exercises
###############################################

###############################################
# TASK 1: Examine the types of data structures.
###############################################


x = 8

y = 3.2

z = 8j + 18

a = "Hello World"

b = True

c = 23 < 22

l = [1, 2, 3, 4, "String", 3.2, False]

d = {"Name": "Jake",
     "Age": [27, 56],
     "Adress": "Downtown"}

t = ("Machine Learning", "Data Science")

s = {"Python", "Machine Learning", "Data Science", "Python"}

# List of given variables
data_list = [x, y, z, a, b, c, l, d, t, s]

# Save as 'what_is_it_type' that the variables in the list themselves and their type
what_is_it_type = ["/" + str(i) + "--->  " + str(type(i)) + " /" for i in data_list]

# Print
print(what_is_it_type)

###############################################
# TASK 2: Convert all letters of the given string expression to uppercase. Put space instead of commas and periods, separate them word by word.
###############################################

text = "The goal is to turn data into information, and information into insight."


def upper_and_space_text(text):
    '''

    Capitalizes the letters of the given text, replaces commas and periods with spaces.

    Parameters
    ----------
    text: string
        variable names are the text to be retrieved.

    Returns
    -------
    text : string
    '''

    # Convert the given text to uppercase.
    text = text.upper()

    # Use spaces instead of commas and periods.
    text = text.replace(",", " ").replace(".", " ")

    # Get the words of the text
    word_by_word = text.split()

    # print
    print(word_by_word)


# call function
upper_and_space_text(text)

###############################################
# TASK 3: Do the following tasks for the given list.
###############################################

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Step 1: Look at the number of elements of the given list.

# Keep the length of the list as 'num_of_list_elements'
num_of_list_elements = len(lst)

# print
print(num_of_list_elements)

# Step 2: Call the elements at index zero and ten.

# keep first element of list as 'zero_index'
zero_index = lst[0]

# print
print(zero_index)

# keep the last element of the list as 'tenth_index'
tenth_index = lst[-1]

# print
print(tenth_index)

# Step 3: Create a list ["D","A","T","A"] from the given list.

# get the first 3 elements of the list as 'firs_three_index_in_lst'
firs_three_index_in_lst = lst[:4]

# print
print(firs_three_index_in_lst)

# Step 4: Delete the element in the eighth index.

# delete but save the eighth element of the list as 'lst_eighth_index'
lst_eighth_index = lst.pop(8)

# print list
print(lst)

# Step 5: Add a new element.

# Add to the list 'Era with Miuul'
lst.append('Era with Miuul')

# print
print(lst)

# Step 6: Re-add element "N" to the eighth index.

# add 'N' to index 8 of the list
lst.insert(8, 'N')

# alternative way
# lst.insert(8,lst_eighth_index)

# print
print(lst)

###############################################
# TASK 4: Apply the following steps to the given dictionary structure.
###############################################

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Step 1: Access the key values.

# print dictionary key values
print(dict.keys())

# Step 2: Access the values.
print(dict.values())

# Step 3: Update the value 12 of the Daisy key to 13.

# Make the first index of the 'daisy' key value 13
dict["Daisy"][1] = 13

# print
print(dict)

# Step 4: Add a new value whose key value is Ahmet value [Turkey,24].

# Value of the 'Ahmet' key in the personal ["Turkey", 24]
dict["Ahmet"] = ["Turkey", 24]

# print
print(dict)

# Step 5: Delete Antonio from dictionary.

# del dict["Antonio"]
print(dict)

###############################################
# TASK 5: Write a function that takes a list as an argument, assigns the odd and even numbers in the list to separate lists, and returns these lists.
###############################################

l = [2, 13, 18, 93, 22]


def even_and_odd_numbers(list_of_numbers):
    '''
    Separates the elements of the given list as odd and even and adds them to the appropriate list.

    Parameters
    ----------
    list_of_numbers : list
        List of numbers

    Returns
    -------
    even_numbers : list
    odd_numbers  : list

    '''

    # lists to hold odd and even numbers
    even_numbers = []
    odd_numbers = []

    # If the index in the list is even, add it to the list of 'even_numbers', if odd, add it to the list of 'odd_numbers'
    [even_numbers.append(i) if i % 2 == 0 else odd_numbers.append(i) for i in list_of_numbers]

    return (even_numbers, odd_numbers)


even_and_odd_numbers(l)

###############################################
# TASK 6: In the list given below are the names of the students who won degrees in engineering and medicine faculties.
# While the first three students represent the success order of the engineering faculty, the last three students belong to the medical faculty student rank, respectively.
# Print the student's degrees specific to the faculty using Enumarate.
###############################################

students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

# Print the first 3 indices with ranks and then the values in the other index
result = [["From the Faculty of Engineering " + str(i) + "." + student] \
          if i < 4 else ["From the Faculty of Medicine " + str(i - 3) + ". " + student] \
          for i, student in enumerate(students, 1)]

for line in result:
    print(line)


###############################################
# TASK 7: 3 lists are given below. In the lists, there is a course code, credit and quota information, respectively. Print course information using zip.
###############################################

lesson_codes = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
credits = [3, 4, 2, 4]
quota = [30, 75, 150, 25]

print(list(zip(lesson_codes, credits, quota)))

###############################################
# TASK 8: Below are 2 sets.
# You are asked to define the function that will print the difference of the 2nd set from the 1st set, if the 1st set includes the 2nd set, if it does not cover the common elements.###############################################

set_1 = set(["data", "python"])
set_2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

print([set_1.intersection(set_2) if set_1.issuperset(set_2) else set_2.difference(set_1)])
