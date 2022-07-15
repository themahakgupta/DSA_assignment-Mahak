# convert postfix to prefix expression

def push(x):
    global stack 
    global top
    top+=1
    stack[top]=x
def pop():
    global stack
    global top
    x=stack[top]
    top-=1
    return x
def is_operator(x):
    if x=='+' or x=='-' or x=='*' or x=='/':
        return True
    else:
        return False
def con():
    global stack
    global top
    l=len(exp)
    for i in range(0,l):
        if is_operator(exp[i])==True:
            a=stack[top]
            pop()
            b=stack[top]
            pop()
            temp=exp[i]+b+a
            push(temp)
        else:
            push(exp[i])
    print("The prefix expression is",stack[top])
stack=[]
top=-1
exp=input("Enter the postfix expression:")
x=int(input("Enter the range limit:"))
for i in range(x):
    stack.append(0)
con()

