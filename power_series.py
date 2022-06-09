from random import randint

n = int(input('введите модуль n: '))


def power_mod(x, pow, mod):
    res = 1
    pow_res = 0
    while pow_res < pow:
        pow_res_1 = 2
        res1 = x
        while pow_res + pow_res_1 <= pow:
            res1 = (res1 * res1) % mod
            pow_res_1 *= 2
        pow_res_1 //= 2
        res = (res * res1) % mod
        pow_res += pow_res_1
    return res % mod


def factor(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans


def div(n):
    numb = n
    t = []
    for i in range(numb - 1, 1, -1):
        if numb % i == 0:
            t.append(i)
    return t


def direct_product_of_groups(x):
    k = 1
    t = []
    res = []
    while True:
        t.append(f'\n{x} ^ {k} (mod{n}) = {power_mod(x, k, n)}')
        res.append(power_mod(x, k, n))
        if power_mod(x, k, n) == 1:
            break
        k += 1
    return t, res


def step_posled(d):
    digit = 0
    fac = 0
    for i in range(10000):
        rnd = randint(1, len(d) - 1)
        digit = int(d[rnd][0])
        fac = int(d[rnd][2])
        k = 0
        if fac > 50:  # костыль для проверки степени: если < 50, то берем следующую
            for j in d.values():
                if j[0] == digit:
                    k += 1
            if k == 1:
                break
    return fac, digit


def group(d):
    digit = step_posled(d)[1]
    fac = step_posled(d)[0]
    gb = []  # циклическая группа
    for i in range(fac):  # степень
        gb.append(power_mod(digit, i, n))  # число, степень, модуль

    g = []
    for i in gb:
        if i not in g:
            g.append(i)
    return g, digit, fac


def adj_classes(resultat, h):
    buf = []
    buf.extend(h)
    flag = False
    k = 0
    dict_factor = {}
    g_classes = []
    for i in range(1, 100):
        r = []
        if flag is not True:
            for j in h:
                try:
                    if resultat[resultat.index(j) + i] in buf:
                        flag = True
                        break
                    r.append(resultat[resultat.index(j) + i])
                    buf.append(resultat[resultat.index(j) + i])
                except IndexError:
                    r.append(resultat[i - 1])
                    break
            if len(r) > 0:
                k = i
                dict_factor[i] = r
                g_classes.append(f'\nG{i} = {r}')
    buf.clear()
    return g_classes, dict_factor, k


def factor_gruppa(k):
    f_g = ['X']
    for i in range(1, k + 1):
        f_g.append(f'G{i}')
    f_g.append('H')

    print(*f_g)

    b = []
    for i in range(1, k + 1):
        f_g.remove(f_g[0])
        f_g.append(f'G{i}')
        print(*f_g)

    f_g.remove(f_g[0])
    f_g.append('H')
    print(*f_g, '\n')

    return ''


def h_eval(mas_div, g):
    try:
        h = g[int(mas_div[-1]) - 1::mas_div[-1]]  # последняя получившаяся подгруппа
        if len(h) <= 2:  # если в подгруппе <= 2 чисел, то берем предыдущий
            h = g[int(mas_div[-2]) - 1::mas_div[-2]]
    except IndexError:
        h = g
    return h


def main1():
    d = {'№': ('число', 'степень', 'модуль', 'разложение степени на множители')}  # степенная последовательность
    k = 0  # ключ для словаря
    for x in range(2, 100000):
        for z in range(2, 15):
            if power_mod(x, z, n) == 1:  # число, степень, модуль
                k += 1
                d[k] = x, n, z, factor(z)
            if len(d) == 21:
                break
        if len(d) == 21:
            break

    digit = 0
    fac = 0
    for i in range(10000):
        rnd = randint(1, len(d) - 1)
        digit = int(d[rnd][0])
        fac = int(d[rnd][2])
        k = 0
        if fac > 50:  # костыль для проверки степени: если < 50, то берем следующую
            for j in d.values():
                if j[0] == digit:
                    k += 1
            if k == 1:
                break

    gb = []  # циклическая группа
    for i in range(fac):  # степень
        gb.append(power_mod(digit, i, n))  # число, степень, модуль

    g = []
    for i in gb:
        if i not in g:
            g.append(i)

    buf = group(d)
    g = buf[0]
    digit = buf[1]
    fac = buf[2]
    while len(g) < 7:
        buf = group(d)
        g = buf[0]
        digit = buf[1]
        fac = buf[2]

    g = g[1:]  # циклическая группа: передвигаем единицу из начала списка в конец
    g.append(1)
    order_g = fac  # порядок группы
    mas_div = div(order_g)[::-1]  # массив делителей

    g_new = []
    for i in g:
        if i not in g_new:
            g_new.append(i)
    g = g_new

    h = h_eval(mas_div, g)

    a_c = adj_classes(g, h)
    g_classes = a_c[0]
    dict_factor = a_c[1]
    k = a_c[2]

    return dict_factor, h, k, d, digit, g, mas_div, g_classes


def check(rnd1, rnd2, res):
    if res > k:
        res = res - k - 1
    if res == 0:
        out1 = f'Выполнили проверку. Для этого перемножили G{rnd1} и G{rnd2}. В результате должен получиться смежный класс H:'
        out2 = f'\nG{rnd1} = {dict_factor[rnd1]}\nG{rnd2} = {dict_factor[rnd2]}\nH = {h}'
    else:
        out1 = f'Выполнили проверку. Для этого перемножили G{rnd1} и G{rnd2}. В результате должен получиться смежный класс G{res}:'
        out2 = f'\nG{rnd1} = {dict_factor[rnd1]}\nG{rnd2} = {dict_factor[rnd2]}\nG{res} = {dict_factor[res]}'

    bufr = []
    out3 = []
    for i, j in zip(dict_factor[rnd1], dict_factor[rnd2]):
        result = ((i - n) * (j - n)) % n
        bufr.append(result)
        out3.append(f'\n{i} * {j} (mod{n}) = {result}')

    fl = False
    if res != 0:
        if sorted(bufr) == sorted(dict_factor[res]):
            fl = True
            out4 = '\nПроверка выполнена успешно\n'
            return out1, out2, out3, out4, fl
        else:
            out4 = '\nПроверка не выполнена\n'
            return out1, out2, out3, out4, fl
    else:
        if sorted(bufr) == sorted(h):
            fl = True
            out4 = '\nПроверка выполнена успешно\n'
            return out1, out2, out3, out4, fl
        else:
            out4 = '\nПроверка не выполнена\n'
            return out1, out2, out3, out4, fl


while True:
    main = main1()
    dict_factor = main[0]
    h = main[1]
    k = main[2]
    d = main[3]
    digit = main[4]
    g = main[5]
    mas_div = main[6]
    g_classes = main[7]

    rnd1 = randint(1, k)  # фактор группа 1
    rnd2 = randint(1, k)  # фактор группа 2
    res = rnd1 + rnd2  # результат проверки
    ch = check(rnd1, rnd2, res)

    if ch[4]:
        print('Степенная последовательность')
        for key, value in d.items():
            print("{0}: {1}".format(key, value))

        print('Выбрали число: ', digit)
        print(f'{digit} (mod {n}) = 1; |G| = {len(g)}.')
        print('Получили циклическую группу: ', g)
        print('Порядок группы: ', len(set(g)))
        print('Массив делителей индекса: ', mas_div)
        print(f'Получили {len(mas_div)} подгруппы:')

        for i in mas_div:
            print(f'H{i} = {g[i - 1::i]}')

        print(f'Нашли смежные классы:\nH = {h}')
        print(*g_classes)
        print('Фактор-группа:')
        print(factor_gruppa(k))

        print(ch[0], ch[1], *ch[2], ch[3])
        break
    else:
        continue

print('Прямое произведение циклических групп:\n')
d2 = {}
t = []
for i in range(1, len(d)):
    d2[i] = int(d[i][0]), int(d[i][2])
bufr2 = []
for i in d2.values():
    if i[1] <= 9 and i[0] not in bufr2:
        t.append((i[0], i[1]))
        bufr2.append(i[0])
num1 = t[0]
num2 = t[1]

print(f'Для первой циклической группы взяли число x = {num1[0]}, z = {num1[1]}')
x = num1[0]
t1 = direct_product_of_groups(x)
print(*t1[0])
print(f'Первая циклическая группа:\nA = {t1[1]}\n')

print(f'Для второй циклической группы взяли число x = {num2[0]}, z = {num2[1]}')
x = num2[0]
t2 = direct_product_of_groups(x)
print(*t2[0])
print(f'Вторая циклическая группа:\nB = {t2[1]}\n')

print('Прямое произведение двух групп:')
prod_gr = ['A*B']
prod_gr.extend(t1[1])
buf_t = []
resultat = []
print(*prod_gr)

for i in range(len(t2[1])):
    buf_t = [t2[1][i]]
    for j in t1[1]:
        rt = ((t2[1][i] - n) * (j - n)) % n
        buf_t.append(rt)
        if rt not in resultat:
            resultat.append(rt)
    print(*buf_t)

print(f'\nПолучили результат:\nG = {resultat}')
order_res = len(resultat)
massiv_del = div(order_res)[::-1]
podgr = len(massiv_del)

h = h_eval(massiv_del, resultat)

for i in massiv_del:
    print(f'H{i} = {resultat[i - 1::i]}')


a_c1 = adj_classes(resultat, h)
g_classes = a_c1[0]
dict_factor = a_c1[1]
k = a_c1[2]

print(f'\nНашли смежные классы:\nH = {h}')
print(*g_classes)

print('\nФактор-группа:')
print(factor_gruppa(k))

rnd1 = randint(1, k)  # фактор группа 1
rnd2 = randint(1, k)  # фактор группа 2
res = rnd1 + rnd2  # результат проверки
ch = check(rnd1, rnd2, res)

print(ch[0], ch[1], *ch[2], ch[3])

print(f'Нахождение последовательности чисел\nВзяли число p = {digit}, модуль n = {n}, степень x = 2^1,2,…,k. '
      f'\nНайденная последовательность:')
x = 2
start = power_mod(digit, x, n)
lst = []
c = 0
print(f'x   s\n2 {start}')
while True:
    x *= 2
    current = power_mod(digit, x, n)
    print(x, current)
    if current in lst:
        break
    lst.append(current)
    c += 1
print(f'Последовательность чисел s = {lst}\nПовторяется через каждую {c} степень')
