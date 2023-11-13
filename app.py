from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)
DB_FILE = "../historian_data.db"

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

