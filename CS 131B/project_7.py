from Invoice import Invoice

def main():
    # Instantiate four or more Invoice objects.
    invoice1 = Invoice("1", "Wrench", 4, 4.25)
    invoice2 = Invoice("2", "Nail", 10, 2.00)
    invoice3 = Invoice("3", "Screw", 20, 1.15)
    invoice4 = Invoice("4", "Hammer", 1, 20.49)
    
    # Immediately display all objects.
    print(invoice1)
    print(invoice2)
    print(invoice3)
    print(invoice4)

    # Mutate one or more memebers of every object.
    invoice1.set_part_number("10")
    
    invoice2.set_part_description("Long Nail")
    
    invoice3.set_part_quantity(-10)
    print(invoice3)
    invoice3.set_part_quantity(2.4)
    print(invoice3)
    invoice3.set_part_quantity(30)

    invoice4.set_part_price(-5.00)
    print(invoice4)
    invoice4.set_part_price(123.45)

    # Display all objects a second time.
    print(invoice1)
    print(invoice2)
    print(invoice3)
    print(invoice4)

    # Make two accessor calls to demonstrate that they work.
    print(invoice1.get_part_quantity())
    print(invoice2.get_part_price())

# Call main function.
main()

'''
---------------------Sample Output---------------------
Part Number: 1
Part Description: Wrench
Part Quantity: 4
Part Price: 4.25

Part Number: 2
Part Description: Nail
Part Quantity: 10
Part Price: 2.0

Part Number: 3
Part Description: Screw
Part Quantity: 20
Part Price: 1.15

Part Number: 4
Part Description: Hammer
Part Quantity: 1
Part Price: 20.49

Error. Please call this function again and enter a valid non-negative integer for the part quantity. Value set to 0.
Part Number: 3
Part Description: Screw
Part Quantity: 0
Part Price: 1.15

Error. Please call this function again and enter a valid non-negative integer for the part quantity. Value set to 0.
Part Number: 3
Part Description: Screw
Part Quantity: 0
Part Price: 1.15

Error. Please call this function again and enter a valid non-negative float for the part price. Value set to 0.
Part Number: 4
Part Description: Hammer
Part Quantity: 1
Part Price: 0

Part Number: 10
Part Description: Wrench
Part Quantity: 4
Part Price: 4.25

Part Number: 2
Part Description: Long Nail
Part Quantity: 10
Part Price: 2.0

Part Number: 3
Part Description: Screw
Part Quantity: 30
Part Price: 1.15

Part Number: 4
Part Description: Hammer
Part Quantity: 1
Part Price: 123.45

4
2.0
-------------------End Sample Output-------------------
'''