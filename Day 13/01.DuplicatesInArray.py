def duplicatesInArray():
    my_arr = [30, 20, 30, 40, 1000, 20, 70, 80, 80, 1000]
    print("Duplicate elements in the given array are: ")
    arr_len = len(my_arr)

    # Searches for all duplicate elements

    for i in range(0, arr_len):    # outer loop
     for j in range(i+1, arr_len):   # inner loop
      if(my_arr[i] == my_arr[j]):    
       print(my_arr[j])

# Driver Code

duplicatesInArray()