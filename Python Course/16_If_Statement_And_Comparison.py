def max(num1,num2,num3):
    if num1>num2 and num1>num3:
        print('Maximum Number : ', num1)
    elif num2>num1 and num2>num3:
        print('Maximum Number : ', num2)
    else:
        print('Maximum Number : ', num3)
    
max(5,6,8)