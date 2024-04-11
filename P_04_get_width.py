# Ask user for width and loop until they
#enter a number that is more than zero

error = "please enter a number that is more that zero\n"
while True:

    try:
        #ask the user for a number
        width = float(input("width: "))

        #check that the number is more than zero
        if width > 0:
            break
        else:
            print("please enter a number that is more than zero")

    except ValueError:
        print(error)