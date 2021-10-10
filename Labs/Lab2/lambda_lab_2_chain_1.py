import json
import boto3


client = boto3.client('lambda')

def lambda_handler(event, context):

    message = {"message":"Hello from Lamdba 1 "}

    response = client.invoke(
        FunctionName='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        InvocationType='RequestResponse',
        Payload=json.dumps(message),
    )

    print(response)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
