# python3
# import io

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)

    for i in range(n//2, -1, -1):
        parent = i
        leftChild = 2*i + 1
        rightChild = 2*i + 2

        # Find the smallest child node
        if leftChild < n and data[leftChild] < data[parent]:
            parent = leftChild
        if rightChild < n and data[rightChild] < data[parent]:
            parent = rightChild

        if i != parent:
            data[i], data[parent] = data[parent], data[i]
            swaps.append((i, parent))

            # Continue the heapify process from the smallest child node
            child = parent
            while child < n//2:
                parent = child
                left_child = 2*parent + 1
                right_child = 2*parent + 2

                if left_child < n and data[left_child] < data[parent]:
                    parent = left_child
                if right_child < n and data[right_child] < data[parent]:
                    parent = right_child

                if parent == child:
                    break

                data[parent], data[child] = data[child], data[parent]
                swaps.append((parent, child))

                child = parent
    return swaps

    
def main():
    
    # TODO : add input and corresponding checks
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
    # n = int(input())
    # data = list(map(int, input().split()))

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
