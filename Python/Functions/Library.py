def Left(text, n):
	return text[:n]

def Right(text, n):
	return text[-n:]

def Mid(text, n, m):
	return text[n-1:n+m-1]

def Get_Text(text_path):
	with open(text_path,'r',encoding='utf-8') as f:
		texts = f.readlines()
		
	tmp=''
	for text in texts:
		text=text.strip()
		if text != '':
			tmp = tmp + text + '\n'
	
	tmp=tmp.strip()
	return tmp

def Get_Text_List(text_path):
	texts = Get_Text(text_path)
	
	tmp=[]
	for text in texts.split('\n'):
		if text.strip() != '':
			tmp.append(text.strip())
	
	return tmp

def Write_Text(text_path,text):
	with open(text_path,'w',encoding='utf-8') as f:
		f.write(text)

def Sort_Text(text_path):
	texts=Get_Text_List(text_path)
	texts=sorted(texts)
	
	tmp=""
	
	for text in texts:
		text=text.strip()
		tmp=tmp + text + '\n'
	
	with open(text_path,'w',encoding='utf-8') as f:
		f.write(tmp)

def Get_HTML_Content(URL):
	import requests
	from bs4 import BeautifulSoup
	import time
	
	time.sleep(3)
	data=requests.get(URL)
	return BeautifulSoup(data.content,'html.parser')

def Get_HTML_Text(URL):
	import requests
	from bs4 import BeautifulSoup
	import time
	
	time.sleep(3)
	data=requests.get(URL)
	return BeautifulSoup(data.text,'html.parser')

def Copy_Photo(photo_name):
	import photos
	
	photos.create_image_asset(photo_name)

def Move_Photo(photo_name):
	Copy_Photo(photo_name)
	
	import os
	os.remove(photo_name)

def Add_Text_To_Photo(siori_name,text):
	from PIL import Image, ImageDraw, ImageFont
	import os
	
	tmp=""
	while text != "":
		tmp=tmp + Left(text,20) + "\n"
		text=text[20:]
	
	if os.path.exists(siori_name):
		img=Image.open(siori_name)
	else:
		img = Image.new("RGB",(1215,1000),"white")
	
	draw = ImageDraw.Draw(img)
	font=ImageFont.truetype(os.path.dirname(__file__) + '/mikachan_o.otf',50)
	
	draw.text((20, 80), tmp, fill=(0, 0, 0), font=font)
	img.save(siori_name)

def Get_Files_Name_List_From_Folder(folder_name):
	import glob
	Names=[]
	files=glob.glob(folder_name + "/*")
	for file in files:
		Names.append(file)
	
	return Names

def Get_Domain(URL):
	tmp=URL
	tmp=tmp.replace('https://','')
	tmp=tmp.replace('http://','')
	tmp=tmp.split('/')[0]
	
	return tmp

def Download_Video(URL,folder_name,file_name='%(title)s'):
	import youtube_dl
	import sys, os
	import datetime
	
	ydl_opts = {'outtmpl':file_name + '.%(ext)s','format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]','--merge-output-format':'mkv'}
	
	os.makedirs(folder_name,exist_ok=True)
	before_folder=os.getcwd()
	os.chdir(folder_name)
	
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		result=ydl.extract_info(URL,download=True)
	
	os.chdir(before_folder)

def Test():
	import wx
	
	application = wx.App()
	
	frame = wx.Frame(None, wx.ID_ANY, 'りーたん', pos=(300, 300))
	# 中央へ表示する場合
	frame.Centre()
	frame.CreateStatusBar()
	frame.SetStatusText('りーたん！！！！！！')
	frame.Show()
	
	application.MainLoop()

Test()