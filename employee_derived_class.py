
import sys
import os

from person_base_class import Person

class Employee(Person):
    '''
    employee derived class
    '''
    
    def __init__(self, first, last, id=None):
        super().__init__(first, last)
        self.id_number = id
    
    @property
    def property_id(self):
        self.id_number
        
    @property_id.setter
    def property_id(self, new_id):
        self.id_number = new_id
    
    def employee_name(self):
        '''
        get employee name only
        :return employee name information
        '''
        try:
            employee_info = self.FirstLastName()        
        except:
            exception_message = sys.exc_info()[0]
            print("An error occurred. {}".format(exception_message))
        return employee_info
            
    def employee_name_id(self):
        '''
        get employee name and id with overridden the FirstLastName()
        :return employee name and id information
        '''
        try:
            employee_info = self.FirstLastName() + " | " +  self.id_number
        except:
            exception_message = sys.exc_info()[0]
            print("An error occurred. {}".format(exception_message))
        return employee_info


