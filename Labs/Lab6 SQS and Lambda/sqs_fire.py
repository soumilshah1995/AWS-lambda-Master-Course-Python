try:

    import sys
    import os
    import json
    import uuid
    import random
    import boto3
    print('all module are loaded ')
except Exception as e:
    print("Error : {} ".format(e))


global AWS_ACCESS_KEY
global AWS_SECRET_KEY
global AWS_REGION_NAME

AWS_ACCESS_KEY = "XXXXXXXXXXXXXXXXX"
AWS_SECRET_KEY ="XXXXXXXXXXXXXXXXXXX"
AWS_REGION_NAME = "us-east-1"

AWS_SQS_QUEUE_NAME = "XXXXXXXXXXX"

class SQSQueue(object):

    def __init__(self, queueName=None):
        self.resource = boto3.resource('sqs', region_name='us-east-1',
                                       aws_access_key_id=AWS_ACCESS_KEY,
                                       aws_secret_access_key=AWS_SECRET_KEY)

        self.queue = self.resource.get_queue_by_name(QueueName=AWS_SQS_QUEUE_NAME)
        self.QueueName = queueName

    def send(self, Message={}):
        data = json.dumps(Message)
        response = self.queue.send_message(MessageBody=data)
        return response

    def receive(self):
        try:
            queue = self.resource.get_queue_by_name(QueueName=self.QueueName)
            for message in queue.receive_messages():
                data = message.body
                data = json.loads(data)
                message.delete()
        except Exception:
            print(e)
            return []
        return data


def lambda_handler(event=None, context=None):

    companies =["Jobtarget", "google", "amazon", "soumil company"]

    for c, company in enumerate(companies):
        print(company)
        data = {
            "company":company,
        }
        q = SQSQueue(queueName=AWS_SQS_QUEUE_NAME)
        response = q.send(Message=data)
        print("response",c, response)


