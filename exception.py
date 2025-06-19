try:
    result=1/2
    a=b
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex1:
    print(ex1)
    print('Main exception got here')
    
