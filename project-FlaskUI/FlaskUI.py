from openpyxl import Workbook
from openpyxl import load_workbook
import csv 

wb = Workbook()
ws = wb.active
ws['A1'] = "birthday"
ws['B1'] = "fav colour"
ws['C1'] = "favourite food"
ws.append(["1st Jan 2008", "green", "pretzels"])
ws.append(["1", "2", "3"])

wb.save("FlaskUI.xlsx")

#def open_workbook(path):
    #workbook = load_workbook(filename=path)
    #print(f"Workskeet names: {workbook.sheetnames}")
    #sheet = workbook.active
    #print(sheet)
    #print(f"he title of the Worksheet is:{sheet.title}")

#if __name__ == "__main__":
    #open_workbook("books.xlsx")


