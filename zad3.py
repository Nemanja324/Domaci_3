def najduzi_testerasti_podniz(niz):
    n = len(niz)

    dp = [1] * n

    prethodnik = [-1] * n

    for i in range(n):
        for j in range(i):
            if niz[j] > niz[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prethodnik[i] = j

    krajnji = 0
    for i in range(n):
        if dp[i] > dp[krajnji]:
            krajnji = i

    podniz = []
    while krajnji != -1:
        podniz.append(niz[krajnji])
        krajnji = prethodnik[krajnji]

    podniz.reverse()
    return podniz


niz = [1, 5, 3, 7, 2, 4, 6, 10]
podniz = najduzi_testerasti_podniz(niz)
print(f"Najduži testerasti podniz: {podniz}")
