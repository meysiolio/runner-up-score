if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    L = list(set(arr))
    
    maximum = max(L)
    max_index = [i for i,j in enumerate(L) if j == maximum]
    
    for k in max_index:
        del L[0]

    print(max(L))
