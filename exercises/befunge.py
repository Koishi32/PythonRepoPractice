import math
import random
numbers = ('0','1','2','3','4','5','6','7','8','9')
stack = []
output =""
plane = []
current_char =''
CurrentDir = (1,0)
rows=0
colums=0
string_mode= False
def reset_values():
    global current_char
    current_char =''
    global output
    output = ""
    global rows
    rows = 0
    global colums
    colums = 0
    global CurrentDir
    CurrentDir = (1,0)
    global string_mode
    string_mode= False

def interpret(code):
    global rows
    global colums
    global output
    reset_values()
    plane = convert_to_2D_plane(code)
    current_char= plane[rows][colums]
    while (current_char!='@'):
        current_char= plane[rows][colums]
        check_char(current_char,plane)
        rows, colums = ( (rows+CurrentDir[1]) % len(plane) , (colums+CurrentDir[0]) % len(plane[rows]))
    return output

def check_char(element,plane):
    global string_mode
    if (string_mode):
        if (element=='"'):
            string_mode=False
        else:
            stack.append(ord(element))
    else:
        if (numbers.__contains__(element)):
            stack.append(int(element))
        else:
            check_cases(element,plane)

def check_cases(element,plane):
    global string_mode
    global CurrentDir
    global output
    global colums,rows
    match element:
        case '+':
            tup=get_a_b()
            stack.append(tup[0]+tup[1])
        case '-':
            tup=get_a_b()
            stack.append(tup[1]-tup[0])
        case '*':
            tup=get_a_b()
            stack.append(tup[0]*tup[1])
        case '/':
            tup=get_a_b()
            if (tup[0] == 0):
                stack.append(0)
            stack.append(math.floor(tup[1]/tup[0]))
        case '%':
            tup=get_a_b()
            if (tup[0] == 0):
                stack.append(0)
            stack.append(math.floor(tup[1]%tup[0]))
        case '!':
            if (stack.pop() == 0):
                stack.append(1)
            else:
                stack.append(0)
        case '`':
            tup=get_a_b()
            if (tup[1] > tup [0]):
                stack.append(1)
            else:
                stack.append(0)
        case '>':
            CurrentDir = (1,0)
        case '<':
            CurrentDir = (-1,0)
        case '^':
            CurrentDir = (0,-1)
        case 'v':
            CurrentDir = (0,1)
        case '?':
            match (random.randint(0,3)):
                case 0:
                    CurrentDir = (1,0)
                case 1:
                    CurrentDir=(-1,0)
                case 2:
                    CurrentDir=(0,-1)
                case 3:
                    CurrentDir=(0,1)
                case _:
                    CurrentDir = (1,0)
        case '_':
            if(stack.pop() ==0):
                CurrentDir = (1,0)
            else:
                CurrentDir = (-1,0)
        case '|':
            if(stack.pop() ==0):
                CurrentDir = (0,1)
            else:
                CurrentDir = (0,-1)
        case '"':
                string_mode=True
        case ':':
            if(len(stack)==0):
                stack.append(0)
            else:
                a=stack.pop()
                stack.append(a)
                stack.append(a)
        case '\\':
            if (len(stack)>0):
                b=0
                a = stack.pop()
                if not (len(stack)==1):
                    b= stack.pop()
                stack.append(a)
                stack.append(b)
        case '$':
            stack.pop()
        case '.':
            output += str(stack.pop())
        case ',':
            to_output = chr(stack.pop())
            output += str(to_output)
        case '#':
            rows, colums = ( (rows+CurrentDir[1]) % len(plane) , (colums+CurrentDir[0]) % len(plane[rows]))
        case 'p':
            y = stack.pop()
            x = stack.pop()
            v = stack.pop()
            plane[y][x] = chr(v)
        case 'g':
            y = stack.pop()
            x = stack.pop()
            stack.append(ord(plane[y][x]))
        case ' ':
            pass
            
def get_a_b():
    a = int(stack.pop())
    b = int(stack.pop())
    return (a,b)

def convert_to_2D_plane(code):
    list_elements = code.split("\n")
    array=[]
    for a in list_elements:
        array.append(list(a))
    return array

def main ():
    a = interpret('>987v>.v\nv456<  :\n>321 ^ _@')
    print(a)
    factorial = "08>:1-:v v *_$.@\n  ^    _$>\:^"
    print(interpret(factorial)) 
    line = "01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@"
    print(interpret(line))

if __name__ == "__main__":
    main()