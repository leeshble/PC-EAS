import tkinter
import Alert
import Background
import Setting
import threading

def func_prev():
    conf_date, conf_name, conf_md101_sn, conf_msg = Setting.get_config(3)
    Alert.alert_Screen(conf_date, conf_name, conf_md101_sn, conf_msg, 1)

def func_option():
    Setting.setting_screen()

def func_exit():
    root.quit()
    root.destroy()

if __name__=='__main__':
    root = tkinter.Tk()
    root.title("PC-EAS")
    root.geometry("220x70")
    root.resizable(0, 0)

    mainMenu = tkinter.Menu(root)
    root.config(menu=mainMenu)

    subMenu = tkinter.Menu(mainMenu)
    mainMenu.add_cascade(label="보기", menu=subMenu)
    subMenu.add_command(label="옵션", command=func_option)
    subMenu.add_command(label="이전 경보", command=func_prev)
    subMenu.add_separator()
    subMenu.add_command(label="종료", command=func_exit)

    mainImage=tkinter.PhotoImage(file="main.png")
    mainLabel=tkinter.Label(root, image=mainImage).pack()

    th = threading.Thread(target=Background.background, name="[Daemon]")
    th.setDaemon(True)
    th.start()

    root.mainloop()