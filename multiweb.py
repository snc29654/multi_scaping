import tkinter
import requests
from bs4 import BeautifulSoup
import webbrowser
import os
import sys
from tkinter.scrolledtext import ScrolledText



  
  
class main_class():  
    def __init__(self):
        # ボタン
        btn = tkinter.Button(root, text='実行', command=self.btn_click)
        btn.place(x=10, y=80)

        btn6 = tkinter.Button(root, text='入力クリア', command=self.btn_click6)
        btn6.place(x=10, y=570)

  
  
    def  data_print(self):
        import requests
        message=[]
        datalist = []
        for url in urls:

            webbrowser.open(url)

       
      
# clickイベント
    def btn_click(self):
        textExample.delete("1.0",tkinter.END)
        self.data_print()
    
    def btn_click6(self):
    
        textExample.delete("1.0",tkinter.END)





root = tkinter.Tk()
# 画面サイズ
root.geometry('700x600')
# 画面タイトル
root.title('複数WEB表示')


textExample=ScrolledText(root, height=40,wrap=tkinter.CHAR)
textExample.pack()
textExample.place(x=90, y=40)


# ラベル
lbl = tkinter.Label(text='')
lbl.place(x=10, y=10)
lbl2 = tkinter.Label(text='結果')
lbl2.place(x=10, y=50)




# リストボックスに項目追加
urls = [
    "https://news.yahoo.co.jp/categories/domestic",
    "https://news.yahoo.co.jp/categories/sports",
    "https://news.yahoo.co.jp/categories/entertainment", 
    "https://news.yahoo.co.jp/categories/business", 
    "https://news.yahoo.co.jp/categories/it", 
    "https://news.yahoo.co.jp/categories/world", 
    "https://news.yahoo.co.jp/categories/science", 
    "https://news.yahoo.co.jp/topics/top-picks"
]

c=main_class()  

root.mainloop()
