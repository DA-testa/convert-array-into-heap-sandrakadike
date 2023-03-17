# python3
# import io

def build_heap(i,data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)

    parent=i
    leftChild=2*i+1
    rightChild=2*i+1

    if leftChild<=n-1 and data[leftChild]<data[parent]:
        parent=leftChild
    if rightChild<=n-1 and data[rightChild]<data[parent]:
        parent=rightChild

    if i!=parent:
        data[i],data[parent]=data[parent],data[i]

    

    build_heap(parent)
    for i in range(n//2,-1.-1,-1):
        build_heap(i)
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
