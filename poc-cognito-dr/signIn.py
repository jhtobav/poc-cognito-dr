import json


def generate_response(event, status, body, headers={}):

    bodyevent = str(event.get('body'))
    bodyevent = json.loads(bodyevent)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "username": bodyevent.get('username'),
        "password": bodyevent.get('password')
    }

    return {
        "statusCode": status,
        "body": json.dumps(body),
        "headers": headers
    }


def endpoint_signIn(event, context):
    return generate_response(event, 200, {"status": True})
