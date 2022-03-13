num=[20,40,60]
try:
    print(num[2])
except IndexError  as ie:
    print(ie)
else:
    print('no error')
finally:
    print('always executed')
