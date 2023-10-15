SLOT_PAYLOAD = {
    "operational_models_priority": ["FULL_SERVICE"],
    "minimum_slot_size": 15,
    "store_reference": "101_FS",
    "currency_code": "COP",
    "origin": {
        "name": "origen",
        "address": "Avenida Carrera 80, 110851 Bogotá, Colombia",
        "latitude": 4.6232316,
        "longitude": -74.16214
    },
    "destination": {
        "name": "destino",
        "address": "Avenida Carrera 80, Kennedy, 110851 Bogotá, Colombia",
        "latitude": 4.6232316,
        "longitude": -74.16214
    },
    "job_items": [
        {
            "quantity_found_limits": {
                "min": 1,
                "max": 10
            },
            "attributes": {
                "category": "Beers",
                "plu": "909090",
                "ean": "['2000125']",
                "location": "casa",
                "picking_index": "123"
            },
            "id": "p01",
            "name": "Corona",
            "unit": "l",
            "sub_unit": "ml",
            "quantity": 1,
            "sub_quantity": 1000,
            "weight": 0,
            "price": 10000
        }
    ]
}

JOB_PAYLOAD = {
    "recipient": {
        "identification": {
            "number": "string",
            "type": "string"
        },
        "name": "DARIO",
        "email": "correo@cliente.com",
        "phone_number": "3118118888"
    },
    "payment_info": {
        "prices": {
            "subtotal": 0,
            "shipping_fee": 0,
            "discounts": 0,
            "taxes": 0,
            "order_value": 500000,
            "attributes": [
                {
                    "type": "SUBTOTAL",
                    "name": "corona",
                    "value": 500000
                }
            ]
        },
        "payment": {
            "method": "CASH",
            "metadata": {
                "newKey": "New Value",
                "newKey-1": "New Value"
            },
            "id": "string",
            "payment_status": "FAILED",
            "reference": "string",
            "value": 0,
            "payment_status_details": "string",
            "method_details": "string",
            "blocking_policy": "CHECKOUT"
        },
        "currency_code": "COP"
    },
    "add_delivery_code": True,
    "contact_less": {
        "comment": "LeaveAtTheDoor",
        "cash_receiver": "DARIO",
        "phone_number": "3118118888"
    },
    "external_data": {
        "webhook": { "newKey": "New Value" },
        "backoffice": { "newKey": "New Value" },
        "shopper_app": { "newKey": "New Value" }
    },
    "job_comment": "string"
}


INSTALEAP_DOMAIN = "https://api.xandar.instaleap.io"

APY_KEY = "API_KEY_TOKEN"