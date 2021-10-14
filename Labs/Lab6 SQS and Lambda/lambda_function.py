
try:

    import sys
    import os
    import json
    import uuid
    import boto3
    print('all module are loaded ')

except Exception as e:

    print("Error : {} ".format(e))


def lambda_handler(event=None, context=None):

    data = event.get("Records")[0].get("body")
    data = json.loads(data)
    event = data
    print("--------->>>>>>>>")
    print(event)

    return "ok"




