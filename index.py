#   index.py
import sys
from determined_handler import determined_handler
from undetermined_handler import undetermined_handler
#Function declarations
def menu():
    print('What do you want to do?\n\t1- Solve a system\n\t2- Exit')
    try:
        a= int(input())
    except ValueError:
        sys.exit('Invalid input')
    if (a== 1):
        global input_matrix
        input_matrix= [input_handler(input('Enter the 1st equation\n(e.g 1, 2, 3, 26)\n')), input_handler(input('Enter the 2st equation\n')), input_handler(input('Enter the 3st equation\n'))]
        type_checker(input_matrix)
        return
    elif (a == 2):
        sys.exit()
    else:
        sys.exit('Invalid input')
    

def input_handler(str):
    x= lambda a: float(a)
    try:
        if (str.find(',')== -1):
            equation= list(map(x, str.split(' ')))
            if (len(equation) != 4):
                sys.exit('Invalid inputs')
            return equation
        else:
            equation= list(map(x, str.replace(' ', '').split(',')))
            if (len(equation) != 4):
                sys.exit('Invalid inputs')
            return equation
    except ValueError:
        sys.exit('Invalid inputs')

def type_checker(M):
    e1_e2_constants_multiples, e2_e3_constants_multiples, e3_e1_constants_multiples, e1_e2_results_multiples, e2_e3_results_multiples, e3_e1_results_multiples= multiples_identifier(M)
    #remove equations that are multiples
    if (e1_e2_constants_multiples):
        print('The 1st and the 2nd equation are multiples')
        if (not e1_e2_results_multiples):
            inconsistent_handler(M)
            return
        else:
            M[0]= None
    if (e2_e3_constants_multiples):
        print('The 2nd and the 3rd equation are multiples')
        if (not e2_e3_results_multiples):
            inconsistent_handler(M)
            return
        else:
            M[1]= None
    if (e3_e1_constants_multiples):
        print('The 1st and the 3rd equation are multiples')
        if (not e3_e1_results_multiples):
            inconsistent_handler(M)
            return
        else:
            M[2]= None
    done= False
    while not done:
        try:
            M.remove(None)
        except ValueError:
            done= True
    if (not M):
        print("All equations of the system are multiples, such systems cannot be calculated.")
        return
    result= reduced_row_echelon_form(M)
    print(result)
    try:
        if (result[2][2]==1):
            determined_handler(result)
            return
        if (result[2][3]!=0):
            inconsistent_handler()
            return
    except IndexError:
        pass
    undetermined_handler(result)
    return



