import sys
import os

class Person(object):
    '''
    person base class
    '''
        
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def FirstLastName(self):
        '''
        get person first and last name
        :return first and last name
        '''
        try:
            first_last_name = self.firstname + " " + self.lastname            
        except:
            exception_message = sys.exc_info()[0]
            print("An error occurred. {}".format(exception_message))
        return first_last_name