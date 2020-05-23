'''
For this assignment you should read the task, then below the task do what it asks you to do
based on what the task tells you do first.
EXAMPLE TASK:
'''

'''
START HERE
'''

'''Write a File'''
#1) Create a file with Python that is named after your first and last name.  
#   Then write your first name on the first line with Python and your last name
#   on the second line with Python. 
#    
me = open("joshPorter.txt", "w")
line = ["Josh\n", "Porter\n"]
me.writelines(line)
me.close()



#2) In the same file you just created describe one of the projects you created
#   with at least 5 lines and how you think you can improve.
#    
#   
part2 = open("joshPorter.txt", "a")
project = ["I\n", "will\n", "make\n", "my code\n", "more\n", "efficient\n", "by reducing\n", "my code\n", "to fewer lines\n"]
part2.writelines(project)
part2.close()


#3) Within 5 lines of the previous lines you've written on, describe what line 
#   you are on, on that line. Then close the file
#    
part3 = open("joshPorter.txt", "a")
part3.write("I am on line 12")
part3.close()

'''Read a file'''
#4) Open the previous file you created. Create an if statement that checks if
#   the mode is r. If the mode is r, create a variable named contents and set
#   the variable with .read() of the file you created. Print the contents of
#    the file. Close the file
part4 = open("joshporter.txt", "r")
if part4.mode == "r":
    contents = part4.read()
    print(contents)
part4.close()

#5) Open the same file you created. Create a variable that uses .readLines() of
# the file Create a for loop that prints each line in the file.

part5 = open("joshporter.txt", "r")
var1 = part5.readlines()
for var1 in range(0,13):
    print(var1)
part5.close()
#6) Print the first, middle, and last line in the file.

part6 = open("joshporter.txt", "r")
lines = part6.readlines()
part6.close()
print(lines[0])
print(lines[5])
print(lines[6])
print(lines[11])




