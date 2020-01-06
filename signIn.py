import json


def generate_response(status, body, headers={}):
    return {
        "statusCode": status,
        "body": json.dumps(body),
        "headers": headers
    }


def endpoint_signIn(event, context):
    return generate_response(200, {"status": True})
