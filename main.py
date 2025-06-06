# 主程式
# 封包用來整理，分類模組程式
# 建立封包－專案檔案配置
# －專案資料夾
#     －主程式.Py
#     －封包資料夾
#         －__init__.py(__是兩個半形底線)
#         －模組１.Py
#         －模組２.py
# 主程式
# import 封包名稱.模組名稱
# import 封包名稱.模組名稱 as 模組別名
import geometry.point
result=geometry.point.distance(3,4)
print("距離",result)

import geometry.line 
result= geometry.line.slope(1,1,3,4)
print("斜率",result)

import geometry.line as linelen # 使用別名用法
result= linelen.len(1,1,3,4)
print("長度",result)