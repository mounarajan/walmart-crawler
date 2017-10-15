import requests

def requests_lib(url):
   
    pass_count = 0
    count = 0
    while pass_count == 0:
        
        count = count + 1
        

        user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'
        headers = {'User-Agent': user_agent}
        data = requests.get(url,headers = headers)
        data = data.text.encode('utf-8')
        if count > 10:
            pass_count = 1
            data = ''
        return data

def requests_lib_prod(url):
   
    pass_count = 0
    count = 0
    while pass_count == 0:
        
        count = count + 1
        

        user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'
        headers = {'User-Agent': user_agent}
        data = requests.get(url,headers = headers)
        data = data.text.encode('utf-8')
        if count > 10:
            pass_count = 1
            data = ''
        return data