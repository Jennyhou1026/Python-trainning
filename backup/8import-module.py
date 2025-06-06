# 基本語法：
# import 模組名稱  <<這樣就可以載入模組
# import 模組名稱 as 模組別名 <<把長篇名稱改短
#使用
# 模組名稱或別名.函式名稱（參數資料）
# 模組名稱或別名.變數名稱
# 建立內建的sys模組，並取得資訊
# import sys
# print(sys.platform)
# print(sys.maxsize)

# 建立geometry模組，載入使用
# import geometry
# result=geometry.distance(3,6,7,8) 
# print(result)
# result=geometry.slope(5,8,10,12) 
# print(result)
# 調整搜尋模組的路徑
import sys
sys.path.append("modules")#把geometry.py改放到這邊，sys.path搜尋不到，所以用這條程式碼讓Python多加搜尋"modules"資料夾
print(sys.path) #印出模組的搜尋路徑，模組必須要放在這些地方 Python才會找到 
import geometry
print (geometry.distance(1,1,5,5))