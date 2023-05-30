from tokenize import Name
from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)

@app.route("/")
def home_page():
  jobs = load_jobs_from_db()
  #print(jobs)
  return render_template('home.html',jobs=jobs,company_name='Paritosh')
  #

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/Apply")
def show_job(Name):
  job = load_job_from_db(Name)
  print(job)
  if not job:
    return "Not Found", 404
  
  return render_template('jobpage.html', 
                         job=job)

@app.route("/api/job/<Name>")
def show_job_json(Name):
  job = load_job_from_db(Name)
  return jsonify(job)

@app.route("/job/<Name>/apply", methods=['post'])
def apply_to_job(Name):
  data = request.form
  #job = load_job_from_db(Name)
  add_application_to_db(data)
  return render_template('application_submitted.html', 
                         application=data)


if __name__ == '__main__':
  app.run(host='0.0.0.0',port='5000',debug=True)
