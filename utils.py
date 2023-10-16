import json
from typing import Dict, Tuple

def make_body(amount: str, job_data: str) -> Tuple[Dict, str]:
    """Build json to update pyment Job"""
    data = job_data.replace("'", '"').replace("None", '"None"')
    json_data = json.loads(data)
    job_id = json_data.pop("id")
    json_data.pop("invoice")
    json_data["payment"]["value"] = int(amount)
    return job_id, json_data