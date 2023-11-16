from flask import Flask, render_template, jsonify, request
import sqlite3
from flask import LoginManager, UserMixin, login_user, login_required, logout_user, url_for


app = Flask(__name__)
DB_FILE = "../historian_data.db"
CONFIG_FILE = "../config.jsaon"

app.secret_key='your_secret_key' #Change this to any string
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app) #bind to the application

#hardcore
users = {
   "admin":"12345"
}

#Create the user mixin to work with our application
class User(UserMixin):
   def __init__(self, username):
      self.id = username

@login_manager.user_loader
def load_user(user_id):
   return User(user_id)


@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('index'))

@app.route('/login',methods=['GET','POST'])
def login():
   if request.method=='POST': #form to submit 
      username = request.form.get('username') #POST data
      formPassword = request.form.get('password')
      #handle the "next" parameter which gets the user back to the correct page
      next = request.args.get('next')
      DBPassword = user.get(username)
      if DBPassword == formPassword: 
         user = User(username)
         login_user(user)
         return redirect(next) #Redirect to the user to the resource they were requesting
   return render_template('login.html')
         
  

#load jsonfile
with open(CONFIG_FILE, 'r') as config_file:
   config_data = json.load(confige_file)

@app.route('/',methods=['GET'])
#Web page
def main():
  return render_template ('index.html')

#Serving up stuff 
@app.route('/configure',methogds=['GET'])
def configure():
  return render_template('configure HMTL')
  
#Return some data using JSOn format
@app.route('/service',methods=['GET'])
def ser():
  data = [1,2,3,4]
  return jsonify (data)

@app.route('/historian',methods=['GET'])
def historian():
   topic = request.args.get('topic',"#")
   timestamp = request.args.get('timestamp',"1970-01-01 00:00:00")

   topic=topic.replace("#","%")
  
   SQL = "SELECT timestamp, topic, payload FROM historian_data WHERE timestamp >= ? and topic LIKE ?"

   conn = sqlite3.connect(DB_FILE)
   cursor = conn.cursor()  
   cursor.execute(SQL,(timestamp,topic))  

   results = cursor.fetchall()

   results_data = [{"topic":row[1], "payload":row[2], "timestamp":row[0]} for row in results]  
  
   return jsonify(results_data)

if __name__ == "__main__"
  app.run(host='0.0.0.0',port=5000)

