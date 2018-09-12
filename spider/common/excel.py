# -*- coding:utf-8 -*-
import xlrd

class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    # def dict_data(self):
    #     if self.rowNum <= 1:
    #         print("总行数小于1")
    #     else:
    #         r = {}
    #         for i in range(self.colNum):
    #             s = []
    #
    #             # 遍历第i列的所有值，放入列表
    #             for j in range(1, self.rowNum):
    #                 values = self.table.row_values(j, start_colx=i, end_colx=i+1)
    #                 s.append(values[0])
    #
    #             #取列名做key，取该列的所有值的列表为value
    #             r[self.keys[i]] = s
    #
    #         return r

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j=1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r

    def get_data(self, row, col):
        values = self.table.cell(row-1, col-1)
        return values


if __name__ == "__main__":
    filepath = "C:\\test.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath, sheetName)
    print(data.dict_data())
    # print(data.get_data(2, 3))