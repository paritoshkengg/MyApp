from sqlalchemy import create_engine, text,exc
import os

db_connection_string ="mysql+pymysql://zj9nw57qmk7434pu7n36:pscale_pw_fGBuabExbjJO4vih9V7PkF54IYfd91Avy4q5cWSAjap@aws.connect.psdb.cloud:3306/myapp"
#os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from Employee"))
    jobs = []
    for row in result.all():
        print (row[0])
        jobs.append({"Name": row[1],"Designation":row[3],"Grade":row[4]})
    return jobs

def load_job_from_db(var1):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM Employee WHERE Name = :val"),
      {"val": var1}
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      for row in rows:
        return ({"Name": row[1]})


def add_application_to_db(data):
  with engine.connect() as conn:
    query = text("INSERT INTO Employee (Name,Designation,Grade,EmployeeNumber) VALUES (:full_name,:designation, :grade, :emp_no)")

    try:
        conn.execute(query, {"full_name": data['full_name'], "designation": data['designation'], "grade": data['grade'], "emp_no": data['emp_no']})
        print("Data inserted successfully!")
    except exc.IntegrityError as e:
        print(f"IntegrityError: {str(e)}")
        # Handle the integrity error here
                 
