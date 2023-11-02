from flask import Flask, render_template, jsonify

app = Flask(__name__)

app.route('/',methods=['GET'])
#Web page
def main():
  return render_template ('index.html')

#Serving up stuff 
app.route('/example',methogds=['GET'])
def example():
  return 'example'

#Return some data using JSOn format
app.route('/service',methods=['GET'])
def ser():
  data = [1,2,3,4]
  return jsonify (data)

if __name__ == "__main__"
  app.run()

