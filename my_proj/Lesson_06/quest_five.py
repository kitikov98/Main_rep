import openpyxl
import csv

with open('quest_four.csv', mode='r', encoding='utf-8') as func_read:
    reader = csv.reader(func_read)
    field_01 = [line[0] for line in reader]
    reader = csv.reader(func_read)
    field_02 = [line[2] for line in reader]
with open('quest_four.csv', mode='r', encoding='utf-8') as func_read:
    reader = csv.reader(func_read)
    field_04 = [line[3] for line in reader]

print(field_01)
print(field_02)
print(field_04)

name_of_filds = ['', 'person1', 'person2', 'person3', 'person4', 'person5', 'person6']
wb = openpyxl.Workbook()
sheet = wb['Sheet']
for row_index, row in enumerate((name_of_filds, field_01, field_02, field_04)):
    for col_index, value in enumerate(row):
        cell = sheet.cell(row=row_index + 1, column=col_index + 1)
        cell.value = value
wb.save('quest_five.xlsx')
