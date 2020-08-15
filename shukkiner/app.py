import json, os, decimal, uuid
from datetime import datetime, timezone
import boto3


ddb = boto3.resource("dynamodb")
table = ddb.Table(os.environ["TABLE_NAME"])


HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Content-Type": "application/json; charset=UTF-8",
}

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


def get_shukkin(event, context):
    """
    GET /shukkin
    """
    try:
        response = table.scan()

        status_code = 200
        resp = response.get("Items")
    except Exception as e:
        status_code = 500
        resp = {
            "error_message": str(e)
        }

    return {
        "statusCode": status_code,
        "headers": HEADERS,
        "body": json.dumps(resp, cls=DecimalEncoder),
    }


def post_shukkin(event, context):
    """
    POST /shukkin
    """
    try:
        body = event.get("body")
        if not body:
            raise ValueError("bodyをheaderにｼｭｳｳｳｳｳｳｳｳｳｳ!!")
        body = json.loads(body)

        for key in ["username", "place", "leaving_expected_time"]:
            if not body.get(key):
                raise ValueError(f"{key}をbodyにｼｭｳｳｳｳｳｳｳｳｳｳ!!")

        record = {
            "item_id": uuid.uuid4().hex,
            "username": body["username"],
            "place": body["place"],
            "leaving_expected_time": body["leaving_expected_time"],
            "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        response = table.put_item(Item=record)

        status_code = 201
        resp = {"message": "しゅっきん！"}
    except ValueError as e:
        status_code = 400
        resp = {"error_message": str(e)}
    except Exception as e:
        status_code = 500
        resp = {"error_message": str(e)}

    return {
        "statusCode": status_code,
        "headers": HEADERS,
        "body": json.dumps(resp),
    }


def patch_shukkin(event, context):
    """
    PATCH /shukkin/{item_id}
    """
    try:
        path_params = event.get("pathParameters", {})
        item_id = path_params.get("item_id", "")
        if not item_id:
            raise ValueError("退社失敗！！！！！(item_idがないよ)")

        response = table.update_item(
            Key={"item_id": item_id},
            UpdateExpression=f"SET leaved_at = :l",
            ExpressionAttributeValues={
                ":l": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            },
        )

        status_code = 200
        resp = {"message": "たいしゃっ！！！！！！！"}
    except ValueError as e:
        status_code = 400
        resp = {"error_message": str(e)}
    except Exception as e:
        status_code = 500
        resp = {"error_message": str(e)}
    
    return {
        "statusCode": status_code,
        "headers": HEADERS,
        "body": json.dumps(resp)
    }


def delete_shukkin(event, context):
    """
    DELETE /shukkin/{item_id}
    """
    try:
        path_params = event.get("pathParameters", {})
        item_id = path_params.get("item_id", "")
        if not item_id:
            raise ValueError("item_idが不正だよ")

        response = table.delete_item(
            Key={"item_id": item_id}
        )

        status_code = 200
        resp = {"message": "出勤を取り消しました(血涙)"}
    except ValueError as e:
        status_code = 400
        resp = {"error_message": str(e)}
    except Exception as e:
        status_code = 500
        resp = {"error_message": str(e)}

    return {
        "statusCode": status_code,
        "headers": HEADERS,
        "body": json.dumps(resp)
    }
