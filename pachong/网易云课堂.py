import urllib.request
import urllib.error
import urllib.response
import urllib.parse
import urllib.robotparser
import ssl
import requests
import time
import json

def get_json(index):
    print(f"正在抓取{index}页数据")
    payload = {"pageIndex": index,
               "pageSize": 50,
               "relativeOffset": 50,
               "frontCategoryId": -1,
               "searchTimeType": -1,
               "orderType": 50,
               "priceType": -1,
               "activityId": 0,
               "keyword": ""
               }
    headers = {"Accept": "application/json",
               "Host": "study.163.com",
               "Origin": "https://study.163.com",
               "Content-Type": "application/json",
               "Referer": "https://study.163.com/courses",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
               }
    try:
        # 请注意这个地方发送的是post请求
        # CSDN 博客 梦想橡皮擦
        res = requests.post("https://study.163.com/p/search/studycourse.json", data=json.dumps(payload), headers=headers)
        content_json = res.json()
        if content_json and content_json["code"] == 0:
            data = get_content(content_json)  # 获取正确的数据

            ############################################
            if len(data) > 0:
                print(data)
            ############################################


    except Exception as e:
        print("出现BUG了")
        print(e)
    finally:
        time.sleep(1)
        index += 1
        get_json(index)


def get_content(content_json):
    if "result" in content_json:
        return content_json["result"]["list"]


if __name__ == '__main__':
    get_json(1)