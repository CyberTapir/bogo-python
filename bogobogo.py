import random
import argparse
count = 0
parser = argparse.ArgumentParser(description='Bogo Sort with verbose option')
parser.add_argument('-v', '--verbose', action='store_true', help='Print each pass of the array')
args = parser.parse_args()
def bogoSort(a):
    global count
    while not is_sorted(a):
        shuffle(a)
        count += 1
def bogobogoSort(a):
    global count
    while not is_sorted(a):
        r = []
        for value in a:
            r.append(value)
            bogoSort(r)
            if args.verbose:
                print(a)
        bogoSort(a)
        count += 1
def is_sorted(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True
def shuffle(a):
    n = len(a)
    for i in range(n):
        r = random.randint(0, n - 1)
        a[i], a[r] = a[r], a[i]
a = [3, 9, 2, 8, 4, 1, 6, 5, 7, 10]
bogobogoSort(a)
print(count)
