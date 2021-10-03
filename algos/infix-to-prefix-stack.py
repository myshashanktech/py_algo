# Convert a given infix expression into prefix notation using Stack.

 

# Input Description:
# The code should take a string of arbitrary length (infix notation).

# Output Description:
# Print the corresponding prefix notation form.

# Sample Input :
# (a+b)
# Sample Output :
# +ab


## Solution


class Stack:
    # initialize the stack
    def __init__(self, size):
        self.stack = []
        self.size = size
    
    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)           

    def pop(self):
        result = -1

        if self.stack != []:
            result = self.stack.pop()

        return result
    
    def display(self):
        if self.stack == []:
            print("Stack is empty!")
        else:
            print("Stack data:")
            for item in reversed(self.stack):
                print(item)
    
    def isEmpty(self):
        return self.stack == []
    
    def topChar(self):
        result = -1

        if self.stack != []:
            result = self.stack[len(self.stack) - 1]

        return result


def isOperand(c):
    opr = ["/", "-","+","^","*","(",")"]
    if c not in opr:
        return True
    else:
        return False

# check for the operators (add if some are necessary)
operators = "+-*/^"

# Returns true if the operator is present in the string
def isOperator(c):
    return c in operators

def getPrecedence(c):
    result = 0

    for char in operators:
        result += 1

        if char == c:
            if c in '-/':
                result -= 1
            break

    return result


def toPostfix(expression):
    result = ""

    stack = Stack(len(expression))

    for char in expression:
        if isOperand(char):
            result += char
        elif isOperator(char):
            while True:
                topChar = stack.topChar()

                if stack.isEmpty() or topChar == '(':
                    stack.push(char)
                    break
                else:
                    pC = getPrecedence(char)
                    pTC = getPrecedence(topChar)

                    if pC > pTC:
                        stack.push(char)
                        break
                    else:
                        result += stack.pop()

        elif char == '(':
            stack.push(char)
        elif char == ')':
            cpop = stack.pop()

            while cpop != '(':
                result += cpop
                cpop = stack.pop()

    while not stack.isEmpty():
        cpop = stack.pop()
        result += cpop

    return result

flag = "upper"
a = str(input())
for i in a:
    if i.islower() == True:
        flag = "lower"
        a.upper()
        break
tem = []
for i in a[::-1]:
    if i == "(":
        tem.append(")")
    elif i == ")":
        tem.append("(")
    else:
        tem.append(i)
a = ''.join(tem)

postfix = toPostfix(a)
print(postfix[::-1])