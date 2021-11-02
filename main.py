from sympy import isprime
from math import gcd
import eel

eel.init('web')


def ru_dict():
    a = ord('а')
    b = {}
    a = ' '.join([chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)]).split(' ')
    t = 0
    for c in a:
        t += 1
        b[t] = c
    return b


@eel.expose
def q_eval(q):
    q = q.replace(' ', '')
    a = ru_dict()
    k = 0

    for i in q.lower():
        for j in a.items():
            if j[1] == i:
                k += j[0]
                break

    if k >= 1000:
        while k >= 1000:
            k -= 1000

    c, v = k, k
    if not isprime(k):
        while True:
            if not isprime(c):
                c += 1
            else:
                return c
            if not isprime(v):
                v -= 1
            else:
                return v
    else:
        return k


@eel.expose
def p_eval(p):
    p = int(p)
    b = {}
    r = [i for i in range(101, 998) if isprime(i) is True][::-1]
    h, k1 = 1, 0

    for e in r:

        if h == 144:
            break

        if k1 == 10:
            b[h] = e
            h -= 129
            k1 = 0
            continue

        b[h] = e
        h += 13
        k1 += 1

    return 83 #int(b[p])


@eel.expose
def e_check(q, p, e):
    e = int(e)
    q = q_eval(q)
    p = p_eval(p)
    phi_n = (p - 1) * (q - 1)

    if (gcd(e, phi_n) == 1) and (1 < e) and (e < phi_n):
        return True
    else:
        return False


eel.start('main.html', size=(1180, 732))
