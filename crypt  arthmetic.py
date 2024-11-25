from itertools import permutations

def solve_cryptarithm():
    for perm in permutations(range(10), 4):
        s, e, n, d = perm
        if s != 0:
            send = 1000 * s + 100 * e + 10 * n + d
            more = 1000 + 100 * e + 10 * n + d
            money = send + more
            if money == 10000 + 100 * e + 10 * n + y:
                print(f"SEND: {send}, MORE: {more}, MONEY: {money}")
                return

solve_cryptarithm()
