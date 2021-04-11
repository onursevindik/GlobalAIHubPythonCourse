list1 = [0,1,2,3,4,5,6,7,8,9,10]
copy_list1 = list1.copy()
print("Original List", list1)
x = int(len(list1))
hx = int(x/2)
if x %2 == 1:
    for i in range (0, hx):
        list1[i] = copy_list1[i+1+hx]
        list1[i+1+hx] = copy_list1[i]
    print("Swapped List", list1)
else:
    for i in range (0, hx):
        list1[i] = copy_list1[i+hx]
        list1[i+hx] = copy_list1[i]
    print("Swapped List", list1)



n = int(input("Enter a Single Digit Positive Integer Number: "))
if n <= 0 or n > 9:
    print("Enter a Valid Number!")
else:
    for i in range (0,n):
        if i %2 == 0:
            print(i)
