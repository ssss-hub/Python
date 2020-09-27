from tqdm import tqdm
import os


def Delete_Text(text_path, text):
    tmp = Get_Text_List(text_path)
    Write_Text(text_path, '')
    for i in tmp:
        if i != text:
            Write_Text(text_path, i)


def Write_Text(text_path, text):
    with open(text_path, 'w', encoding='utf-8') as f:
        f.write(text)


def Get_Text_List(text_path):
    texts = Get_Text(text_path)

    tmp = []
    for text in texts.split('\n'):
        if text.strip() != '':
            tmp.append(text.strip())

    return tmp


def Get_Text(text_path):
    with open(text_path, 'r', encoding='utf-8') as f:
        texts = f.readlines()

    tmp = ''
    for text in texts:
        text = text.strip()
        if text != '':
            tmp = tmp + text + '\n'

    tmp = tmp.strip()
    return tmp


def Download_Video(URL, folder_name):
    import os
    import youtube_dl

    os.makedirs(folder_name, exist_ok=True)
    before_folder = os.path.dirname(__file__)
    os.chdir(folder_name)
    isSucceed = True
    try:
        ydl_opts = {'outtmpl': '%(title)s.%(ext)s',
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]', '--merge-output-format': 'mkv'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(URL, download=True)
    except:
        try:
            ydl_opts = {'outtmpl': '%(title)s.%(ext)s', 'format': 'best'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                result = ydl.extract_info(URL, download=True)
        except:
            isSucceed = False

    os.chdir(before_folder)

    return isSucceed


urls = set()
url_text = os.path.join(os.path.dirname(__file__), 'URL.txt')

if len(Get_Text(url_text)) == 0:
    Write_Text(url_text, input('URLを入力してください。'), True)

for i in tqdm(Get_Text_List(url_text)):
    isSucceed = Download_Video(i, os.path.join(
        os.path.dirname(__file__), 'Download_Files'))
    if isSucceed:
        Delete_Text(url_text, i)

print('終了')
