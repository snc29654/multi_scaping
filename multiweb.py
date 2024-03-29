import tkinter
import requests
from bs4 import BeautifulSoup
import webbrowser
import os
import sys
from tkinter.scrolledtext import ScrolledText


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

  
  
class main_class():  
    def __init__(self):


        root = tkinter.Tk()
        # 画面サイズ
        root.geometry('700x600')
        # 画面タイトル
        root.title('スクレいピング')


        self.textExample=ScrolledText(root, height=40,wrap=tkinter.CHAR)
        self.textExample.pack()
        self.textExample.place(x=90, y=40)


        # ラベル
        lbl = tkinter.Label(text='')
        lbl.place(x=10, y=10)
        lbl2 = tkinter.Label(text='結果')
        lbl2.place(x=10, y=50)






        # ボタン
        btn = tkinter.Button(root, text='実行', command=self.btn_click)
        btn.place(x=10, y=80)

        btn6 = tkinter.Button(root, text='入力クリア', command=self.btn_click6)
        btn6.place(x=10, y=570)





        root.mainloop()


  
  
    def  data_print(self):
        import requests
        message=[]
        datalist = []
        for url in urls:


            site = requests.get(url)
            data = BeautifulSoup(site.text, 'html.parser')
            self.textExample.insert(tkinter.END,data.find_all("p"))

            SAMPLE_DIR = "../"
 
            if not os.path.exists(SAMPLE_DIR):
            # ディレクトリが存在しない場合、ディレクトリを作成する
                os.makedirs(SAMPLE_DIR)       

            web_site=SAMPLE_DIR+"\\scraping_result.html"
            f = open(web_site, 'w',encoding='utf-8', errors='ignore')
            message = str(data)



            datalist.append('<html>\n')
            datalist.append('<head>\n')
            datalist.append('<title>from python</title>\n')
            datalist.append('</head>\n')
            datalist.append('<body>\n')
            datalist.append(message)
            datalist.append('\n')
            datalist.append('</body>\n')
            datalist.append('</html>\n')

        f.writelines(datalist)

        f.close()
        webbrowser.open(web_site)

       
      
    # clickイベント
    def btn_click(self):
        self.textExample.delete("1.0",tkinter.END)
        self.data_print()
    
    def btn_click6(self):
    
        self.textExample.delete("1.0",tkinter.END)



c=main_class()  




