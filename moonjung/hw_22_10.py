from openpyxl import load_workbook
import os

if os.path.exists('data.xlsx'):
    wb = load_workbook('data.xlsx')
    sheet = wb.active
    sheet['A1'] = 'data1'
    wb.save('data.xlsx')
else:
    print("파일 없음")