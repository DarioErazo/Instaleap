import os
import uuid
from typing import Dict, Tuple
import json
from datetime import datetime, timedelta
import requests 
from constants import (
    INSTALEAP_DOMAIN, 
    JOB_PAYLOAD, 
    SLOT_PAYLOAD, 
    APY_KEY
)

API_TOKEN_KEY = os.environ.get(APY_KEY)

def get_availability() -> Dict:
    """Post to view availe slots"""
    url = f"{INSTALEAP_DOMAIN}/jobs/availability/v2"

    headers = {
        "x-api-key": API_TOKEN_KEY
    }

    times_to_slots = {
        "start": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "end": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    SLOT_PAYLOAD.update(times_to_slots)

    response = requests.post(url, json=SLOT_PAYLOAD, headers=headers)
    response.raise_for_status()
    #TODO: CONTROL DE EXCEPTIONS
    return response.json()

def create_job(slot_id: str) -> Dict:
    """Create job using a slot id"""
    url = f"{INSTALEAP_DOMAIN}/jobs"

    try:

        headers = {
            "x-api-key": API_TOKEN_KEY
        }

        slot_info = {
            "slot_id": slot_id,
            "client_reference": str(uuid.uuid4()),
        }

        JOB_PAYLOAD.update(slot_info)

        response = requests.post(url, json=JOB_PAYLOAD, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Error en la solicitud: {err}")
        print(f"Contenido de la respuesta de error: {response.text}")
    except requests.exceptions.ConnectionError as err:
        print(f"Error de conexión: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error en la solicitud: {err}")
    except ValueError as err:
        print(f"Error en el método HTTP: {err}")
    except Exception as err:
        print(f"Error desconocido: {err}")

def details_job(id: str) -> Dict:
    """Get details job using id"""
    url = f"{INSTALEAP_DOMAIN}/jobs/{id}"

    try:

        headers = {
            "x-api-key": API_TOKEN_KEY
        }
    
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Error en la solicitud: {err}")
        print(f"Contenido de la respuesta de error: {response.text}")
        a = {
            "content_response": response,
            "error_text": response.text
        }
        return a
    except requests.exceptions.ConnectionError as err:
        print(f"Error de conexión: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error en la solicitud: {err}")
    except ValueError as err:
        print(f"Error en el método HTTP: {err}")
    except Exception as err:
        print(f"Error desconocido: {err}")


#TODO: LLEVAR A UN ARCHIVO DE UTILS
def make_body(amount: str, job_data: str) -> Tuple[Dict, str]:
    """Build json to update pyment Job"""
    data = job_data.replace("'", '"').replace("None", '"None"')
    json_data = json.loads(data)
    job_id = json_data.pop("id")
    json_data.pop("invoice")
    json_data["payment"]["value"] = int(amount)
    return job_id, json_data

def update_job(payload: str, new_amount: int) -> Dict:
    """Update payment Job"""
    job_id, json_body = make_body(
        amount=new_amount, 
        job_data=payload
    )

    url = f"{INSTALEAP_DOMAIN}/jobs/{job_id}/payment_info"

    try:

        headers = {
            "x-api-key": API_TOKEN_KEY
        }
    
        response = requests.put(url, json=json_body, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Contenido de la respuesta de error: {response.text}")
    except requests.exceptions.ConnectionError as err:
        print(f"Error de conexión: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error en la solicitud: {err}")
    except ValueError as err:
        print(f"Error en el método HTTP: {err}")
    except Exception as err:
        print(f"Error desconocido: {err}")
