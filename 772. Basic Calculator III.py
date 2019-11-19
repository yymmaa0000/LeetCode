# 772. Basic Calculator III
# Hard
# 26584FavoriteShare
# Implement a basic calculator to evaluate a simple expression string.
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
# The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].
# Some examples:
# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
 
# Note: Do not use the eval built-in library function.
class Solution:
    def calculate(self, s: str) -> int:
        def solve_simple(s):
            '''return 1
            stack = [""]
            for i in range(len(s)):
                if s[i] in "+-*/": 
                    if len(stack) > 1:
                        if stack[-2][-1] == "*":
                            temp = int(stack.pop())
                            stack[-1] = str(int(stack[-1][0:len(stack[-1])-1]) * int(temp))
                        elif stack[-2][-1] == "/":
                            temp = int(stack.pop())
                            stack[-1] = str(int(stack[-1][0:len(stack[-1])-1]) // int(temp))
                    stack[-1] += s[i]
                    stack.append("")
                elif i == len(s)-1:
                    stack[-1] += s[i]
                    print(stack[-2][-1])
                    if len(stack) > 1:
                        if stack[-2][-1] == "*":
                            temp = int(stack.pop())
                            stack[-1] = str(int(stack[-1][0:len(stack[-1])-1]) * int(temp))
                        elif stack[-2][-1] == "/":
                            temp = int(stack.pop())
                            stack[-1] = str(int(stack[-1][0:len(stack[-1])-1]) // int(temp))              
                else:
                    stack[-1] += s[i]
                print(stack)
            while len(stack) > 1:
                temp = stack.pop()
                if stack[-1][-1] == "+":
                    stack[-1] = str(int(stack[-1][0:len(stack[-1])-1])+int(temp))
                elif stack[-1][-1] == "-":
                    stack[-1] = str(int(stack[-1][0:len(stack[-1])-1])-int(temp))  
            return stack[0]'''
            i = 0
            while 1:
                if i >= len(s)-1: break
                if s[i] == "*":
                    s[i-1] *= int(s[i+1])
                    del s[i]
                    del s[i]
                elif s[i] == "/":
                    try:
                        s[i-1] = s[i-1]//int(s[i+1])
                    except:
                        print(s[i-1],s[i+1])
                    del s[i]
                    del s[i]
                else: i += 1
                #print(s)
            i = 0
            while 1:
                if i >= len(s)-1: break
                if s[i] == "+":
                    s[i-1] += int(s[i+1])
                    del s[i]
                    del s[i]
                elif s[i] == "-":
                    s[i-1] -= int(s[i+1])
                    del s[i]
                    del s[i]
                else: i += 1
                #print(s)
            return s[0]

        ass = s.split(" ")
        s = "".join(ass)
        temp = []
        i = 0
        while 1:
            if i >= len(s):break
            if s[i] == "-":
                if i ==0 or (isinstance(s[i-1],str) and s[i-1] in "+-*/("):
                    cnt = 1
                    while s[i] == "-":
                        cnt *= -1
                        i += 1
                    temp.append(cnt)
                    temp.append("*")
                    continue
            if s[i].isdigit():
                if len(temp) >0 and isinstance(temp[-1],int): temp[-1] = 10*temp[-1]+int(s[i])
                else:temp.append(int(s[i]))
            else: temp.append(s[i])
            i += 1
        s = temp
        print(s)
        stack = [[]]
        for x in s:
            if x == '(': stack.append([])
            elif x == ")": 
                temp = stack.pop()
                temp_result = solve_simple(temp)
                stack[-1].append(temp_result)
            elif isinstance(x,str) and x in "+-*/":
                stack[-1][-1] = int(stack[-1][-1])
                stack[-1].append(x)
            else: 
                if len(stack[-1]) == 0: stack[-1].append(x)
                elif isinstance(stack[-1][-1] ,str) and stack[-1][-1] in "+-*/": stack[-1].append(x)
                else: stack[-1][-1] += x
            print(stack)
        stack[-1][-1] = int(stack[-1][-1])
        #print(stack)
        return int(solve_simple(stack[0]))
