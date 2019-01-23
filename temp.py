

'''

workbook = xlrd.open_workbook(r'D:\login.xlsx')
sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始
#获取sheet1的第一行的第一个单元格的内容
username1=int(sheet1.row(1)[0].value)
password1=int(sheet1.row(1)[1].value)

'''


def shell(arr):
    n=len(arr)
    h=1
    while h<n/3:
        h=3*h+1
    while h>=1:
        for i in range(h,n):
            j=i
            while j>=h and arr[j]<arr[j-h]:
                arr[j], arr[j-h] = arr[j-h], arr[j]
                j-=h
        h=h//3
    return arr
print(shell([1,5,3,2]))
