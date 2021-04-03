def sumar(a, b):
    return a + b

def siftDown(a, start, end):
    root = start
    while root*2 + 1 <= end:
        child = root*2 + 1
        swap = root
        if a[swap] < a[child]:
            swap = child;
        child += 1
        if child <= end and a[swap] < a[child]:
            swap = child
        if swap == root:
            return
        else:
            a[root], a[swap] = a[swap], a[root]
            root = swap

def heapify(a):
    end = len(a) - 1
    for i in range(end - 1, -1, -1):
        siftDown(a, i, end)
    return a

