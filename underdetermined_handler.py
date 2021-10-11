#   underdetermined_handler.py
def underdetermined_handler(M):
    print('The system is underdetermined')
    #rounding the numbers of the matrix saving them in another array to then replace them in the ecuation
    rounded_M = []

    for arr in M:
        rounded_arr = []
        for number in arr:
            rounded_arr.append(round(number, 3))
        rounded_M.append(rounded_arr)
    #lambda function to correct the cases where a negative number stayed with 2 negative signs converting it in a positive number as it should be
    minus = lambda num: f"+{abs(num)}" if num < 0 or num==0 else f"-{abs(num)}"
    #printing the ecuation
    print(f"S: x=λ\n   y=({rounded_M[1][3]}{minus(rounded_M[1][2])}·(({rounded_M[0][3]}{minus(rounded_M[0][0])}·λ)/{rounded_M[0][2]}))/{rounded_M[1][1]}\n   z=({rounded_M[0][3]}{minus(rounded_M[0][0])}·λ)/{rounded_M[0][2]}")
    
    print("Quiere ponerle un valor a lambda?\n\t1- si\n\t2- No")
    try: 
        a= int(input())
    except ValueError:
        sys.exit('Invalid input')
    print("Ingrese un valor")
    if (a == 1):
        λ = float(input())
        #equations 
        cuenta_z=(M[0][3]-M[0][0]*λ)/(M[0][2])
        cuenta_y=(M[1][3]-M[1][2])*(cuenta_z)/M[1][1]

        print(f"S: x=λ\n    y={round(cuenta_y, 3)}\n    z={round(cuenta_z, 3)}")
    if (a == 2):
        return  
