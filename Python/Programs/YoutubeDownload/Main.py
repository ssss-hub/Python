import sys
sys.path.append('/content/drive/My Drive/Colab Notebooks/Personal_Library/')
import Library
import os
from tqdm import tqdm

def Delete_Text(text_path,text):
	tmp=Library.Get_Text_List(text_path)
	Library.Write_Text(text_path,'',True)
	for i in tmp:
		if i!=text:
			Library.Write_Text(text_path,i)

urls=set()
url_text=os.path.join(os.getcwd(),'URL.txt')

if len(Library.Get_Text(url_text))==0:
	Library.Write_Text(url_text,input('URLを入力してください。'),True)

if input('画像化しますか？(y or n)')=='y':
	make_photo=True
else:
	make_photo=False

for i in tqdm(Library.Get_Text_List(url_text)):
	Library.Youtube_Download(i,os.path.join(os.getcwd(),'Download_Files'),make_photo)
	Delete_Text(url_text,i)

print('終了')