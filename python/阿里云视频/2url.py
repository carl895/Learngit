from urllib.request import urlopen,Request

url ='http://www.bing.com'

ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
req = Request(url , headers={
    'User-agent':ua
})
# req.add_header('user-agent',ua)
response = urlopen(req)
print(response.closed)

with response:
    print(type(response))
    print(response.geturl())
    print(response.status)
    print(response._method)

print(response.closed)