class Employee:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number
    
class ProductionWorker(Employee):
    def __init__(self, name, id_number, shift_number, pay_rate):
        super().__init__(name, id_number)
        self.__shift_number = shift_number  # Must be 1 or 2, where 1 = day shift and 2 = night shift
        self.__pay_rate = pay_rate
    
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
    
    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate
    
    def get_shift_number(self):
        return self.__shift_number
    
    def get_pay_rate(self):
        return self.__pay_rate