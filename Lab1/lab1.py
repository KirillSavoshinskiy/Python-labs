import collections
import sys
import argparse
import random
import os


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--quick_sort', nargs='?')
    parser.add_argument('--merge_sort', nargs='?')
    parser.add_argument('--word_count', nargs='?')
    parser.add_argument('--fib', nargs='?', type=int)
    return parser


def word_stat(data, n):
    c = collections.Counter(data.split())
    print(f'Statistics: {c}')
    print(f'Most common words:{c.most_common(n)}')


def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        middle = int(len(array) / 2)
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def quick_sort(array):#убрать доп массивы
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[random.randint(0, len(array) - 1)]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return array


def fib_generator(n):
    if n == 0:
        quit()
    fib1 = fib2 = 1
    while fib1 < n:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


def control():
    if __name__ == '__main__':
        parser = create_parser()
        namespace = parser.parse_args(sys.argv[1:])
        if namespace.word_count:
            if os.path.exists(namespace.word_count):
                with open(namespace.word_count, 'r') as file_handler:
                    data = file_handler.read()
                word_stat(data, 10)
        elif namespace.quick_sort:
            if os.path.exists(namespace.quick_sort):
                with open(namespace.quick_sort, 'r') as file_handler:
                    data = file_handler.read()
                    array = [int(x) for x in data.split()]
                print(quick_sort(array))
        elif namespace.merge_sort:
            if os.path.exists(namespace.merge_sort):
                with open(namespace.merge_sort, 'r') as file_handler:
                    data = file_handler.read()
                    array = [int(x) for x in data.split()]
                print(merge_sort(array))
        elif namespace.fib:
            for i in fib_generator(namespace.fib):
                print(i)


def main():
    control()


main()
