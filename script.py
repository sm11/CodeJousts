names =  (input ("Please enter list of names separated by a comma: ")).split(',')
assignments =  [int(x) for x in (input("Please enter the number of assignments separated by a comma: ")).split(',')]
grades = [int(x) for x in (input ("Please enetr the grade input separated by a comma: ")).split(',')]

# message string to be used for each student
# HINT: use .format() with this string in your for loop

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for n, a, g in zip(names, assignments, grades):
    print (message.format(n.title(),a,g, a+(2*g)))
