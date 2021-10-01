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

def preventDivByZero(e1, e2, e3):
    check= [['e1[0] / e2[0]', 'e1[1] / e2[1]', 'e1[2] / e2[2]'],['e2[0] / e3[0]', 'e2[1] / e3[1]', 'e2[2] / e3[2]'],['e1[0] / e3[0]', 'e1[1] / e3[1]', 'e1[2] / e3[2]']]
    e1e2Statement= None
    e2e3Statement= None
    e1e3Statement= None
    #test if values are suitable for division
    for index in range(3):
        #checks for e2[]
        if (e2[index]==0):
            if (e1[index]==0):
                check[0].pop(index)
            else:
                check[0]= False
        #checks for e3[]
        if (e3[index]==0):
            if (e2[index]==0):
                check[1].pop(index)
            else:
                check[1]= False
            if (e1[index]==0):
                check[2].pop(index)
            else:
                check[2]= False
    #statement constructor
    if (check[0]):
        check0Length= len(check[0])
        if (check0Length == 1):
            e1e2Statement= True    
        elif (check0Length == 2):
            e1e2Statement= eval(f'{check[0][0]} == {check[0][1]}')
        elif (check0Length == 3):
            e1e2Statement= eval(f'{check[0][0]} == {check[0][1]} == {check[0][2]}')
    if (check[1]):
        check1Length= len(check[1])
        if (check1Length == 1):
            e2e3Statement= True    
        elif (check1Length == 2):
            e2e3Statement= eval(f'{check[1][0]} == {check[1][1]}')
        elif (check1Length == 3):
            e2e3Statement= eval(f'{check[1][0]} == {check[1][1]} == {check[1][2]}')
    if (check[2]):
        check2Length= len(check[2])
        if (check2Length == 1):
            e1e3Statement= True    
        elif (check2Length == 2):
            e1e3Statement= eval(f'{check[2][0]} == {check[2][1]}')
        elif (check2Length == 3):
            e1e3Statement= eval(f'{check[2][0]} == {check[2][1]} == {check[2][2]}')
    return [e1e2Statement, e2e3Statement, e1e3Statement]

def typeChecker(e1, e2, e3):
    global isolatedZ
    isolatedZ= (e1[1]*e3[0]-e1[0]*e3[1])*(e1[2]*e2[0]-e1[0]*e2[2])-(e1[1]*e2[0]-e1[0]*e2[1])*(e1[2]*e3[0]-e1[0]*e3[2])
    print(isolatedZ)
    equalTo= 0#some formula
    
    #undetermined check
    if (isolatedZ == 0):
        #inconsistent check
        if (equalTo != 0):
            inconsistentHandler(e1, e2, e3)
            return
        e1e2Statement, e2e3Statement, e1e3Statement= preventDivByZero(e1, e2, e3)
        multiples= False
        if (e1e2Statement):
            print('The 1st and the 2nd equation are multiples')
            multiples= True
        if (e2e3Statement):
            print('The 2nd and the 3rd equation are multiples')
            multiples= True
        if (e1e3Statement):
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

