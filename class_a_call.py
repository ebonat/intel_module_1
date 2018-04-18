

from class_a import ClassA

def main():
#     class method
    my_class_a = ClassA()     
    result = my_class_a.function_multiplication(2, 2)     
    print("The multiplication is {}".format(result))

#     static method - important for developerm generic libraries
    ClassA.show_message("Hello")

if __name__ == '__main__':
    main()