import requests
import json
import time

getDataUrl = "http://ndnu-api.ndnulife.com/api/ncov/wechat/check_bind/"
reportUrl = "http://ndnu-api.ndnulife.com/api/ncov/student/report0827/"


class Student:

    def __init__(self, name, sturl):
        self.name = name
        postion = sturl.rfind("session=") + 8
        self.wechat = sturl[postion:]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
            "Content-Type": "application/json",
            "wechat": self.wechat
        }
        self.data = ''
    
    def post(self):
        res = requests.get(url=getDataUrl, headers=self.headers)
        data = json.loads(res.text)['data']
        payload = data['last_data']
        payload['version'] = data['version']
        self.data = payload
        #       print(self.name, "getdata状态码：", res.status_code,
        #             "\n截取last_data后加上version:", payload, "\n")
    
        r = requests.post(url=reportUrl, json=self.data, headers=self.headers)
    
        print("----------------------------------------------------",
              "\nPOST返回：", r.status_code, r.text,
              "\n", self.name + "{}".format("POST成功" if r.status_code == 200 else "！！！提交失败！！！"),
              "\n--------------------------------------------------")


if __name__ == '__main__':
    Stu0 = Student("shh", "http://2019-ncov.ndnulife.com/#/home?session=xxxxxxxx")
    

studentList = [Stu0]

for student in studentList:
    try:
        student.post()
        time.sleep(0.5)

    except:
        print("error!")
