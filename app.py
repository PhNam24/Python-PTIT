import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image, ImageTk
import main


# --------------------------------------------------------------------------------------#


def home_page():
    home_screen.pack()
    main_screen.pack_forget()


def main_page():
    main_screen.pack()
    home_screen.pack_forget()


def browse_files():
    filenames = filedialog.askopenfilenames(initialdir="/",
                                            title="Select Files",
                                            filetypes=(("AndroidManifest",
                                                        "*.xml*"),
                                                       ("all files",
                                                        "*.*")))
    if len(filenames) == 0:
        messagebox.showerror("Error!!!", "No file selected!")
    else:
        for i in filenames:
            tmp = i.split("/")
            tmp1 = tmp[len(tmp) - 1].split(".")
            if tmp1[len(tmp1) - 1] != "xml":
                messagebox.showerror("Error!!!", "Wrong file format!\nPlease select xml file!")
                return
        files_list.configure(state="normal")
        font = ctk.CTkFont(family="Lexend", size=16, weight="normal")
        files_list.configure(font=font)
        if files_list.get("0.0", "end") == "No file selected\n":
            files_list.delete("0.0", "end")
        line = len(path) + 1
        for i in range(len(filenames)):
            path.append(filenames[i])
            get_path = filenames[i].split("/")
            filename = get_path[len(get_path) - 2] + "/" + get_path[len(get_path) - 1]
            files_list.insert(f"{line}.0", str(line) + " " + filename + "\n")
            line += 1


def process():
    files_list.configure(state="disabled")
    if len(path) == 0:
        messagebox.showerror("Error!!!", "No file selected!")
    else:
        result = main.process(path)
        res_list.configure(state="normal")
        font = ctk.CTkFont(family="Lexend", size=16, weight="normal")
        res_list.configure(font=font)
        res_list.delete("0.0", "end")
        line = 1
        for i in range(len(result)):
            res_list.insert(f"{line}.0", "File " + str(line) + " is " + result[i] + "\n")
            line += 1
    res_list.configure(state="disabled")
    path.clear()


def reset():
    path.clear()
    files_list.configure(state="normal")
    files_list.delete("0.0", "end")
    files_list.insert("0.0", "No file selected")
    files_list.configure(state="disable")
    res_list.configure(state="normal")
    res_list.delete("0.0", "end")
    res_list.insert("0.0", "No file selected")
    res_list.configure(state="disable")


# --------------------------------------------------------------------------------------#


# Khởi tạo cửa sổ
app = tk.Tk()
app.title("Android Malware Detection GUI App")
app.geometry("960x540")
app.resizable(width=False, height=False)

# ---------------------------------------------------------------------------------------#


# Home Screen

home_screen = tk.Frame(app, height=540, width=960)

## Home Background
home_bg_img = ImageTk.PhotoImage(Image.open("assets/img/background/home_bg.jpg").resize((960, 540)))
home_bg = tk.Label(home_screen, image=home_bg_img)
home_bg.pack()

## Logo PTIT
logo_img = ImageTk.PhotoImage(Image.open("assets/img/logo_ptit/logo1.png").resize((60, 77)))
logo = tk.Label(home_screen, image=logo_img, bg="#081243")
logo.place(relx=0.05, rely=0.05, anchor=NW)

## Tên HV + tên nhóm + chủ đề

### HV
font1 = ctk.CTkFont(family="Lexend Medium", size=30, weight="normal")
hv = tk.Label(home_screen, text="Học viên Công nghệ Bưu Chính Viễn thông", font=font1, fg="white", bg="#020517")
hv.place(relx=0.5, rely=0.08, anchor=N)

### Nhóm + chủ đề + gv
font1 = ctk.CTkFont(family="Lexend", size=27, weight="normal")
gr_name = tk.Label(home_screen, text="BTL Nhóm 5", font=font1, fg="white", bg="#081041")
gr_name.place(relx=0.05, rely=0.25, anchor=NW)

font1 = ctk.CTkFont(family="Lexend Light", size=20, weight="normal")
topic = tk.Label(home_screen, text="Chủ đề: Phát hiện mã độc Android dựa vào phân tích quyền truy cập của ứng dụng",
                 font=font1, fg="white", bg="#0F204B")
topic.place(relx=0.05, rely=0.33, anchor=NW)

