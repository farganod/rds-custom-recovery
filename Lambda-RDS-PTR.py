import json
import boto3

def lambda_handler(event, context):
    rds = boto3.client("rds")
    db_arn = event["detail"]["SourceArn"]
    arn_array = db_arn.split(":")
    db_identifier = arn_array[6]
    print (db_identifier)
    
    response = rds.restore_db_instance_to_point_in_time(
        SourceDBInstanceAutomatedBackupsArn = "arn:aws:rds:us-east-2:175039216299:auto-backup:ab-6pf6xquzm6prrhroxlim2ncs5i4cakk3734iply",
        TargetDBInstanceIdentifier=db_identifier,
        UseLatestRestorableTime=True,
        DBInstanceClass='db.m5.xlarge',
        Port=1433,
        AvailabilityZone='us-east-2b',
        DBSubnetGroupName='default',
        MultiAZ= False,
        CustomIamInstanceProfile='AWSRDSCustom',
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
