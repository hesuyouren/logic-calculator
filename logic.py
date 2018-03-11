from itertools import product
from copy import deepcopy
dict={ 'neg': 5,'con' : 4,'dis' : 3,'imp' : 2,'bil' : 1}

stack1=[]
stack=[]

a = input().replace('﹁',' neg ').replace('∧',' con ').replace('∨',' dis ').replace('→',' imp ').replace('↔','bil').replace('(','( ').replace(')',' )').split()

for i in a:
    if i in dict.keys():
        if len(stack1) == 0:
            stack1.append(i)
        else:
            while 1:
                if len(stack1)== 0:
                    break
                else:
                    if stack1[-1] == '(' :
                        break
                    elif stack1[-1] in dict.keys():
                        if dict[i] <= dict[stack1[-1]]:
                            stack.append(stack1.pop())
                        else:
                            break
            stack1.append(i)

    elif i == '(':
        stack1.append(i)
    elif i == ')':
        while 1:
            if stack1[-1] == '(':
                stack1.pop()
                break
            else:
                stack.append(stack1.pop())
    else:
        stack.append(i)


while len(stack1)>0:
    stack.append(stack1.pop())

set1=set()
for i in stack:
    if i.isalpha() == 1:
        if len(i) == 1:
            set1.add(i)
        else:pass
    else:pass

letter=[]
for i in set1:
    letter.append(i)
letter.sort()

    
def h(stack):
    stack2=[]
    for j in stack:
        if j == 'neg':
            ans = stack2.pop()
            if ans == 1:
                stack2.append(0)
            else:
                stack2.append(1)
        elif j == 'con':
            m = stack2[-2]
            n = stack2[-1]
            if m and n == 1:
                stack2.pop()
                stack2.pop()
                stack2.append(1)
            else:
                stack2.pop()
                stack2.pop()
                stack2.append(0)
        elif j == 'dis':
            m = stack2[-2]
            n = stack2[-1]
            if m or n == 1:
                stack2.pop()
                stack2.pop()
                stack2.append(1)
            else:
                stack2.pop()
                stack2.pop()
                stack2.append(0)
        elif j == 'imp':
            m = stack2[-2]
            n = stack2[-1]
            if m == 1:
                if n == 0:
                    stack2.pop()
                    stack2.pop() 
                    stack2.append(0)
                else:
                    stack2.pop()
                    stack2.pop()
                    stack2.append(1)
            else:
                stack2.pop()
                stack2.pop()
                stack2.append(1)
        elif j == 'bil':
            m = stack2[-2]
            n = stack2[-1]
            if m == n:
                stack2.pop()
                stack2.pop()
                stack2.append(1)
            else:
                stack2.pop()
                stack2.pop()
                stack2.append(0)
        else:
            stack2.append(j)
    return stack2.pop()


for i in letter:
    print(i,end='  ')
print('C')


num = len(letter)

lst = list(product([0,1],repeat=num))



for j in lst:
    stack_1 = deepcopy(stack)
    stack_ = stack_1
    for i in range(len(letter)):
        for k in range(len(stack_)):
            if stack_[k] == letter[i]:
                stack_[k] = j[i]
        if j[i] == 1:
            print('T',end='  ')
        else:
            print('F',end='  ')
    if h(stack_)==1:
        print('T')
    else:
        print('F')
