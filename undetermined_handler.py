#   undetermined_handler.py
def undetermined_handler(M):
    for x in M:
        for number in x:
            number = round(number,3)

    print(f"S: x=λ\n   y=({M[1][3]}-{M[1][2]}·(({M[0][3]}-{M[0][0]}·λ)/{M[0][2]}))/{M[1][1]}\n   z=({M[0][3]}-{M[0][0]}·λ)/{M[0][2]}")

    print("Quiere ponerle un valor a lambda?\n\t1- si!\n\t2- No")
    try: 
        a= int(input())
    except ValueError:
        sys.exit('Invalid input')
    print("ingrese un valor")
    if (a == 1):
        λ = float(input())
        cuenta_y=(M[1][3]-M[1][2]*((M[0][3]-M[0][0]*λ)/M[0][2]))/M[1][1]
        cuenta_z=(M[0][3]-M[0][0]*λ)/(M[0][2])
        print(f"S: x=λ\n    y={cuenta_y}\n    z={cuenta_z}")
    if (a == 2):
        return
