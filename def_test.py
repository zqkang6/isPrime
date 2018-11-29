def lineSpilt(line):
    plist = ['，', '。', '！', '？']
    for p in plist:
        line = line.replace(p, '\n')
    return line.split('\n')

def linePrint(line):
    global linewidth
    print(line.center(linewidth, chr(12288)))

txt = '''昨夜斗回北，今朝岁起东。
我年已强仕，无禄尚忧农。
桑野就耕父，荷锄随牧童。
田家占气候，共说此年丰。'''

newlines = lineSpilt(txt)
linewidth = 25
for line in newlines:
    linePrint(line)


'''
def isNum(n):
    n = type(eval(n))
    if n == type(1):
        return True
    elif n == type(1.0):
        return True
    elif n == type(1 + 1j):
        return True
    else:
        return False
try:
    print(isNum(input("请输入你想要询问的内容")))
except:
    print('False')
    #print(isNum(input("请输入数字内容,不要输入字符等其他内容")))
#print(isNum(input("请输入你想要询问的内容")))
'''
import math
def isPrime(data):
    try:
        #isinstance(1, data)
        if(data == 2 or data== 1):
            #print(True)
            return True
        if(data % 2 == 0):
            #print(False)
            return False
        else:
            fanwei = math.sqrt(data)+1
            for i in range(2, int(fanwei)):
                if(data % i == 0):
                    #print(False)
                    return False
                    break
            #print(True)
            return True
    except:
        print("输入的内容不是整数")

try:

    #data = eval(input("请输入需要验证是否为质数的值"))
    #isPrime(data)
    for i in range(1, 201):
        if(isPrime(int(i))):
            print(i, end=' ')
except:
    print("输入的数值不是数值")
