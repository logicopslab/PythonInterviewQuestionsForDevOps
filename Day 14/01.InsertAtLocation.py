# given array (list)

my_arr = [1, 2, 3, 4, 5, 6]

num=int(input("Enter a number to insert in your array : "))
index=int(input("Enter the index to insert that value : "))

if index >= len(my_arr):
    print("Index out of bounds, no change in the array!",len(my_arr))
else:
    # insetring element ‘num’ at ‘index’ position
    my_arr.insert(index, num)  

print("Array after inserting",num,"=",my_arr)