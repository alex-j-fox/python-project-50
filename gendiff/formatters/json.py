import json


def make_json(data: [dict, any]) -> str:
    return json.dumps(data, indent=4)