def multiples_identifier(M):
    check= [['M[0][0] / M[1][0]', 'M[0][1] / M[1][1]', 'M[0][2] / M[1][2]'],['M[1][0] / M[2][0]', 'M[1][1] / M[2][1]', 'M[1][2] / M[2][2]'],['M[2][0] / M[0][0]', 'M[2][1] / M[0][1]', 'M[2][2] / M[0][2]']]
    #assume there are no multiples
    e1_e2_constants_multiples= False
    e2_e3_constants_multiples= False
    e3_e1_constants_multiples= False
    #and initialize vars for future use
    e1_e2_results_multiples= None
    e2_e3_results_multiples= None
    e3_e1_results_multiples= None
    #test if system's constants are suitable for division
    for i in range(3):
        #checks for M[1]
        if (check[0] and M[1][i]==0):
            if (M[0][i]==0):
                check[0][i]= ''
            else:
                check[0]= False
        #checks for M[2]
        if (check[1] and M[2][i]==0):
            if (M[1][i]==0):
                check[1][i]= ''
            else:
                check[1]= False
        #checks for M[0]
        if (check[2] and M[0][i]==0):
            if (M[2][i]==0):
                check[2][i]= ''
            else:
                check[2]= False
    #handle system's results that are zero
    if (M[1][3]==0):
        if (M[0][3]==0):
            e1_e2_results_multiples= True
        else:
            e1_e2_results_multiples= False
    if (M[2][3]==0):
        if (M[1][3]==0):
            e2_e3_results_multiples= True
        else:
            e2_e3_results_multiples= False
    if (M[0][3]==0):
        if (M[2][3]==0):
            e3_e1_results_multiples= True
        else:
            e3_e1_results_multiples= False
    #statement constructor
    if (check[0]):
        #remove falsy entries
        done= False
        while not done:
            try:
                check[0].remove('')
            except ValueError:
                done= True
        #construct condition for system's constants
        check0_length= len(check[0])
        if (check0_length == 1 or check0_length == 0):
            e1_e2_constants_multiples= True
        elif (check0_length == 2):
            e1_e2_constants_multiples= eval(f'{check[0][0]} == {check[0][1]}')
        elif (check0_length == 3):
            e1_e2_constants_multiples= eval(f'{check[0][0]} == {check[0][1]} == {check[0][2]}')
        #construct condition for system's results
        if (e1_e2_results_multiples == None):
            if (check0_length == 0):
                e1_e2_results_multiples= False
            else:
                e1_e2_results_multiples= eval(f'{check[0][0]} == M[0][3]/M[1][3]')
    if (check[1]):
        #remove falsy entries
        done= False
        while not done:
            try:
                check[1].remove('')
            except ValueError:
                done= True
        #construct condition for system's constants
        check1_length= len(check[1])
        if (check1_length == 1 or check1_length == 0):
            e2_e3_constants_multiples= True    
        elif (check1_length == 2):
            e2_e3_constants_multiples= eval(f'{check[1][0]} == {check[1][1]}')
        elif (check1_length == 3):
            e2_e3_constants_multiples= eval(f'{check[1][0]} == {check[1][1]} == {check[1][2]}')
        #construct condition for system's results
        if (e2_e3_results_multiples == None):
            if (check1_length == 0):
                e2_e3_results_multiples= False
            else:
                e2_e3_results_multiples= eval(f'{check[1][0]} == M[1][3]/M[2][3]')
    if (check[2]):
        #remove falsy entries
        done= False
        while not done:
            try:
                check[2].remove('')
            except ValueError:
                done= True
        #construct condition for system's constants
        check2_length= len(check[2])
        if (check2_length == 1 or check2_length == 0):
            e3_e1_constants_multiples= True    
        elif (check2_length == 2):
            e3_e1_constants_multiples= eval(f'{check[2][0]} == {check[2][1]}')
        elif (check2_length == 3):
            e3_e1_constants_multiples= eval(f'{check[2][0]} == {check[2][1]} == {check[2][2]}')
        #construct condition for system's results
        if (e3_e1_results_multiples == None):
            if (check2_length == 0):
                e3_e1_results_multiples= False
            else:
                e3_e1_results_multiples= eval(f'{check[2][0]} == M[2][3]/M[0][3]')
    
    return [e1_e2_constants_multiples, e2_e3_constants_multiples, e3_e1_constants_multiples, e1_e2_results_multiples, e2_e3_results_multiples, e3_e1_results_multiples]

#The following function belongs to rosetta code: 
# https://rosettacode.org/wiki/Reduced_row_echelon_form#Python
def reduced_row_echelon_form(M):
    lead = 0
    row_count = len(M)
    column_count = len(M[0])
    for r in range(row_count):
        if lead >= column_count:
            return None
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == row_count:
                i = r
                lead += 1
                if column_count == lead:
                    return None
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        M[r] = [ mrx / float(lv) for mrx in M[r]]
        for i in range(row_count):
            if i != r:
                lv = M[i][lead]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1
    return M

def inconsistent_handler():
    global exit_program
    print('The system is inconsistent')
    exit_program= True
    return

#code
print('Welcome to the 3x3 linear equation solver, made by Kupa; Gonzalez, Ghia, Apesteguia and Gentile')
exit_program= False
while not exit_program:
    menu()
