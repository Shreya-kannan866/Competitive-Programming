#To remove the duplicate elements from an array
array_duplicate=[eval(input("Enter an element:")) for i in range(int(input("Enter the number of elements in the array:")))]
final_array=[]
print("Before removing duplicate: ",array_duplicate)
for n in array_duplicate:
    if n not in final_array:
        final_array.append(n)
print("After removing duplicate elements: ",final_array)
