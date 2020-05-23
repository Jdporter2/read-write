'''
Created on Feb 29, 2020

@author: ITAUser
'''
'''
file1 = "fileName.txt", "mode"

mode will be either r, w, a, or r+




Objective: Create new file
'''
file1 = open("hello.txt", "a")
file1.close()


string = "Hello my name is Josh"
file1.write(string)


line = ["dogs ", "are ", "cool " ]
file1.writeLines(line)
file1.close()

file1.open("hello.txt", "r")
text = file1.read()
file1.close()

print(text)