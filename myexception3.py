d={'stuid':101,'stuname':'indhuja'}
try:
    print(d['course'])
except KeyError as ke:
    print(ke)
else:
    print('no error')
