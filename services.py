from vosk import Model, KaldiRecognizer
import wave,json
MODEL_PATH='vosk-model-small-en-us-0.15'

def transcribe(file_path):
 wf=wave.open(file_path,'rb')
 model=Model(MODEL_PATH)
 rec=KaldiRecognizer(model,wf.getframerate())
 text=''
 while True:
  data=wf.readframes(4000)
  if len(data)==0: break
  if rec.AcceptWaveform(data):
   r=json.loads(rec.Result())
   text += r.get('text',' ')
 return text

def analyze(text):
 t=text.lower()
 intent='General Support'
 if 'refund' in t: intent='Refund Request'
 elif 'cancel' in t: intent='Cancellation'
 sentiment='Negative' if any(x in t for x in ['angry','issue','problem']) else 'Positive'
 unresolved='Yes' if any(x in t for x in ['not resolved','still waiting','call back']) else 'No'
 return {'intent':intent,'sentiment':sentiment,'unresolved':unresolved}
