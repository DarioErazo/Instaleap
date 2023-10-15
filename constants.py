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

DETAILS_JOB = {
  "job_number": "string",
  "client_id": "string",
  "start_time": "2023-10-08T22:46:59.053Z",
  "end_time": "2023-10-08T22:46:59.053Z",
  "state": "string",
  "origin": {
    "name": "string",
    "address": "string",
    "address_two": "string",
    "country": "string",
    "state": "string",
    "city": "string",
    "zip_code": "string",
    "description": "string",
    "coordinates": {
      "lat": 0,
      "lng": 0
    }
  },
  "destination": {
    "name": "string",
    "address": "string",
    "address_two": "string",
    "country": "string",
    "state": "string",
    "city": "string",
    "zip_code": "string",
    "description": "string",
    "coordinates": {
      "lat": 0,
      "lng": 0
    }
  },
  "total_items": 0,
  "items_replaced": 0,
  "products_cost": {
    "amount": 0,
    "currency_code": "string"
  },
  "items": [
    {
      "id": "string",
      "state": "string",
      "name": "string",
      "package_id": "string",
      "quantity": 0,
      "found_quantity": 0,
      "photo_url": "string",
      "presentation": {
        "quantity": 0,
        "unit": "string",
        "name": "string",
        "price": {
          "amount": 0,
          "currency_code": "string"
        },
        "weight": 0,
        "dimensions": [
          {
            "length": 0,
            "width": 0,
            "height": 0
          }
        ]
      },
      "attributes": {
        "category": "string",
        "another attributes": "string"
      },
      "origin": "string",
      "comment": "string",
      "replaced_by": "string"
    }
  ],
  "collect_with": {
    "method": "string",
    "payment": {
      "amount": 0,
      "currency": "string"
    }
  },
  "recipient": {
    "name": "string",
    "email": "string",
    "phone_number": 0
  },
  "tasks": {
    "id": "string",
    "type": "string",
    "state": "string",
    "resource": "string",
    "payment": "string",
    "steps": [
      {
        "id": "string",
        "state": "string",
        "type": "string"
      }
    ]
  },
  "delivery_options": [
  ],
  "job_comment": "string",
  "external_data": {
    "webhook": {
      "key": "string"
    },
    "backoffice": {
      "key": "string"
    }
  }
}

INSTALEAP_DOMAIN = "https://api.xandar.instaleap.io"

APY_KEY = "API_KEY_TOKEN"