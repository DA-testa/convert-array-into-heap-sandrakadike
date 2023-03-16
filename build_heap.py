# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)

    # build a binary heap bottom-up starting from the last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        j = i
        while True:
            k = j
            left_child = 2 * j + 1
            right_child = 2 * j + 2
            if left_child < n and data[left_child] < data[k]:
                k = left_child
            if right_child < n and data[right_child] < data[k]:
                k = right_child
            if k == j:
                break
            data[j], data[k] = data[k], data[j]
            swaps.append((j, k))
            j = k



    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
