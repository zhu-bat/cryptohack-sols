# https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm

a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768

p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161


"""
Assumptuions:
- a is a quadratic residue
"""


# Step 1: Find Q and S such that p − 1 = Q*2^S such that Q is odd

def get_s(x, cur):
    if x % 2 == 1:
        return cur
    return get_s(x//2, cur+1)

def get_q(x, s):
    return x // (2**s)

def get_q_s(p):
    s = get_s(p-1, 0)
    q = get_q(p-1, s)
    # print(f"{p} - 1 = {q} * 2 ^ {s}")
    return (q, s)    

def legendre_symbol(a, p):
    symbol = pow(a, (p - 1) // 2, p)
    if symbol == 1:
        return 1
    elif symbol - p == -1:
        return -1
    elif symbol == 0:
        return 0
    else:
        return None
    

# Step 2: Find some quadratic non-residue z
def get_z(p):
    for i in range(p):
        if legendre_symbol(i, p) == -1:
            return i



# Steps 3 and 4: Set variables and loop

# Returns the smallest i such that t^(2^i) == 1
def get_i(t, m, p):
    for i in range(1, m):
        if pow(t, pow(2, i), p) == 1:
            return i
   
def tonelli_shanks(m, c, t, r, p):
    # print(f"m = {m}")
    # print(f"c = {c}")
    # print(f"t = {t}")
    # print(f"r = {r}")
    if t == 0:
        return 0
    elif t == 1:
        return r

    i = get_i(t, m, p)
    # print(f"i = {i}")
    b = pow(c, 2 ** (m - i - 1), p) 
    # print(f"b = {b}")
    m = i
    c = pow(b, 2, p)
    t = (t * pow(b, 2)) % p
    r = (r * b) % p
    return tonelli_shanks(m, c, t, r, p)
    

    
def get_solution(n, p):
    q_s = get_q_s(p)
    q = q_s[0]
    # print(f"q = {q}")
    s = q_s[1]
    # print(f"s = {s}")
    m = s
    z = get_z(p)
    # print(f"z = {z}")
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1)//2, p)
    return tonelli_shanks(m, c, t, r, p)


def get_roots(n, p):
    r = get_solution(n, p)
    roots = (r, (-r) % p)
    return roots


# The flag is the smaller of the two roots.
print(min(get_roots(a, p)))

