# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

smallest = None;
largest = None;

while True:
    number = input("Enter a number: ")
    if number == "done" :
        break
    try:
        num = int(number)

        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num
        
        if largest is None:
            largest = num
        elif num > largest:
            largest = num

    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)