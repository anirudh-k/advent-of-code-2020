def main(target, input_filename):
    remainders = set()
    with open(input_filename) as f:
        for n in f:
            n = int(n)
            remainders.add(target - n)
            if n in remainders:
                return (target - n) *  n

            

if __name__ == '__main__':
    print(main(2020, 'input'))