# a = int(input   ("Enter first number: "))
# b = int(input   ("Enter second number: "))

# if a > b:
#     print("A is greater")

# elif a < b:
#     print("B is greater")

# else:
#     print("Both are equal")


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# if num1 >= num2 and num1 >= num3:
#     print("Largest number is: ", num1)

# elif num2 >= num1 and num2 >= num3:
#     print("Largest number is: ", num2)

# else:
#     print("Largest number is: ", num3)

# year = int(input("Enter year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# def add(a, b):
#     print(a+b)

# add(2, 3)

# Even number function
# def check_even(num):
#     if num % 2 == 0:
#         return "EVEN"
#     else:
#         return "ODD"
    
# number = int(input("Enter Number: "))
# result = check_even(number)
# print(number, "is", result)

#  Square function
# def square(n):
#     return n*n

# for i in range(1, 6):
#     print (square(i))

# Vowels function
# def count_vowels(text):
#     count = 0
#     vowels = "aeiouAEIOU"

#     for char in text:
#         if char in vowels:
#             count += 1

#     return count

# print(count_vowels("Kamran Anwar"))

# name = "Kamran"
# rev = ""

# for char in name:
#     rev = char + rev

#     print(rev)

# Reverse function
# def reverse_string(text):
#     rev = ""

#     for char in text:
        
#         rev = char + rev

#     return rev

# print(reverse_string("Kamran"))

# def largest_of_three(a,b,c):
#     if a>=b and a>=c:
#         return a
    
#     elif b>=a and b>=c:
#         return b
    
#     else:
#         return c
    
# print("Largest number is: ",largest_of_three(10, 6, 8))

#  Palindrome function (words same when reversed)

# def is_palindrome(text):
#     text = text.lower()
#     rev = ""

#     for ch in text:
#         rev = ch + rev

#     return text == rev

# print(is_palindrome('level'))

#  Calculate factoriol funtion

# def cal_factorial(num):
#     result = 1

#     for i in range(1, num + 1):
#         result *= i

#     return result
    
# print(cal_factorial(6))

# Function to check prime number

# def is_prime(n):
#     if n <= 1:
#         return False
    
#     for i in range(2, n):
#         if n % i == 0:
#             return False
    
#     return True
# print(is_prime(7))

# Function to count words

# def word_count(sentence):
#     words = sentence.split()

#     return len(words)

# print(word_count("This is automation testing in python playwright"))

# Function remove duplicates from the list
# method 1
# def remove_duplicate(lst):
#     return list(set(lst))

# print(remove_duplicate([1,2,2,3,3,4,4,5,5]))

def remove_duplicate(lst):
    unique = []

    for item in lst:
        if item not in unique:
            unique.append(item)

    return unique
    
print(remove_duplicate([1,1,2,2,3,3,6,6,7,7]))