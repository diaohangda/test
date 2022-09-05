import pandas as pd

class createtrExcel():
    def __init__(self,filename,sheetname,data):
        self.filename=r'./'+filename+'.xlsx'
        self.sheetname=sheetname
        self.data=data

    def createrWookbook(self):
        df = pd.DataFrame(columns=["店铺名", "店铺地址",'联系','图一','图片二','图片三','图片四','图片五',])
        df.to_excel(self.filename, index=False,sheet_name=self.sheetname)

    # def addSheet(self):
    #     df = pd.DataFrame()
    #     book = load_workbook(self.filename)
    #     writer = pd.ExcelWriter(self.filename, engine='openpyxl')
    #     writer.book = book
    #     df.to_excel(writer, self.sheetname)
    #     writer.save()

    def pandas_insert(self):
        table = pd.read_excel(self.filename, sheet_name=self.sheetname, engine='openpyxl', keep_default_na=False)
        d1 = pd.DataFrame(self.data,columns=["店铺名", "店铺地址",'联系','图一','图片二','图片三','图片四','图片五',])
        # ,columns=["店铺名", "店铺地址",'联系','图一','图片二','图片三','图片四','图片五',],
        d1.fillna('NaN')
        df_new = pd.concat([table,d1], ignore_index=True,)
        df_new.to_excel(self.filename, sheet_name=self.sheetname, index=False, header=True)


