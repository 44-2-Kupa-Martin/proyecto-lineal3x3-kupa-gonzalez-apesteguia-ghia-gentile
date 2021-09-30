#   index.py
import sys
#Function declarations
def menu():
    print('What do you want to do?\n\t1- Solve a system\n\t2- Exit')
    try:
        a= int(input())
    except:
        sys.exit('Invalid input')
    if (a== 1):
        typeChecker(inputHandler(input('Enter the 1st equation\n(e.g 1,2,3)\n')), inputHandler(input('Enter the 2st equation\n')), inputHandler(input('Enter the 3st equation\n')))
        return
    elif (a == 2):
        sys.exit()
    else:
        sys.exit('Invalid input')
    

def inputHandler(str):
    x= lambda a: float(a)
    try:
        if (str.find(',')== -1):
            return tuple(map(x, str.split(' ')))
        else:
            return tuple(map(x, str.replace(' ', '').split(',')))
    except:
        sys.exit('Invalid inputs')

def typeChecker(e1, e2, e3):
    global isolatedZ
    isolatedZ= (e1[1]*e3[0]-e1[0]*e3[1])*(e1[2]*e2[0]-e1[0]*e2[2])-(e1[1]*e2[0]-e1[0]*e2[1])*(e1[2]*e3[0]-e1[0]*e3[2])
    equalTo= 1#some formula
    #undetermined check
    if (isolatedZ == 0):
        #inconsistent check
        if (equalTo != 0):
            inconsistentHandler(e1, e2, e3)
            return
        multiples= False
        if (e1[0] / e2[0] == e1[1] / e2[1] == e1[2] / e2[2]):
            print('The 1st and the 2nd equation are multiples')
            multiples= True
        if (e2[0] / e3[0] == e2[1] / e3[1] == e2[2] / e3[2]):
            print('The 2nd and the 3rd equation are multiples')
            multiples= True
        if (e1[0] / e3[0] == e1[1] / e3[1] == e1[2] / e3[2]):
            print('The 1st and the 3rd equation are multiples')
            multiples= True
        if (not multiples):
            print('The equations are linearly dependent')
        else:
            undeterminedHandler(e1, e2, e3)
        return
    else:
        determinedHandler(e1, e2, e3)
        return

def determinedHandler(e1, e2, e3):
    return

def undeterminedHandler(e1, e2, e3):
    return

def inconsistentHandler(e1, e2, e3):
    print('The system is inconsistent')
    menu()
    return

#code
print('Welcome to the 3x3 linear equation solver, made by Kupa; Gonzalez, Ghia, Apesteguia and Gentile')
menu()
#System type checks

