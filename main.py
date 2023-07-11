import openpyxl
import pandas as pd 

file = 'universidades.xlsx'
data = pd.ExcelFile(file)
# print(data.sheet_names) #this returns the all the sheets in the excel file # [universidades]
df = data.parse('universidades')
df.info

# print(df.head(10)) # print first 10 rows 

ps = openpyxl.load_workbook('universidades.xlsx')
sheet = ps['universidades']
sheet.max_row 

for row in range(1, 5):
# each row in the spreadsheet represents information for a particular purchase.
    code = sheet['I' + str(row)].value
    name = sheet['J' + str(row)].value
    
    print('code: ', code)
    print('name: ', name)

# Each value in a cell is represented by a column letter and a row number. So #the first element in the sheet is B1, next column C1 and so on. This enables #to iterate over the entire cells.