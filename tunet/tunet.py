import hashlib
import requests
import re

def get_err(res):
    pattern = re.compile("E\d+")
    arr = pattern.findall(res)
    n = 0
    if arr:
        n = int(arr[0][1:])
    msg = res
    switch = {
        3001: "流量或时长已用尽",
        3002: "计费策略条件不匹配",
        3003: "控制策略条件不匹配",
        3004: "余额不足",
        2531: "用户不存在",
        2532: "两次认证的间隔太短",
        2533: "尝试次数过于频繁",
        2553: "密码错误",
        2601: "不是专用客户端",
        2606: "用户被禁用或无联网权限",
        2611: "MAC绑定错误",
        2613: "NAS PORT绑定错误",
        2616: "余额不足",
        2620: "连接数已满，请登录http://usereg.tsinghua.edu.cn，选择下线您的IP地址。",
        2806: "找不到符合条件的产品",
        2807: "找不到符合条件的计费策略",
        2808: "找不到符合条件的控制策略",
        2833: "IP地址异常，请重新拿地址",
        2840: "校内地址不允许访问外网",
        2841: "IP地址绑定错误",
        2842: "IP地址无需认证可直接上网",
        2843: "IP地址不在IP表中",
        2844: "IP地址在黑名单中，请联系管理员。",
        2901: "第三方接口认证失败"
    }
    return switch.get(n, msg)

def login(name, pwd):
    if name == "":
        print("请填写用户名")
        return

    if pwd == "":
        print("请填写密码")
        return

    ac_id = 1
    host = "http://net.tsinghua.edu.cn/do_login.php"
    md5 = hashlib.md5(pwd.encode()).hexdigest()

    try:
        result = requests.post(host, data = {
            "action": "login",
            "username": name,
            "password": "{MD5_HEX}" + md5,
            "ac_id": "1"})
    except requests.exceptions.RequestException as e:
        print(e)
    else:
        print(get_err(result.text))

def logout():
    host = "http://net.tsinghua.edu.cn/do_login.php"

    try:
        result = requests.post(host, data = {
            "action": "logout"})
    except requests.exceptions.RequestException as e:
        print(e)
    else:
        print(get_err(result.text))

if __name__ == '__main__':
    pass
