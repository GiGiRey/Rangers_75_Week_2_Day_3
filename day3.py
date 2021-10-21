def house_area():
    
    
    length=input('Please enter the length of your house: ')

    width=input('Please enter the height of your house: ')
   
    area = int(length) * int(width)

    return (f'The area of a house with length {length} and height {width} is {area} square feet')

  



def circle():

    from math import pi

    radius=input('Please enter a number that represents the radius of the circle: ')
    
    if radius.isnumeric():
        circle = 2 * pi * int(radius)
    else:
        radius=input('Please enter a VALID number: ')
        circle = 2 * pi * int(radius)

    return (f'The area of the circle with radius {radius} is {circle}.')



