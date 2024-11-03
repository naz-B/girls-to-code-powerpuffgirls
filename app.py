from flask import Flask, render_template
import random

app = Flask(__name__)

if __name__ == '__main__' :
   app.run (debug=True)
    
welcome_msgs = ["Welcome to our portfolio",
"Hello to our portfolio",
"This is our portfolio"]


@app.route('/')
def index():
    random_welcome_msg = random.choice(welcome_msgs)
    return render_template('index.html',welcome_msg=random_welcome_msg)


@app.route('/about')
def about():
    return render_template('about.html', my_name=my_name, my_description=my_description)
@app.route('/projects')
def project_lists():
    return render_template('projects.html', projects=projects)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', contact=my_contact, email=my_email)

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
    
my_name = 'fathimath azha,aishath falak, aishath zehna'
my_description = 'We are humans who is 12 years old'

projects = [
    {"name": "Project 1", "description":"-Our portfolio website project is about us.Whenever you visit our website, you will see our portfolio and you can see our projects."},
    {"name": "Project 2", "description":"-Our portfolio website project is about us.Whenever you need someone to talk to we are here.You can contact us whenever you need us"}]

my_contact = "7982081"
my_email = "azhafathimath389@gmail.com "

     
