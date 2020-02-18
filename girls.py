import requests
import re

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
response = requests.get("https://www.vmgirls.com/9456.html",headers=headers)
html = response.text
print(html)

result = re.findall('<img alt=".*?" src=".*?" width=".*?" height=".*?" class=".*?" data-src="(.*?)" data-nclazyload=".*?">',html)
print(result)
n=0
for url in result:
    file_name = str(n+1)+'.jpg'
    n=n+1
    response = requests.get(url,headers=headers)
    with open(file_name,'wb') as f:
        f.write(response.content)