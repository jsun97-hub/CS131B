'''
Invoice Class.

Attibutes: 
(1) part_number, 
(2) part_description, 
(3) part_quantity, 
(4) part_price

Functions: 
(1) Getters and setters for all atributes (get_attribute or set_attribute).
(2) Calculate_invoice to determine total invoice cost for an instance of Invoice.
(3) __init__ constructor.
(4) __str__ magic method.

Description:
The Invoice class possesses attributes for a part and is able to calculate the
invoice total for an instance of the Invoice class.
'''
class Invoice:
    def __init__(self, part_number, part_description, part_quantity, part_price):
        '''
        Description: Constructor for the Invoice class. Sets part_number and part_description
        based on the arguments that are passed, and calls set_part_quantity and set_part_price
        for the part_quantity and part_price since those are validated attributes.

        Parameters: part_number, part_description, part_quantitiy, part_price

        Output: NA
        '''
        self.part_number = part_number
        self.part_description = part_description
        self.set_part_quantity(part_quantity)
        self.set_part_price(part_price)

    def set_part_number(self, part_number):
        '''
        Description: Setter for the part_number attribute.
        
        Parameters: The desired part number.

        Output: NA.
        '''
        self.part_number = part_number

    def get_part_number(self):
        '''
        Description: Getter for the part_number attribute.
        
        Parameters: NA.

        Output: The part number for this instance of the Invoice class.
        '''
        return self.part_number
    
    def set_part_description(self, part_description):
        '''
        Description: Setter for the part_description attribute.
        
        Parameters: The desired part description.

        Output: NA.
        '''
        self.part_description = part_description

    def get_part_description(self):
        '''
        Description: Getter for the part_description attribute.
        
        Parameters: NA.

        Output: The part description for this instance of the Invoice class.
        '''
        return self.part_description
    
    def set_part_quantity(self, part_quantity):
        '''
        Description: Setter for the part_quantity attribute. Includes data validation loop to ensure
        that the specified input is a non-negative integer.
        
        Parameters: The desired part quantity.

        Output: NA
        '''
        if not isinstance(part_quantity, int) or part_quantity < 0:
            self.part_quantity = 0
            print("Error. Please call this function again and enter a valid non-negative integer for the part quantity. Value set to 0.")
        else:
            self.part_quantity = part_quantity

    def get_part_quantity(self):
        '''
        Description: Getter for the part_quantity attribute.
        
        Parameters: NA.

        Output: The part quantity for this instance of the Invoice class.
        '''
        return self.part_quantity
    
    def set_part_price(self, part_price):
        '''
        Description: Setter for the part_price attribute. Includes data validation loop to ensure
        that the specified input is a non-negative float.
        
        Parameters: The desired part price.

        Output: NA
        '''
        if part_price < 0:
            self.part_price = 0
            print("Error. Please call this function again and enter a valid non-negative float for the part price. Value set to 0.")
        else:
            self.part_price = part_price

    def get_part_price(self):
        '''
        Description: Getter for the part_price attribute.
        
        Parameters: NA.

        Output: The part price for this instance of the Invoice class.
        '''
        return self.part_price
    
    def __str__(self):
        '''
        Description: Magic method that displays this Invoice class instance's attribute values.

        Parameters: NA.

        Output: The part price, description, quantity, and price for this instance of the Invoice class.
        '''
        return (f"Part Number: {self.part_number}\n"
                f"Part Description: {self.part_description}\n"
                f"Part Quantity: {self.part_quantity}\n"
                f"Part Price: {self.part_price}\n")

    def calculate_invoice(self):
        '''
        Description: This function multiplies this Invoice class instance's part quantity and part price
        to determine and return the invoice total.

        Parameters: NA.

        Output: The invoice total for this instance of the Invoice class.
        '''
        return self.part_price * self.part_quantity
# End Invoice Class defintion.