#迴圈控制進階流程
#break & continue  這兩個一定要跟迴圈搭配
#！！！break
# n=0
# while n<5:
#     if n==3:
#         break
#     print(n) #印出迴圈中的n
#     n+=1
# print("最後的n:",n) #印出迴圈結束後的n

#continue 
# n=0
# for x in range(4):
#     if x%2==0:
#         continue
#     print(x)

# print("最後的：",n)

# n=0
# for x in [0,1,2,3]:
#     if x%2==0:
#         continue
#     print(x)
#     n+=1

# print("最後的：",n)

#else

# sum=0
# for n in range(1,11):
#     sum+=n
# else:
#     print(sum)#印出１＋２＋．．＋１０結果

#綜合範例： 找出整數平方根
#輸入９得到3
#輸入１１得到沒有平方根
n=input("輸入一個正整數：")
n=int(n)#轉換輸入成數字
for i in range(n): #i從０～ n-1
    if i*i==n:
        print("整數平方根",i)
        break # 用break 強制結束迴圈時，不會值性else
else:
    print("沒有整數平方根")