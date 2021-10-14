import json
import random


def lambda_handler(event, context):

    number = random.randint(0, 7)
    if number <= 5:
        print("ame Over ")
        raise Exception("Game Over ")
    else:
        print("good to go you win.........")
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
