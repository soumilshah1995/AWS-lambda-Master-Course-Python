
try:

    import sys
    import os
    import json
    import requests
    print('all module are loaded ')

except Exception as e:

    print("Error : {} ".format(e))


class MakeHttp(object):

    def __init__(self, url):
        self.url = url
        self.headers = {
            'Origin': 'http://fiddle.jshell.net',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': '*/*',
            'Referer': 'http://fiddle.jshell.net/_display/',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
        }

    def get(self):
        try:

            r = requests.get(url=self.url, headers= self.headers)
            r = r.text
            return r

        except Exception as e:
            return {"status":-1,
                    "error":{"message":str(e)}}


class Controller():

    def __init__(self):
        self.ip_finder = "http://api.ipify.org/"

    def run(self):
        helper = MakeHttp(url=self.ip_finder)
        response = helper.get()
        ip  = response
        print("IP->>>>>")
        print(ip)
        return True


def lambda_handler(event=None, context=None):

    instance = Controller()
    instance.run()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }




