num1=input("Enter input one: ")
num2=input("Enter input two: ")
def division(num1, num2):
    try:
        result=(num1/num2)
        print(result)
    except:
        print('num2 cannot be zero')
        
division(num1, num2)