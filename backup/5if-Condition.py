#判斷式

#四則運算
n1=int(input("請輸入數字一："))#第一層轉化成數字型態，第二層輸入字串
n2=int(input("請輸入數字二："))
op=input("請輸入運算：+,-,*,/:")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else :
    print("不知支援的運算")

#x=input("請輸入數字：") #取得字串形式的使用者輸入
#x=int(x) #將字串型態轉成數字型態
#if x>100:
#    print("大於100")
#elif x>50:
#     print("大於50 小於等於100")
#else:
#   print("小於等於50")

#if False:
#    print("True 執行")
#else:
#    print("False 執行")