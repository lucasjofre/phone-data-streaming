import json
import boto3

def lambda_handler(event, context):
    # print the request body to test it
    print(event)
    # Send data to Kinesis Data Stream
    kinesis_client = boto3.client('kinesis', region_name='us-east-1')
    # extract body content
    data = event['body']
    response = kinesis_client.put_record(
        StreamName='phone-data-streaming-DataStream-jTyFNLg0OkgY',
        Data=json.dumps(data),
        PartitionKey='1'
    )

    return {
        'statusCode': 200,
        'body': 'Data sent to Kinesis Data Stream'
    }
