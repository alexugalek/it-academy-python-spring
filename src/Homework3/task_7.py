def chocolate(n=1, m=1, k=1, t=1):
    """Cutting chocolate

    res1: Если число плиток в куске меньше чем т * n, то одним разломом можно
    отделить количество плиток или кратное m или количество плиток кратное n

    res2: От шоколадки m * n никогда всегда нельзя отделить m * n - 1 кусок,
    так как максимальное количество разломов при этом также будет m * n -1 и
    в остатке всегда будет 1 долька 1х1. Все оастальные варианты возможны за
    исключеним случаяб когда плитка 2х2. В этом случае также нельзя отделить
    только одну дольку 1х1, так как здесь в остатке также будет 2
    """
    res_1 = (k % n == 0 or k % m == 0) and k < n * m
    res_2 = False
    if k <= n * m:
        if not (k == 1 and n == m == 2) and k != n * m - 1:
            res_2 = True
    print(res_1, res_2)
