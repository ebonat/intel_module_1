import sys
import config

def build_full_name1(first_name, middle_name, last_name):
    string_one_space = " "
    name = (first_name, middle_name, last_name)
    full_name = string_one_space.join(name)
    return full_name

def build_full_name2(first_name, middle_name, last_name):
    string_one_space = " "
    try:
        name = (first_name, middle_name, last_name)
        full_name = string_one_space.join(name)        
    except Exception as e:        
        print("An error occurred. {}".format(str(e)))
    finally:
        pass
    return full_name

def build_full_name3(first_name, middle_name, last_name):
    string_one_space = " "
    try:
        name = (first_name, middle_name, last_name)
        full_name = string_one_space.join(name)        
    except:
        exception_message = sys.exc_info()[0]
        print("An error occurred. {}".format(exception_message))
    return full_name

def build_full_name4(first_name, middle_name, last_name):
    string_one_space = " "
    exception_message = None
    try:
        name = (first_name, middle_name, last_name)
        full_name = string_one_space.join(name)        
    except:
        exception_message = sys.exc_info()[0]        
    return full_name, exception_message

def build_full_name5(first_name, middle_name, last_name):
    '''
    build person full time
    :param first_name: person first name
    :param middle_name: person middle name
    :param last_name: person last name
    :return person full name
    '''
    exception_message = None
    try:
        name = (first_name, middle_name, last_name)
        full_name = config.STRING_ONE_SPACE.join(name)        
    except:
        exception_message = sys.exc_info()[0]        
    return full_name, exception_message

def main():
#     constants
    string_one_space = " "
    STRING_ONE_SPACE = " "
    
#     first_name = "John"
#     middle_name = "B"
#     last_name = "Smith"
    
    first_name, middle_name, last_name= "John", "B", "Smith"

#     full_name = first_name + " " + middle_name + " " + last_name
#     print(full_name)
    
#     string_one_space = " "
#     name = (first_name, middle_name, last_name)
#     full_name = string_one_space.join(name)
#     print(full_name)
            
#     name = (first_name, middle_name, last_name)
#     full_name = STRING_ONE_SPACE.join(name)
#     print("Full Name: {}".format(full_name))
         
#     full_name = build_full_name3(first_name, middle_name, last_name)
#     print("Full Name: {}".format(full_name))
    
    full_name, exception_message = build_full_name5(first_name, middle_name, last_name)
    if exception_message is None:
        print("Full Name: {}".format(full_name))

if __name__ == '__main__':
    main()