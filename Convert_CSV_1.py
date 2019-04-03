import csv
from openpyxl import *
from numpy import *
import xlsxwriter
import json

workbook = xlsxwriter.Workbook('output_3.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

with open('Sample_3.csv', 'r') as cs:
    row = 0
    read = csv.DictReader(cs)
    for line in read:
        col = 0
        if row ==0 and col == 0:
            firstrow = list(line.keys())
            for i in range(0,len(firstrow)):
                print(firstrow[i], end='')
                val = firstrow[i]
                worksheet.write(row, col, val, bold)
                col += 1
            row += 1
            print(end='\n')
        else:
            
            nextrow = list(line.values())
            for i in range(0,len(nextrow)):
                print(nextrow[i], col, end='')
                nextval = nextrow[i]
                worksheet.write(row, col, nextval)
                col += 1
            row += 1
            print(end='\n')
workbook.close()      
        # print(len(line))
    # var = dict(read)
    # print(type(var))
    
#     for (i,j,k,l,m,n,o,p,q,r) in read:
#         if row ==0 and col ==0:
#             worksheet.write  (row, col, i, bold)
#             worksheet.write (row, col + 1, j, bold)
#             worksheet.write  (row, col + 2, k, bold)
#             worksheet.write  (row, col + 3, l, bold)
#             worksheet.write  (row, col + 4, m, bold)
#             worksheet.write  (row, col + 5, n, bold)
#             worksheet.write  (row, col + 6, o, bold)
#             worksheet.write  (row, col + 7, p, bold)
#             worksheet.write  (row, col + 8, q, bold)
#             worksheet.write  (row, col + 9, r, bold)
#             row +=1
#         else:
#             worksheet.write  (row, col, i)
#             worksheet.write (row, col + 1, j)
#             worksheet.write  (row, col + 2, k)
#             worksheet.write  (row, col + 3, l)
#             worksheet.write  (row, col + 4, m)
#             worksheet.write  (row, col + 5, n)
#             worksheet.write  (row, col + 6, o)
#             worksheet.write  (row, col + 7, p)
#             worksheet.write  (row, col + 8, q)
#             worksheet.write  (row, col + 9, r)
#             row +=1
# workbook.close()

    # for line in read:
    #     print(type(line))

    # with open('Write.xlsx', 'w') as wr:
    #     headerName = ['id','Product_discription','Product_sellername','Product_no','Product_lenght','Product_width','Product_cost','Product_country','Product_name','Product_rating']
    #     writefile = csv.DictWriter(wr, fieldnames = headerName, delimiter='\t')
    #     writefile.writeheader()
        
    #     for row in read:
    #         writefile.writerow(row)
            
    #next(read)
    # with open('Write.csv', 'w', newline='') as wr:
    #     writefile = csv.writer(wr, delimiter='|')
    #     for row in read:
    #         writefile.writerow(row)

# with open('Write.csv', 'r') as cs:
#     read = csv.reader(cs, delimiter='|')
#     for line in read:
#         print(line)
