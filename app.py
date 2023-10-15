from flask import Flask, render_template, request

from external_requests import (
    get_availability, 
    create_job, 
    details_job,
    update_job
)

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """redirect to home page"""
    return render_template('home.html')


@app.route('/slots', methods = ['POST'])
def slot_view() -> str:
     """Get available slots"""
     response = get_availability()
     return render_template("availability_table.html", data=response)

      
@app.route('/jobs', methods = ["POST"])
def def_job() -> str:
        """Create Jobs"""
        slot_id = request.form.get('slot_id')
        response = create_job(slot_id)
        return render_template("job_created.html", data=response)


@app.route('/jobs/details/<string:job_id>', methods = ["GET"])
def details(job_id) -> str:
     """List job details"""
     response = details_job(job_id)
     response["payment_info"]["id"] = job_id
     return render_template("details.html", data=response, items=response["items"])


@app.route('/jobs/update/<string:job_id>', methods = ["POST"])
def update(job_id) -> str:
     """Update payment job"""
     #TODO: amount no puede ir vacio
     amount = request.form.get('amount')
     job_info = request.form.get('payment_info')
     response = update_job(job_info, amount)
     return render_template("payment_details.html", data=response)


if __name__ == "__main__":
    app.run(port = 9000, debug=True)
