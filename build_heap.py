# python3


def build_heap(data):
    swaps = []
    n = len(data)

    # iterate over all non-leaf nodes in reverse order
    for i in range(n // 2 - 1, -1, -1):
        # call sift_down to move the current node to its correct position
        j = i
        while True:
            left_child = 2 * j + 1
            right_child = 2 * j + 2

            # find the smallest child
            smallest = j
            if left_child < n and data[left_child] < data[smallest]:
                smallest = left_child
            if right_child < n and data[right_child] < data[smallest]:
                smallest = right_child

            if j != smallest:
                # swap the current node with the smallest child
                swaps.append((j, smallest))
                data[j], data[smallest] = data[smallest], data[j]
                j = smallest
            else:
                break

    return swaps


def main():

    # TODO: Add input and corresponding checks
    # Add another input for I or F
    # First two tests are from keyboard, third test is from a file
    izvele=(input())
    if "I" in izvele:
        n = int(input())
        data = list(map(int, input().split()))
    if "F" in izvele:
        filename=input()
        with open(f"tests/{filename}") as f:
            n=int(f.readline())
            data = list(map(int, f.readline().split()))


    # Input from keyboard
    # n = int(input())
    # data = list(map(int, input().split()))

    # Checks if length of data is the same as the said length
    assert len(data) == n

    # Calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data,)

    # TODO: Output how many swaps were made,
    # this number should be less than 4n (less than 4*len(data))

    # Output all swaps
    print(len(swaps))
    for i, j in swaps:
        # Swap the elements in swaps before printing them
        if i > j:
            i, j = j, i
        print(i, j)


if __name__ == "__main__":
    main()