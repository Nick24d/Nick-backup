def main():
    #get input for mass
    mass = int(input("what is the mass value? : "))
    c = 300000000
    n = mass * square(c)
    print(f"{n}")

def square(n):
    return n*n
main ()