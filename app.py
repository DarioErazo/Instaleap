from flask import Flask, render_template, request, jsonify
from flask_session import Session
import requests as req

from external_requests import get_avaibility, create_job, details_job, update_json, update_job

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/slots', methods = ['POST', 'GET'])
def slot_view():
    if request.method == "POST":
        response = get_avaibility()
        return render_template("availability_table.html", data=response)
      
@app.route('/jobs', methods = ["POST"])
def def_job():
        slot_id = request.form.get('slot_id')
        client_id = request.form.get('client_id')
        response = create_job(slot_id)
        return render_template("job_created.html", data=response)

@app.route('/job/search', methods = ['POST', 'GET'])
def search():
     return render_template("Job_search_client.html")
     
@app.route('/jobs/details/<string:job_id>', methods = ["GET"])
def details(job_id):
     response = details_job(job_id)
     response["payment_info"]["id"] = job_id
     return render_template("details.html", data=response, items=response["items"])

@app.route('/jobs/update/<string:job_id>', methods = ["POST"])
def update(job_id):
     amount = request.form.get('amount')
     job_info = request.form.get('payment_info')
     job_number, data = update_json(amount, job_info)
     print("-------  Imprimir desde el principal  -------")
     print(data)
     response = update_job(job_number, data)
     print("-------  Imprimiendo EL RESPONSE  -------")
     print(response)
     print(type(response))
     #print(response.status_code)
     return render_template("payment_details.html", data=response)


if __name__ == "__main__":
    app.run(port = 9000, debug=True)
