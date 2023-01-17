import xlsxwriter
from MyParser import array

def writer(parametr):
    book=xlsxwriter.Workbook(r"C:\Users\zeusb\Desktop\MyDATA.xlsx")
    page=book.add_worksheet("data")

    row=0
    column=0

    page.set_column("I:I",20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 20)
    page.set_column("D:D", 20)
    page.set_column("E:E", 20)
    page.set_column("F:F", 20)
    page.set_column("G:G", 20)
    page.set_column("H:H", 30)
    page.set_column("K:K", 30)

    for item in parametr():
        page.write(row,column,item[0])
        page.write(row, column, item[1])
        page.write(row, column, item[2])
        page.write(row, column, item[3])
        page.write(row, column, item[4])
        page.write(row, column, item[5])
        page.write(row, column, item[6])
        page.write(row, column, item[7])
        page.write(row, column, item[8])
        row+=1

        #print(item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8])
    book.close()

writer(array)