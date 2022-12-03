# -*- coding: utf-8 -*-
"""
Dec 2 2022

Anthony Mak
"""

cubes = [pow(i, 3) for i in range(1, 11)]   
print("Cubes of numbers 1-10 are: {}".format(cubes))


flips = [i+j for i in ['h', 't'] for j in ['h', 't']]
print(flips)

vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
testString = input("Input a string to return vowels: ")
stringVowels = [i for i in list(testString) if i in vowels]
print(stringVowels)

quest4 = [x+y for x in [10,20,30] for y in [1,2,3]]
print(quest4)

ans4 = []

for x in range(10, 40, 10):
    for y in range(1, 4):
        ans4.append(x+y)
        
print(ans4)