import tkinter
import webbrowser
import winsound as ws

def beepsound():
    freq = 2000
    dur = 1000
    ws.Beep(freq, dur)
def open_web():
    webbrowser.open("http://www.safekorea.go.kr", 1)

def alert_Screen(create_date, location_name, md101_sn, msg, is_test):
    root = tkinter.Tk()
    if is_test == 0:
        root.title("재난 경보")
        beepsound()
    else:
        root.title("이전 재난 경보")
    root.geometry("400x150-100-100")
    root.resizable(0, 0)

    date_label = tkinter.Label(root, text="날짜: %s" % create_date, width=20, anchor="w").pack(fill="both")

    sn_label = tkinter.Label(root, text="일련번호: %s" % md101_sn, width=20, anchor="w").pack(fill="both")

    location_label = tkinter.Label(root, text="지역: %s" % location_name, wraplength=400, anchor="w").pack(fill="both")

    msg_label = tkinter.Label(root, text="메시지: %s" % msg, wraplength=400, justify="left").pack(fill="both")

    link_button = tkinter.Button(root, text="국민재난안전포털", command=open_web).pack(padx=10, pady=10)

    root.mainloop()