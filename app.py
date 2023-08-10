from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location': 'Lagos, Nigeria',
    'salary': '$80,000'
  },
    {
    'id':2,
    'title':'Data Scientist',
    'location': 'Enugu State, Nigeria',
    'salary': '$180,000'
  },
    {
    'id':3,
    'title':'DevOps Engineer',
    'location': 'Florida, USA',
    'salary': '$120,000'
  },
    {
    'id':4,
    'title':'Cloud Engineer',
    'location': 'Remote',
    
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                        jobs=JOBS,
                        company_name='Montego')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug=True)