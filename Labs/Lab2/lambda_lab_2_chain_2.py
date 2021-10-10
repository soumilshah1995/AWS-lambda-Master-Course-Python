import json

def lambda_handler(event, context):

    print("Iam lambda 2")


    print(event)


    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
