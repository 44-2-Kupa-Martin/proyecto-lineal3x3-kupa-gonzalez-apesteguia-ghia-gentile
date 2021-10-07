#   undetermined_handler.py
def undetermined_handler(M):
    for x in M :
        for number in x:
            number = round(number,3)


    print(f"S: x=λ\n   y=({M[1][3]}-{M[1][2]}·(({M[0][3]}-{M[0][0]}·λ)/{M[0][2]}))/{M[1][1]}\n   z=({M[0][3]}-{M[0][0]}·λ)/{M[0][2]}")
    
    λ = int()

    print("Quiere ponerle un valor a lambda?\n\t1- si!\n\t2- No")
    try: 
        a= int(input())
    except ValueError:
        sys.exit('Invalid input')
    print("ingrese un valor")
    if (a == 1):
        λ = (input())
        print(f"S: x={λ}\n   y=({M[1][3]}-{M[1][2]}·(({M[0][3]}-{M[0][0]}·{λ})/{M[0][2]}))/{M[1][1]}\n   z=({M[0][3]}-{M[0][0]}·{λ})/{M[0][2]}")
    if (a == 2):
        sys.exit('input invalido')

    return