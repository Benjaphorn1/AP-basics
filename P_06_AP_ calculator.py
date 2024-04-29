# Ask the user for the width and height
# (assume they put in valid data)
width = float(input("wdith: "))
height = float(input("Height: "))

#calculate the area / perimeter
area= width * height
perimeter = 2 * (width + height)

# output the area and perimeter
print()
print(f"perimeter: {perimeter} units")
print(f"area: {area} square units")