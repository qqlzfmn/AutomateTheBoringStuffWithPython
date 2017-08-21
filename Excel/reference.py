# Part reference of module openpyxl.
import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))  # 数据类型：Workbook
print(wb.get_sheet_names())  # Workbook对象的get_sheet_names方法：获取工作簿中所有表名的列表
sheet = wb.get_sheet_by_name('Sheet1')  # Workbook对象的get_sheet_by_name方法：获取工作簿中表名是Sheet1的工作表
print(sheet)
print(type(sheet))  # 数据类型：Worksheet
print(sheet.title)  # Worksheet对象的title属性：获取工作表的表名
anotherSheet = wb.get_active_sheet()  # Workbook对象的get_active_sheet方法：获取工作簿的活动表（活动表是工作簿在Excel中打开时出现的工作表）
print(anotherSheet)
print()

print(sheet['A1'])
print(sheet['A1'].value)
print(type(sheet['A1'].value))
c = sheet['B1']
print(type(c))  # 数据类型：Cell
print(c.value)  # Cell对象的value属性：获取单元格的值
print('Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value)  # Cell对象的row属性：获取单元格行号；Cell对象的column属性：获取单元格列号
print('Cell ' + c.coordinate + ' is ' + c.value)  # Cell对象的coordinate属性：获取单元格名称
print(sheet['C1'].value)
#