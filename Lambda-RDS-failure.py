import json
import boto3

def lambda_handler(event, context):
    rds = boto3.client("rds")
    db_arn = event["detail"]["SourceArn"]
    arn_array = db_arn.split(":")
    db_identifier = arn_array[6]
    print (db_identifier)
    
    response = rds.modify_db_instance(
        DBInstanceIdentifier=db_identifier,
        DeletionProtection=False,

    )
    
    response = rds.delete_db_instance(
        DBInstanceIdentifier=db_identifier,
        SkipFinalSnapshot=True,
        DeleteAutomatedBackups=False
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
