"""
a*u + b*v = gcd(a,b)

Enter your values for a and b below!

Reuqires that a and b are positive integers and a > b

"""

a = UwU
b = OwO

"""
Uses the Euclidean algorithm to compute the 
gcd of a and b. That is, gcd(a, b) == gcd(b, r)
where a = q * b - r.
"""

def gcd(a, b):
    # Uncomment the line below to show working out:
    # print(str(a) + " = " + str(b) + " * " + str(a // b) + " + " + str(a % b))
    if a % b == 0:
        return b
    return gcd(b, a % b)

def gcdDict(a, b, d):
    if a % b == 0:
        return d
    # Uncomment the line below to show working out:
    # print(str(a % b) + " = " + str(a) + " - " + str(b) + " * " + str(a // b))
    d[a % b] = [[1, a], [- (a // b), b]]

    return gcdDict(b, a % b, d)
    

"""
Takes a dict input [[a, b], [c, d]]
and returns a stringified version,
(a * b) + (c * d)
"""
def stringify(x):
    return "(" + str(x[0][0]) + " * " + str(x[0][1]) + ")" \
                + " + (" + str(x[1][0]) + " * " + str(x[1][1]) +")"
   
"""
Computes the values for u and v in
a*u + b*v = gcd(a,b). 
"""
def unwind(d, a, b):
    g = gcd(a, b)
    cur = d.get(gcd(a, b))

    # Uncomment the line below to show working out:
    # print(stringify(cur) + " = " + str(g))
    
    while cur[0][1] != a:
        sub = d.get(cur[1][1]) 

        # Uncomment the lines below to show working out:
        # print("(" + str(cur[0][0]) + " * " + str(cur[0][1]) + ") + " + \
        #       "(" + str(cur[1][0]) + " * " + "(" + stringify(sub) + ")" + ")" + \
        #      " = " + str(g))
        # print("(" + str(cur[0][0]) + " * " + str(cur[0][1]) + ") + " + \
        #       "(" + "(" + str(cur[1][0] * sub[0][0]) + " * " + str(sub[0][1]) + ")" + " + "\
        #          + "(" + str(cur[1][0] * sub[1][0]) + " * " + str(sub[1][1]) + ")" + ")" + \
        #      " = " + str(g))
        
        # print("(" + str(cur[1][0] * sub[0][0]) + " * " + str(sub[0][1]) + ") + " + \
        #       "(" + str(cur[0][0] + cur[1][0] * sub[1][0]) + " * " + str(sub[1][1]) + ")" + \
        #         " = " + str(g))
        
        new_cur = [[cur[1][0] * sub[0][0], sub[0][1]],\
                    [cur[0][0] + cur[1][0] * sub[1][0], sub[1][1]]]
        cur = new_cur
    
    print("gcd(" + str(a) + ", " + str(b) + ") = " + str(g))
    print("(" + str(a) + " * " + str(cur[0][0]) + ") + " + \
          "(" + str(b) + " * " + str(cur[1][0]) + ")" + \
          " = " + str(g))
    return

unwind(gcdDict(a, b, {}), a, b)
