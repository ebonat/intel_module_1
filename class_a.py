
class ClassA(object):
    '''
    a simple testing class
    '''

    def __init__(self):
        '''
        class constructor
        '''
        pass
    
    @classmethod 
    def function_multiplication(self, number_1, number_2):
        result = number_1 * number_2
        return result
    
    @staticmethod
    def show_message(message):
        print("The message is {}".format(message))