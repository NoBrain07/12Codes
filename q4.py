# 4	Write a Python function to remove characters that appear more than k times in a string accepted from the user.


def remove_k(strg, k):
    n, z = dict([(x, strg.count(x)) for x in strg]), ""
    for i in strg:
        if not n[i] >= k:
            z += i
        else:
            continue
    print(z)


remove_k(input("=>"), int(input("k=>")))
