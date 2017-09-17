import xlrd

d = {}
wb = xlrd.open_workbook('numbers_copy.xlsx')
sh = wb.sheet_by_index(0)
for i in range(52):
    cell_value_class = sh.cell(i,0).value
    cell_value_id = sh.cell(i,1).value
    d[cell_value_class] = cell_value_id
print(d)
