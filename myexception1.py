a,b=10,0
try:
    c=a//b  #5
    print(c)
except ArithmeticError as ae:
    print(ae)
else:
    print('no error')
finally:
    print('always executed')