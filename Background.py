import sys
import time
import Alert
import ApiControl
import datetime
import Setting

def date_split(create_date):
    ymd_hms = create_date.split(' ')
    ymd = ymd_hms[0].split('/')
    hms = ymd_hms[1].split(':')
    return ymd, hms


def date_match(ymd, hms):
    now = datetime.datetime.now()
    if ymd[0] == now.strftime('%y') and ymd[1] == now.strftime('%m') and ymd[2] == now.strftime('%d'):
        if hms[0] == now.strftime('%H') and int(ymd[1]) <= now.minute:
            result = 1
    else:
        result = 0
    return result


def background():
    while True:
        create_date, location_name, md101_sn, msg = ApiControl.apiCall(1, 1, 1)
        conf_date, conf_name, conf_md101_sn, conf_msg = Setting.get_config(3)
        if md101_sn != conf_md101_sn:
            user_location = Setting.get_config(0)
            if location_name in user_location:
                if create_date != conf_date:
                    ymd, hms = date_split("2019/06/03 01:32:25")
                    print(date_match(ymd, hms))
                    if date_match(ymd, hms) == 1:
                        Alert.alert_Screen(create_date, location_name, md101_sn, msg, 0)
                        Setting.set_else(create_date, location_name, md101_sn, msg)
        time.sleep(60)
