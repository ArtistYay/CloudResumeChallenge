import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCount')
def lambda_handler(event, context):
    response = table.get_item(Key={
       'ID':'0'
    })
    
    return response['Item']['record_count']