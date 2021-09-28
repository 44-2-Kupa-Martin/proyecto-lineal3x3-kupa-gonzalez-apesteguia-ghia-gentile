#index.py
import sys
x= lambda a: float(a)
multiples= False

def inputHandler(str):
    try:
        if (str.find(',')== -1):
            return tuple(map(x, str.split(' ')))
        else:
            return tuple(map(x, str.replace(' ', '').split(',')))
    except:
        sys.exit('Invalid inputs')

e1 = inputHandler(input('Enter the 1st equation\n(e.g 1,2,3)\n'))
e2 = inputHandler(input('Enter the 2st equation\n'))
e3 = inputHandler(input('Enter the 3st equation\n'))


if((e1[1]*e3[0]-e1[0]*e3[1])*(e1[2]*e2[0]-e1[0]*e2[2])-(e1[1]*e2[0]-e1[0]*e2[1])*(e1[2]*e3[0]-e1[0]*e3[2]) == 0):
    if(e1[0] / e2[0] == e1[1] / e2[1] == e1[2] / e2[2]):
        print('The 1st and the 2nd equation are multiples')
        multiples= True
    if(e2[0] / e3[0] == e2[1] / e3[1] == e2[2] / e3[2]):
        print('The 2nd and the 3rd equation are multiples')
        multiples= True
    if(e1[0] / e3[0] == e1[1] / e3[1] == e1[2] / e3[2]):
        print('The 1st and the 3rd equation are multiples')
        multiples= True
    if (not multiples):
        print('The equations are linearly dependent')
