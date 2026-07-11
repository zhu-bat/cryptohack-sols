
"""
If x is a quadratic residue in the finite field F^*_p, 
print its roots a, where a^2 = x mod p.

Otherwise, print "Quadratic Non-Residue".

Preconditions: 
- x < p

"""
def find_roots(x, p):
    roots = []
    for i in range(p):
        if i**2 % p == x:
            roots.append(i)

    if roots:
        print(roots)
    else:
        print("Quadratic Non-Residue")      


find_roots(14, 29)

find_roots(6, 29)      

find_roots(11, 29)            
