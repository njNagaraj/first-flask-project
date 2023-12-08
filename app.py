from flask import Flask, render_template

app = Flask(__name__)

jobs = [
    {
        'id' : '1',
        'title': 'Python Developer',
        'location': 'Chennai',
        'description': 'A description of the job goes here.'
    },
    {
        'id' : '2',
        'title': 'Web Developer',
        'location': 'Delhi',
        'description': 'A description of the job goes here.'
    },
    {
      'id' : '2',
      'title': 'App Developer',
      'description': 'A description of the job goes here.'
    }
]

@app.route('/')
def home():
  return render_template('home.html',JOBS = jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug = True)