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
        type_checker(input_handler(input('Enter the 1st equation\n(e.g 1, 2, 3)\n')), input_handler(input('Enter the 2st equation\n')), input_handler(input('Enter the 3st equation\n')))
        return
    elif (a == 2):
        sys.exit()
    else:
        sys.exit('Invalid input')
    

def input_handler(str):
    x= lambda a: float(a)
    try:
        if (str.find(',')== -1):
            return tuple(map(x, str.split(' ')))
        else:
            return tuple(map(x, str.replace(' ', '').split(',')))
    except:
        sys.exit('Invalid inputs')

def type_checker(e1, e2, e3):
    global isolated_z
    isolated_z= (e1[1]*e3[0]-e1[0]*e3[1])*(e1[2]*e2[0]-e1[0]*e2[2])-(e1[1]*e2[0]-e1[0]*e2[1])*(e1[2]*e3[0]-e1[0]*e3[2])
    print(isolated_z)
    equal_to= 0#some formula
    
    #undetermined check
    if (isolated_z == 0):
        #inconsistent check
        if (equal_to != 0):
            inconsistent_handler(e1, e2, e3)
            return
        e1_e2_statement, e2_e3_statement, e1_e3_statement= prevent_div_by_zero(e1, e2, e3)
        multiples= False
        if (e1_e2_statement):
            print('The 1st and the 2nd equation are multiples')
            multiples= True
        if (e2_e3_statement):
            print('The 2nd and the 3rd equation are multiples')
            multiples= True
        if (e1_e3_statement):
            print('The 1st and the 3rd equation are multiples')
            multiples= True
        if (not multiples):
            print('The equations are linearly dependent')
        else:
            undetermined_handler(e1, e2, e3)
            return
    else:
        determined_handler(e1, e2, e3)
        return


def prevent_div_by_zero(e1, e2, e3):
    check= [['e1[0] / e2[0]', 'e1[1] / e2[1]', 'e1[2] / e2[2]'],['e2[0] / e3[0]', 'e2[1] / e3[1]', 'e2[2] / e3[2]'],['e1[0] / e3[0]', 'e1[1] / e3[1]', 'e1[2] / e3[2]']]
    #assume there are no multiples
    e1_e2_statement= False
    e2_e3_statement= False
    e1_e3_statement= False
    #test if values are suitable for division
    for i in range(3):
        #checks for e2[]
        if (e2[i]==0):
            if (e1[i]==0):
                check[0][i]= ''
            else:
                check[0]= False
        #checks for e3[]
        if (e3[i]==0):
            if (e2[i]==0):
                check[1][i]= ''
            else:
                check[1]= False
            if (e1[i]==0):
                check[2][i]= ''
            else:
                check[2]= False

    #statement constructor
    if (check[0]):
        #remove falsy entries
        done= False
        for i in range(3):
            if (not done):
                try:
                    check[0].remove('')
                except:
                    done= True
        #construct condition
        check0_length= len(check[0])
        if (check0_length == 1):
            e1_e2_statement= True    
        elif (check0_length == 2):
            e1_e2_statement= eval(f'{check[0][0]} == {check[0][1]}')
        elif (check0_length == 3):
            e1_e2_statement= eval(f'{check[0][0]} == {check[0][1]} == {check[0][2]}')
    if (check[1]):
        #remove falsy entries
        done= False
        for i in range(3):
            if (not done):
                try:
                    check[1].remove('')
                except:
                    done= True
        #construct condition
        check1_length= len(check[1])
        if (check1_length == 1):
            e2_e3_statement= True    
        elif (check1_length == 2):
            e2_e3_statement= eval(f'{check[1][0]} == {check[1][1]}')
        elif (check1_length == 3):
            e2_e3_statement= eval(f'{check[1][0]} == {check[1][1]} == {check[1][2]}')
    if (check[2]):
        #remove falsy entries
        done= False
        for i in range(3):
            if (not done):
                try:
                    check[2].remove('')
                except:
                    done= True
        #construct condition
        check2_length= len(check[2])
        if (check2_length == 1):
            e1_e3_statement= True    
        elif (check2_length == 2):
            e1_e3_statement= eval(f'{check[2][0]} == {check[2][1]}')
        elif (check2_length == 3):
            e1_e3_statement= eval(f'{check[2][0]} == {check[2][1]} == {check[2][2]}')
    return [e1_e2_statement, e2_e3_statement, e1_e3_statement]


def determined_handler(e1, e2, e3):
    return

def undetermined_handler(e1, e2, e3):
    return

def inconsistent_handler(e1, e2, e3):
    print('The system is inconsistent')
    menu()
    return

#code
print('Welcome to the 3x3 linear equation solver, made by Kupa; Gonzalez, Ghia, Apesteguia and Gentile')
menu()
#System type checks