gv = tk.Label(home_screen, text="Giảng viên: Thầy Vũ Minh Mạnh", font=font1, fg="white", bg="#091344")
gv.place(relx=0.05, rely=0.4, anchor=NW)

### Thành viên
name = ["Phạm Hoài Nam", "Đàm Tiến Quân", "Cam Hải Đăng", "Nguyễn Đình Văn"]
msv = ["B21DCCN554", "B21DCCN604", "B21DCCN027", "B21DCCN784"]

tv = tk.Label(home_screen, text="Thành viên nhóm:", font=font1, fg="white", bg="#06094e")
tv.place(relx=0.05, rely=0.5, anchor=NW)

font1 = ctk.CTkFont(family="Lexend Light", size=20, weight="normal")
for i in range(4):
    name_lb = tk.Label(home_screen, text=name[i], font=font1, fg="#dee1e3", bg="#06094e")
    name_lb.place(relx=0.05, rely=0.6 + i * 0.075, anchor=NW)
    msv_lb = tk.Label(home_screen, text=msv[i], font=font1, fg="#dee1e3", bg="#06094e")
    msv_lb.place(relx=0.25, rely=0.6 + i * 0.075, anchor=NW)

## Start Button
start_btn_img = ImageTk.PhotoImage(Image.open("assets/img/button/Start_btn.png").resize((139, 49)))
start_btn = tk.Button(image=start_btn_img, bg="#091255", borderwidth=0, activebackground="#091255", command=main_page)
start_btn.place(relx=0.95, rely=0.9, anchor=SE)

# Main Screen

main_screen = tk.Frame(app, height=540, width=960)

## Main Background
main_bg_img = ImageTk.PhotoImage(Image.open("assets/img/background/main_bg.jpg").resize((960, 540)))
main_bg = tk.Label(main_screen, image=main_bg_img)
main_bg.pack()

## Home Button
home_btn_img = ImageTk.PhotoImage(Image.open("assets/img/button/Home_btn.png").resize((59, 60)))
home_btn = tk.Button(main_screen, image=home_btn_img, bg="#060411", borderwidth=0, activebackground="#060411",
                     command=home_page)
home_btn.place(relx=0.05, rely=0.05, anchor=NW)

## Browse Files
font1 = ctk.CTkFont(family="Lexend", size=24, weight="normal")
browse_files_label = tk.Label(main_screen, text="Browse Files", font=font1, fg="white", bg="#02030c")
browse_files_label.place(relx=0.16, rely=0.12, anchor=NW)

font1 = ctk.CTkFont(family="Lexend", size=20, weight="normal")
files_list = ctk.CTkTextbox(main_screen, height=300, width=360, corner_radius=0, font=font1)
files_list.place(relx=0.05, rely=0.32, anchor=NW)
files_list.insert("0.0", "No file selected")
files_list.configure(state="disabled")

font1 = ctk.CTkFont(family="Lexend", size=16, weight="normal")
browse_files_btn = tk.Button(main_screen, text="Select your files", font=font1, borderwidth=0, command=browse_files)
browse_files_btn.place(relx=0.17, rely=0.22, anchor=NW)

path = []

## Result
font1 = ctk.CTkFont(family="Lexend", size=24, weight="normal")
result_label = tk.Label(main_screen, text="Results", font=font1, fg="white", bg="#13272c")
result_label.place(relx=0.81, rely=0.12, anchor=NE)

font1 = ctk.CTkFont(family="Lexend", size=16, weight="normal")
get_res_btn = tk.Button(main_screen, text="Get results", font=font1, borderwidth=0, command=process)
get_res_btn.place(relx=0.815, rely=0.22, anchor=NE)

font1 = ctk.CTkFont(family="Lexend", size=20, weight="normal")
res_list = ctk.CTkTextbox(main_screen, height=300, width=360, corner_radius=0, font=font1)
res_list.place(relx=0.95, rely=0.32, anchor=NE)
res_list.insert("0.0", "No file selected")
res_list.configure(state="disabled")

## Reset
font1 = ctk.CTkFont(family="Lexend", size=16, weight="normal")
reset_btn = tk.Button(main_screen, text="Reset All", font=font1, command=reset)
reset_btn.place(relx=0.5, rely=0.9, anchor=N)
# --------------------------------------------------------------------------------------#

# Khởi chạy ứng dụng
home_page()
app.mainloop()
