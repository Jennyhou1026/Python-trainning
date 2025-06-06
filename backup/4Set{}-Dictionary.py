#集合的運算，使用大括號{}
#s1={3,4,5}
#s2={4,5,6,7}
#s3=s1&s2 #＆交集，取兩個集合中，相同的資料
#s4=s1|s2 #｜聯集，取兩個集合中所有資料
#s5=s1-s2 #-差集，從s1中減去跟s2重疊的資料({3})
#s6=s2-s1 #{6,7}
#s7=s1^s2 #反交集，取兩個集合中，不重疊的部分{3,6,7}
#print(s7)
#print(10 not in s1)# True
#print(10 in s1)# False
#print(3 in s1)# True(可用in 或是not in看看資料有沒有在Set裡面)
#s=set("Disney") #Set(字串)
#print(s)#會自動幫我拆解成字串，重複的部分不會加進來
#print("d" in s) #False，大小寫有差Ｄ就ＴＲＵＥ

#字典的運算：Key：Value的配對 也是用{}
#dic={"apple":"蘋果", "bug":"蟲族"}
#print(dic["bug"])
#dic["bug"]="蟲王"
#print(dic["bug"])
#print(dic)

#dic={"apple":"蘋果", "bug":"蟲族"}
#print("bug" in dic) # 判斷是否適用”key"來做，是否存在dic裡

#dic={"apple":"蘋果", "bug":"蟲族"}
#print(dic)
#del dic["apple"] #刪除字典中的鍵值對(Key-Value pair)
#print(dic)

#以列表資料去當基礎去產生字典
#dic={x:x*2 for x in [列表]}
dic={x:x*2 for x in [3,4,5]}
print(dic)