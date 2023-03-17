# python3

def build_heap(data):
    swaps = []
    n = len(data)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    for i in range(n // 2 - 1, -1, -1):
        j = i
        while True:
            left_child = 2 * j + 1
            right_child = 2 * j + 2
            smallest = j
            if left_child < n and data[left_child] < data[smallest]:
                smallest = left_child
            if right_child < n and data[right_child] < data[smallest]:
                smallest = right_child

            if j != smallest:
                swaps.append((j, smallest))
                data[j], data[smallest] = data[smallest], data[j]
                j = smallest
            else:
                break

    return swaps


def main():

    # TODO: add input and corresponding checks
    # add another input for I or F
    # first two tests are from keyboard, third test is from a file
    izvele=(input())
    if "I" in izvele:
        n = int(input())
        data = list(map(int, input().split()))
    if "F" in izvele:
        filename=input()
        with open(f"tests/{filename}") as f:
            n=int(f.readline())
            data = list(map(int, f.readline().split()))


    # input from keyboard
    

    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data,)

    # TODO: output how many swaps were made,
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        if i > j:
            i, j = j, i
        print(i, j)


if __name__ == "__main__":
    main()