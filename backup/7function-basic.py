#函式：程式碼包裝在一個區塊中，方便隨時呼叫使用
#先定義（建立）> 再呼叫
#def 函式名稱(參數名稱):   def sayHello():
#    函式內部的程式碼          print("Hello")

# def say(msg):
#     print(msg)
#呼叫函式 say(Disney)
# def say(n1,n2):
#     result=n1+n2
#     print(result)
#呼叫函式 say(7,8)
#回傳值：基本語法
# def 函式名稱(參數名稱):
#     函式內部程式碼
#     return #結束函式，return後面沒資料回傳None，有資料回傳資料
#def say(msg):
#     print(msg)
#     return
#呼叫函式，取得回傳值
#value=say("Disney World")
#print(value) #因return後面沒有東西所以這邊印出None
# def add(n1,n2):
#     result=n1+n2
#     return "Disney Land"
#value=add(3,4)
#print(value)印出Disney Land

#！！！def add(n1,n2):
#     result=n1+n2
#     return result
#value=add(3,4)
#print(value)印出７

# def multiply(n1,n2):
#     print(n1*n2)
#     #return n1*n2#這裡沒有寫回傳值，所以會回傳none。如果寫return 10<<則會回傳10
# value=multiply(7,9)
# print(value)#回傳none

# def multiply(n1, n2):
#     sum=n1 * n2  # 這邊印出來
#     breakpoint()＃quit跳出
#     return sum
# sum= multiply(7, 9)
# print(sum)

# def multiply(n1, n2):
#     #breakpoint()
#     return n1 * n2
# sum= multiply(5, 9) + multiply(4, 8)
# print(sum)
# #有回傳值才能把值帶出來外面使用

#函式最大的用途：同樣的程式一直重複寫，可以用程式的包裝，同樣的邏輯可以重複利用
#程式的包裝（統一縮排cmd+[or])
def caculate(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)

caculate(20)