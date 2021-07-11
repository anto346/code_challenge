'''
Suppose I have "n" chocolates. and "m" children, if i want to distribute each chocolates to all m children in a sequential order by repeating same list of children if excess in chocolates. how do you distribute?
example 1: if n=3 (chocolates here is 3) , m=3 (children are 3 you can name children as 1,2,3 ) answer: {1:1,2:1,3:1}
example 2: if n=7 and m=5 then child {1:2, 2:2, 3:1, 4:1, 5:1}
can you write a simple python function to resolve this? where n and m are parameters.
'''
def child_chocolate_fn(child, chocolate):
    print("The no of chocolates available", chocolate)
    print("The no of children", child)
    remainder_choco=chocolate%child
    minimum_choco_per_child=chocolate//child
    #print(remainder_choco)
    #print(minimum_choco_per_child)
    empty_list = []
    for i in range (child):
        empty_list.append(minimum_choco_per_child)
    #print(empty_list)
    for j in range (remainder_choco):
        #print(empty_list[j])
        empty_list[j] = minimum_choco_per_child + 1
    #print(empty_list)
    #print("The no of children",len(empty_list))
    for j in range(len(empty_list)):
        #print({j+1:empty_list[j]}, end=" ")
        print("Child {0} got {1} chocolates".format(j+1, empty_list[j]))

if __name__ == "__main__":
    print("Please enter the number of children")
    child = int(input())
    print("Please enter the number of chocolates")
    chocolate = int(input())
    child_chocolate_fn(child, chocolate)
