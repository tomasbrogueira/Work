#! /usr/bin/env python3
''' search and sorting algorithms '''
from random import randint
from timeit import timeit

def run(algorithm, vec) :
    ''' run algorithm with given vector '''
    return timeit(f"{algorithm}({vec})",f"from __main__ import {algorithm}", number=1)

# from sorting import bubble
# timeit(f"{algorithm}({vec})",f"from __main__ import {algorithm}", number=1)

def array(length, upper=1000, lower=0) :
    ''' build a 'length' vector with random values between 'loewr' and 'upper' '''
    return [ randint(lower, upper) for i in range(length) ]

def binary(vec, low, high, value) :
    ''' binary search between indexes '''
    print(low, high)
    if high <= low :
        return None
    mid = low + (high - low) // 2
    if vec[mid] == value :
        return mid
    if vec[mid] > value :
        return binary(vec, low, mid-1, value)
    return binary(vec, mid+1, high, value)

def binary_search(vec, value) : # vec must be sorted
    ''' binary search '''
    return binary(vec, 0, len(vec), value) # return index or None

def sorted_search(vec, value) : # vec must be sorted
    ''' sorted search '''
    for pos, val in vec:
        if val == value :
            return pos
        if val > value :
            return None # give up
    return None

def search(vec, value) :
    ''' unsorted search '''
    for pos, val in vec :
        if val == value :
            return pos
    return None

def bubble0(vec) :
    ''' bubble sort (left to right) '''
    k = len(vec)
    for i in range(k) :
        for j in range(k - i - 1) : # left to right
            if vec[j] > vec[j+1] :
                vec[j], vec[j+1] = vec[j+1], vec[j]
        if __debug__:
            print(vec)
    return vec

def bubble1(vec) :
    ''' bubble sort (right to left) '''
    k = len(vec) - 1
    for i in range(k) :
        for j in range(k, i, -1) : # right to left
            if vec[j] < vec[j-1] :
                vec[j], vec[j-1] = vec[j-1], vec[j]
        if __debug__:
            print(vec)
    return vec

def bubble(vec) :
    ''' bubble sort (short-circuit) '''
    k = len(vec)
    for i in range(k) :
        is_sorted = True
        for j in range(k - i - 1) :
            if vec[j] > vec[j+1] :
                vec[j], vec[j+1] = vec[j+1], vec[j]
                is_sorted = False
        if is_sorted :
            break
        if __debug__:
            print(vec)
    return vec

def insertion(vec) :
    ''' insertion sort '''
    for i in range(1, len(vec)) :
        item = vec[i]
        j = i - 1
        while j >= 0 and vec[j] > item :
            vec[j + 1] = vec[j]
            j -= 1
        vec[j + 1] = item
        if __debug__:
            print(vec)
    return vec

# selection([15,14,12,24,18,11,21,48,32])
def selection(vec) :
    ''' selection sort '''
    for i, val in enumerate(vec) :
        pos = i
        for j in range(i+1, len(vec)) :
            if vec[pos] > vec[j] :
                pos = j
        vec[pos], vec[i] = val, vec[pos]
        if __debug__:
            print(vec)
    return vec

def partition(vec, low, high) :
    ''' partition for quick sort '''
    i, j, pivot = low, high -1, vec[high]
    while i <= j :
        while vec[i] <= pivot and i <= j :
            i += 1
        while pivot <= vec[j] and j >= i :
            j -= 1
        if i < j :
            vec[i], vec[j] = vec[j], vec[i]
    vec[i], vec[high] = vec[high], vec[i]
    return i

def quick(vec, low=0, high=None) :
    ''' quick sort '''
    if high is None :
        high = len(vec) -1
    if high <= low :
        return vec
    # if high-low <= M : return insertion(a, low, high)
    i = partition(vec, low, high)
    quick(vec, low, i-1)
    quick(vec, i+1, high)
    return vec

def merge_sorted(vec1, vec2) :
    ''' merge sorted vectors for merge sort '''
    if len(vec1) == 0 :
        return vec2
    if len(vec2) == 0 :
        return vec1
    ret = []
    i = j = 0
    while len(ret) < len(vec1) + len(vec2) :
        if vec1[i] <= vec2[j] :
            ret += [ vec1[i] ]
            i += 1
            if i == len(vec1) :
                break
        else :
            ret += [ vec2[j] ]
            j += 1
            if j == len(vec2) :
                break
    return ret + vec1[i:] + vec2[j:]

def merge(vec) :
    ''' merge sort '''
    if len(vec) < 2 :
        return vec
    mid = len(vec) // 2
    return merge_sorted(merge(vec[:mid]), merge(vec[mid:]))

def parent(idx) :
    ''' parent in heap '''
    return (idx+1)//2-1
def left(idx) :
    ''' left child in heap '''
    return 2*idx+1
def right(idx) :
    ''' right child in heap '''
    return 2*(idx+1)
def fix_down(vec, low, high, idx) :
    ''' fix down in heap '''
    largest, ileft, iright = idx, left(idx), right(idx)
    if ileft <= high and vec[largest] < vec[ileft] :
        largest = low + left(idx-low)
    if iright <= high and vec[largest] < vec[iright] :
        largest = low + right(idx-low)
    if largest != idx :
        vec[idx], vec[largest] = vec[largest], vec[idx]
        fix_down(vec, low, high, largest)
def buildheap(vec, low=0, high=None) :
    ''' build heap '''
    if high is None :
        high = len(vec)-1
    heapsize = high-low+1
    idx = heapsize//2-1
    while idx >= low :
        fix_down(vec, low, high, low+idx)
        idx -= 1
def heapsort(vec, low=0, high=None) :
    ''' heap sort '''
    if high is None :
        high = len(vec)-1
    buildheap(vec, low, high)
    if __debug__:
        print('build',vec)
    while high - low > 0 :
        vec[low], vec[high] = vec[high], vec[low]
        high -= 1
        fix_down(vec, low, high, low)
        if __debug__:
            print(vec)
    return vec

if __name__ == "__main__" :
    from sys import argv, setrecursionlimit
    from time import time
    setrecursionlimit(50000)
    if len(argv) == 1 :
        print('USAGE:', argv[0], ' count [algorithm/value]')
        print('\tSorting: bubble0, bubble1, bubble, insertion, selection,')
        print('\t\tquick, merge, heapsort')
    if len(argv) == 2 :
        v = array(int(argv[1]))
        t = time()
        bubble0(v)
        print('bubble0:', time()-t)
        t = time()
        bubble1(v)
        print('bubble1:', time()-t)
        t = time()
        bubble(v)
        print('bubble:', time()-t)
        t = time()
        insertion(v)
        print('insertion:', time()-t)
        t = time()
        selection(v)
        print('selection:', time()-t)
        t = time()
        quick(v)
        print('quick:', time()-t)
        t = time()
        merge(v)
        print('merge:', time()-t)
        t = time()
        heapsort(v)
        print('heap:', time()-t)
        t = time()
        v.sort()
        print('sort:', time()-t)
    if len(argv) == 3 :
        if argv[2].isnumeric() :
            v = array(int(argv[1]))
            v.sort()
            t = time()
            p = search(v, int(argv[2]))
            print('search: #', p, time()-t)
            t = time()
            p = sorted_search(v, int(argv[2]))
            print('sorted: #', p, time()-t)
            t = time()
            p = binary_search(v, int(argv[2]))
            print('binary: #', p, time()-t)
        else :
            f = locals()[argv[2]]
            t = time()
            f(array(int(argv[1])))
            print(argv[2] + ':', time()-t)
