from flask import Flask,render_template,request
from services import transcribe,analyze
import os
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
 result=None
 if request.method=='POST':
  f=request.files['audio']
  path=os.path.join('uploads',f.filename)
  f.save(path)
  t=transcribe(path)
  result=analyze(t)
  result['transcript']=t
 return render_template('index.html',result=result)
if __name__=='__main__': app.run(debug=True)
