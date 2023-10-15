import os
import uuid 
import json as json_alias
from datetime import datetime, timedelta
import requests 
from constants import (
    INSTALEAP_DOMAIN, 
    JOB_PAYLOAD, 
    SLOT_PAYLOAD, 
    APY_KEY,
    DETAILS_JOB
)


def get_avaibility():

    url = f"{INSTALEAP_DOMAIN}/jobs/availability/v2"

    headers = {
        "x-api-key": os.environ.get(APY_KEY)
    }

    times_to_slots = {
        "start": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "end": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    SLOT_PAYLOAD.update(times_to_slots)

    response = requests.post(url, json=SLOT_PAYLOAD, headers=headers)
    print(response)
    response.raise_for_status()
    # TODO: control de excepciones

    return response.json()

def create_job(slot_id):

    url = f"{INSTALEAP_DOMAIN}/jobs"

    try:

        headers = {
            "x-api-key": os.environ.get(APY_KEY)
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

def details_job(id):

    url = f"{INSTALEAP_DOMAIN}/jobs/{id}"

    try:

        headers = {
            "x-api-key": os.environ.get(APY_KEY)
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


def update_json(amount, job_data):
    data = job_data.replace("'", '"').replace("None", '"None"')
    json_data = json_alias.loads(data)
    job_id = json_data["id"]   
    del json_data['invoice']
    del json_data['id']    
    if not amount:
        # El campo "amount" está vacío, puedes manejar esto como desees
        print("El campo 'amount' está vacío. Por tanto no se actualizaran valores." )
    else:
        amount = int(amount)
        if 'payment' in json_data:
            json_data['payment']['value'] = amount
    return job_id, json_data

def update_job(job_id, data_json):

    url = f"{INSTALEAP_DOMAIN}/jobs/{job_id}/payment_info"

    try:

        headers = {
            "x-api-key": os.environ.get(APY_KEY)
        }
    
        response = requests.put(url, json=data_json, headers=headers)
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

