#arrange words in a string in the order of their length
string=input("Enter a string:")
list_string=string.split()
result=' '.join(sorted(list_string,key=len))
print(result)
