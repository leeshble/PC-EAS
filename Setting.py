from tkinter import *
from tkinter import ttk
from ApiControl import apiCall
from collections import OrderedDict
import json

def set_city(city_data):
    data = OrderedDict()
    data["user_info"]={'CITY_NAME':city_data}
    with open('config2.json', 'w') as make_file:
        json.dump(data, make_file, ensure_ascii=False, indent="\t")
    print("set_city(%s) done"%city_data)

def set_else(create_date, location_name, md101_sn, msg):
    data = OrderedDict()

    data["last_alert"]={'create_date':create_date, 'location_name':location_name, "md101_sn":md101_sn,"msg":msg}

    with open('config.json', 'w') as make_file:
        json.dump(data,make_file, ensure_ascii=False, indent="\t")
    print("set_else() done")

def get_config(data_type) :
    jstring = open("config.json", "r").read()
    data = json.loads(jstring)

    if data_type == 0:
        jstring2 = open("config2.json", "r").read()
        data2 = json.loads(jstring2)
        city_name = data2["user_info"]["CITY_NAME"]
        print("get_config(0)done")
        return city_name

    elif data_type == 1:
        create_date = data["last_alert"]["create_date"]
        print("get_config(1)done")
        return create_date

    elif data_type == 2:
        md101_sn = data["last_alert"]["md101_sn"]
        print("get_config(2)done")
        return md101_sn

    elif data_type == 3:
        create_date = data["last_alert"]["create_date"]
        location_name = data["last_alert"]["location_name"]
        md101_sn = data["last_alert"]["md101_sn"]
        msg = data["last_alert"]["msg"]
        if create_date == "null":
            create_date, location_name, md101_sn, msg = apiCall(1, 1, 1)
            set_else(create_date, location_name, md101_sn, msg)
        print("get_config(3)done")
        return create_date, location_name, md101_sn, msg

def setting_screen() :
    root = Tk()
    root.title("옵션")
    root.geometry("222x100")
    root.resizable(0, 0)

    def btn_click():
        city_data = combo_value.get()
        print(city_data)
        set_city(city_data)

    combo_value = StringVar()
    city_combo = ttk.Combobox(root, width=20, textvariable=combo_value)
    city_combo['values'] = ('서울특별시', '인천광역시', '경기도', '강원도', '대전광역시', '세종특별자치시', '강원도', '충청남도', '충청북도', '전라북도', '광주광역시', '전라남도', '광주광역시', '경상북도', '대구광역시', '울산광역시', '경상남도', '부산광역시', '제주특별자치도')

    city_combo.grid(column=0, row=0)
    city_combo.current(0)

    save_button = Button(root, text="옵션저장", command=btn_click)
    save_button.grid(column=1, row=0)

    current_label = ttk.Label(root, text="현재 위치는 %s 입니다." % get_config(0))
    current_label.grid(column=0, row=1, rowspan=2)

    location_name_label = Label(root, text="Copyrightⓒ2019\n컴퓨터공학과 201935308 이상현\nAll rights reserved.", height=5)
    location_name_label.grid(column=0, row=2, columnspan=2)

    root.mainloop()