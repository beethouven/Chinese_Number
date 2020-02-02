import unicodedata

# 整理字串分開成數字與國字並且將數字合併
def combin_number(ss):
    num_array = []
    num = ''
    order = []

    n = 0
    s = list(ss)
    for x in s :
        if x.isdigit():
            num_array.append(x)
            order.append(n)
            if n == (len(s)-1):
                for y in num_array :
                    num = num + y
                s[order[0]] = num
                order.remove(order[0])
                order.reverse()

                for z in order :
                    s[z]=""
                num_array = []
                num = ''
                order = []                   
        elif not (x.isdigit()) and num_array != []:
            for y in num_array :
                num = num + y
            s[order[0]] = num
            order.remove(order[0])
            order.reverse()

            for z in order :
                s[z]=""
            num_array = []
            num = ''
            order = []
        n=n+1
    while "" in s :
        s.remove("")
    return s


# 判斷是否為數字 可接受大小寫中文數字
# 若非數字則送出false
def is_number(s):
    try:
        n=float(s)
        return n
    except ValueError:
        pass

    try:
        n = unicodedata.numeric(s)
        return n
    except (TypeError,ValueError):
        pass
    return "not a number"

# 輸入的字串先分類數字國字 再判斷是否有非數字 最後算出值
# 可中文阿拉伯數字夾雜
# 例如 六百五十億300萬9527 17萬六千 360兆七千萬零一百 都可接受

def Chinese_number(a="六十"):

    b = []
    under_thousand = []
    sum = 0
    lt_sum = 0
    carry = 0
    
    ComNumber = combin_number(a)
   
    for x in ComNumber :
        ComNumber = is_number(x)
        if ComNumber == "not a number" :
            return False
        b.append(ComNumber)

    print(b)
    b.reverse()
    while 0 in b :
        b.remove(0)
    print(b)


    i = 0
    while i < len(b) :
        if b[i] < 9999 :
            under_thousand.append(b[i])
            i=i+1
        else:
            break
    

    while i < len(b) :
        
        if (b[i] % 10 == 0 and b[i] > 1000 and b[i]> carry) :
            sum = sum + lt_sum*carry
            lt_sum = 0
            carry = b[i]
            if (b[i+1]%10) != 0 :
                lt_sum = lt_sum + b[i+1]
                if i == (len(b)-2) :
                    sum = sum + lt_sum*carry
                    break
            elif ( (b[i+1]%10) == 0 and i == (len(b)-2) ) :
                lt_sum = lt_sum + b[i+1]
                sum = sum + lt_sum*carry
                break



        if b[i] < carry :
            if i == len(b)-1 and lt_sum != 0 :
                i=i+1
                continue

            if ( b[i+1] > carry and lt_sum == 0 ):
                sum = sum + b[i]*carry
                i=i+1
                continue                

            if ( b[i] %10 == 0 and i < (len(b)-1)):
                lt_sum = lt_sum + (b[i]*b[i+1])
                if i == (len(b)-2) :
                    sum = sum + lt_sum*carry
    
        i=i+1
            
    if len(under_thousand) > 0 :
        if len(under_thousand) == 1 :
            sum = sum + under_thousand[0]
        else :
            thousand_i = 0
            while thousand_i < len(under_thousand) :
                if ( under_thousand[thousand_i] %10 == 0):
                    sum=sum+(under_thousand[thousand_i]*under_thousand[thousand_i+1])
                thousand_i=thousand_i+1
            if (under_thousand[0] % 10 != 0) :
                sum=sum+under_thousand[0]

    return sum

def many_Chinese(*a) :
    number_array = []
    for n in a :
        b = Chinese_number(n)
        number_array.append(b)
    
    return number_array

#可於此測試功能
number_array = many_Chinese("五十億7001萬5000")
print(number_array)