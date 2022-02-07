import requests
import json

def apiCall(pageNum, numberRows, data_type):
    get_params = {'pageNo': pageNum, 'numOfRows': numberRows, 'type': 'json', 'flag': 'Y'}
    response = requests.get('http://apis.data.go.kr/1741000/DisasterMsg2/getDisasterMsgList?serviceKey=%2FJwrw5VzFtmrEPG4Qf1VmV7i7AdChcU5TVVb6Zs4078mgIJLTAuZ%2F6JF8NMSEc7nD9xWTFVBI3ci7y9TmVOjxw%3D%3D', params=get_params)
    data = json.loads(response.text)
    return dataDetach(data, data_type)

def dataDetach(data, data_type):
    create_date = data["DisasterMsg"][1]["row"][0]["create_date"]
    location_name = data["DisasterMsg"][1]["row"][0]["location_name"]
    md101_sn = data["DisasterMsg"][1]["row"][0]["md101_sn"]
    msg = data["DisasterMsg"][1]["row"][0]["msg"]
    if data_type == 0:
        return create_date, md101_sn
    elif data_type == 1:
        return create_date, location_name, md101_sn, msg