# try:
    
#     number = int(input("Please Enter A Number : "))
#     print(number)
    
# except:
#     print('Please Enter A Valid Number')

try:
    
    c = 8/0
    
except ZeroDivisionError as err:
    print('Zero Division Error')