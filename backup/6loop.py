#迴圈是寫出一段程式，不斷重複執行
#while 布林值：
    #若布林值為ＴＲＵＥ，執行命令
    #回到上方，做下一次的迴圈判斷
# EX:
#while n<5:
    #print("變數n的資料是：", n)
    #n+=1
#n=1
#while n<=3:
#    print(n)
#    n+=1
#!!! 1+2+3...+10!!!
#n=1
#sum=0 #紀錄累加的結果
#while n<=10:
#    sum=sum+n
#    n+=1
#print(sum)
    
#for 變數名稱  in 列表ＯＲ字串：
    #將列表中的項目或是字串中的字元逐一取出，逐一處理
#for x in [4,1,2]:列表一個個抓出來
    #print("逐一取得列表中的資料",x)
#for c in "Disney":字串一個抓出來
    #print("逐一取得列表中的資料",c)
#for x in range(5,12):
#    print(x)
#for經常搭配range()可以使用連續數字
#for 變數名稱 in range(3):([0,1,2]只有一個數字定義結尾)/range(3,8)開頭跟結尾[3,4,5,6,7]
#相當於
#for 變數名稱 in [0,1,2]:  
#用for迴圈來寫１＋２＋．．．＋１０

sum=0
for x in range(1,11):
    sum=sum+x
print(sum)