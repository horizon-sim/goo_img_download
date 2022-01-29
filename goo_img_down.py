# MIT License 
# Reference : https://github.com/Joeclinton1/google-images-download


from google_images_download import google_images_download 
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox

root = Tk()
root.title("구글 이미지 다운로드")
root.geometry("640x480+500+200") 
root.resizable(False, False) 

# 경로 선택
def dir_choice():
    dir_path = filedialog.askdirectory(parent=root,initialdir="/",title='폴더를 선택해주세요.')
    dir.delete(0, END)
    dir.insert(0, dir_path)
    # print("\ndir_path : ", dir_path) # 디버깅

# 경로 확인
def dir_check():
    if directory[0:3] == "C:/" or "D:/" or "E:/" or "F:/" or "G:/" or "H:/" or "I:/":
        pass
    else:
        print(directory[0:3])
        msgbox.showwarning("경고", "경로를 제대로 작성해주세요.")
        
# 이미지 크롤링
def Google_img_crawling():
    global keyword
    global limit
    global directory
    
    keyword = search.get()
    limit = Limit_number.get()
    directory = dir.get()
    
    # 오류 처리
    if keyword == "":
        msgbox.showwarning("경고", "검색 키워드를 작성해주세요.")
    elif limit == "":
        msgbox.showwarning("경고", "이미지 개수를 작성해주세요.")
    elif directory == "":
        msgbox.showwarning("경고", "경로를 설정해주세요.")
    
    # 100개 이상 다운로드 못하게 막음
    elif int(limit) > 100:
        msgbox.showwarning("경고", "100개이상 다운로드는 현재 막혀있습니다.")
        
    elif directory.startswith("C:/") or directory.startswith("D:/") or \
        directory.startswith("E:/") or directory.startswith("F:/") or \
        directory.startswith("G:/") or directory.startswith("H:/") or \
        directory.startswith("I:/") or directory.startswith("J:/"):
        Google_img_crawling_start()
    else:
       msgbox.showwarning("경고", "경로를 제대로 작성해주세요.")
    
def Google_img_crawling_start():
    if not keyword =="" and not limit =="" and not directory =="" and directory[0:3] == "C:/":
        response = google_images_download.googleimagesdownload() 
        arguments = {
            "keywords":keyword,
            "limit":limit,
            "print_urls":True,
            # "chromedriver":"./chromedriver", # 크롬드라이버는 일단 제외
            "format":"jpg",
            "output_directory":directory}
        paths = response.download(arguments)
        msgbox.showinfo("알림", "완료되었습니다.")


# 제목
title_frame = Frame(root)
title = Label(title_frame, text="이미지를 다운로드 하세요", font=("", 15, "bold"), height=3)
title.pack(pady=30)
title_frame.pack()


# Search
# 1. Search 설명
search_explain_frame = Frame(root)
search_explain = Label(search_explain_frame, text="검색할 내용을 작성하세요. ex) 풍선,공룡")
search_explain.pack()
search_explain_frame.pack()

# 2. Search Input
search = Entry(search_explain_frame, width=50)
search.pack()


# Limit_number
# Limit_number 설명
Limit_number_explain_frame = Frame(root)
Limit_number_explain = Label(Limit_number_explain_frame, text="다운로드 받을 이미지 개수")
Limit_number_explain.pack()
Limit_number_explain_frame.pack()

# Limit_number Input
Limit_number = Entry(Limit_number_explain_frame, width=10)
Limit_number.pack()


# 다운로드 경로
# 1. 경로가 적히는 Entry
dir_frame = Frame(root)
dir = Entry(dir_frame, width=50)
dir.pack(pady=15, side="left")
dir_frame.pack(side="top")

# 2. 경로를 선택하는 btn
dir_btn = Button(dir_frame, text="다운로드 경로", command=dir_choice)
dir_btn.pack(pady=15, side="left")

# 크롤링 실행 버튼
crawling_start_frame = Frame(root)
crawling_start = Button(crawling_start_frame, text="실행", font=("", 10, "bold"), height=2, width=7, command=Google_img_crawling)
crawling_start.pack()
crawling_start_frame.pack(side="bottom", ipady=25)

# my name
name_frame = Frame(root)
name_frame1 = Label(name_frame, text="by. I-enable")
name_frame.place(relx=0.88, rely=0.93)
name_frame1.pack()

root.mainloop()
