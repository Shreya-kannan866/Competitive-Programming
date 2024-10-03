#Design your own stack
stack=[]
def is_empty():
    if len(stack)==0:
        return True
    else:
        return False
def push(value):
    stack.append(value)
    return "Value is pushed into the stack"
def pop():
    if is_empty()==False:
        return stack.pop()
    else:
        return "Stack is empty"
def peek():
    if is_empty()==False:
        return stack[-1]
    else:
        return "Stack is empty"
print("""Stack operations:
1. Push
2. Pop
3. Peek""")
ch=int(input("Enter your choice:"))
if ch==1:
    value=eval(input("Enter a stack element:"))
    print(push(value))
elif ch==2:
    print(pop())
elif ch==3:
    print(peek())
else:
    print("Invalid option!")
