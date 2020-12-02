def two_sum(target, l):
    remainders = set()
    for n in l:
        n = int(n)
        remainders.add(target - n)
        if n in remainders:
            return (target - n, n)
    return ()


def three_sum(target, l):
    targets = [target - x for x in l]
    for i, e in enumerate(targets):
        l_without_e = l[:i] + l[i+1:]
        a = two_sum(e, l_without_e)
        if len(a) > 0:
            return (a[0], a[1], target - e)


def main(target, input_filename):
    with open(input_filename) as f:
        l = [int(x) for x in f.read().splitlines()]

        a = two_sum(target, l)
        print(a)
        print(a[0] * a[1])

        b = three_sum(target, l)
        print(b)
        print(b[0] * b[1] * b[2])


if __name__ == '__main__':
    main(2020, 'input')