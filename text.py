



import xlsxwriter as xw


name = ['小明','小榄','大额']
content = ['及炯炯那','能加快和接口那地方','制授课的']
zan = ['334','332','566']




workbook = xw.Workbook("a.xlsx")  # 创建工作簿
worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
worksheet1.activate()  # 激活表
col = ord('A')  # 定义要开始的列

# names 为一个姓名列表：["李四", "张三"]
# age 为一个年龄列表:[18, 19]
worksheet1.write_column(chr(col) + "1", name)
worksheet1.write_column(chr(col + 1) + "1", content)
worksheet1.write_column(chr(col + 2) + "1", content)
workbook.close()
