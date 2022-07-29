import base64
import datetime
import json

import requests

if __name__ == '__main__':
    github_data = requests.get("https://api.github.com/repos/cornerstoneJW/-Meeting/contents/condition.json").json()
    content = base64.b64decode(github_data.get("content"))
    github_data_json = json.loads(content)
    advance = github_data_json.get("advance")
    delay = github_data_json.get("delay")
    headers = {'Content-Type': 'application/json'}
    employee_list = ["蒋小波", "张航", "余宗建", "李春龙", "周玉彬"]
    start = datetime.datetime(2022, 7, 27, 0, 0, 0)
    now = datetime.datetime.now()
    diff = now - start
    days = diff.days
    if now.weekday() not in (5, 6):
        if days > 3:
            # 矫正前三天缺失情况
            index = days - ((3+days) // 7)*2
        else:
            index = days
        # 提前一天提醒
        idx = (index+1) % len(employee_list)
        employee = employee_list[idx - advance + delay]
        if now.weekday() == 4:
            data_str = "下周一由"+employee+"同学主持晨会，请做好相关准备～"
        else:
            data_str = "明早由"+employee+"同学主持晨会，请做好相关准备～"
        data = {
            "msgtype": "text",
            "text": {
                "content": data_str
            }
        }

    source = requests.post(url='url', headers=headers, data=json.dumps(data)).json()
