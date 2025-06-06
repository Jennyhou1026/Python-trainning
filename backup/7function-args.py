#參數的預設資料
# def power(base, exp=0):#次方沒寫，預設是０，任和數０次方會得出１
#     print(base**exp)#**代表開方
# power(3,2)#３的２次方
# power(4)
#使用參數名稱對應
# def divide(n1,n2):
#     print(n1/n2)
# divide(2,4)
# divide(n2=2,n1=4)
#無限/不定參數資料
def avg(*ns):
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))

avg(3,4)
avg(10,3,4)
avg(-7,10,3,4)