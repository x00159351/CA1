import pycurl
import requests
import datetime
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

def main(rqst):
  buffer = BytesIO()
  c = pycurl.Curl()
  c.setopt(c.URL, 'http://35.228.4.237:31080/')
  c.setopt(c.WRITEDATA, buffer)
  buffer2 = BytesIO()
  d = pycurl.Curl()
  d.setopt(c.URL, 'http://35.228.232.138:31916/allthenews?style=plain')
  d.setopt(c.WRITEDATA, buffer2)

  total = 0
  total2 = 0
  for i in range(100):
    c.perform()
    d.perform()
    total = total + c.getinfo(c.TOTAL_TIME)
    total2 = total2 + d.getinfo(d.TOTAL_TIME)
    if i == 19:
      firstAsync = round(total / 20, 5)
      firstSync = round(total2 / 20, 5)
      total = 0
      total2 = 0
    if i == 39:
      secondAsync = round(total / 20, 5)
      secondSync = round(total2 / 20, 5)
      total = 0
      total2 = 0
    if i == 59:
      thirdAsync = round(total / 20, 5)
      thirdSync = round(total2 / 20, 5)
      total = 0
      total2 = 0
    if i == 79:
      fourthAsync = round(total / 20, 5)
      fourthSync = round(total2 / 20, 5)
      total = 0
      total2 = 0
    if i == 99:
      fifthAsync = round(total / 20, 5)
      fifthSync = round(total2 / 20, 5)

  currentDT = datetime.datetime.now()
  data =	{
    "filename": "LoadTest" + currentDT.strftime("%m%d%H%M%S"),
    "plottype": "bar",
    "x": ["Async1", "Sync1", "Async2", "Sync2", "Async3","Sync3", "Async4", "Sync4", "Async5", "Sync5"],
    "y": [firstAsync, firstSync, secondAsync, secondSync, thirdAsync, thirdSync, fourthAsync, fourthSync, fifthAsync, fifthSync],
    "ylab": "Comparison"
  }

  response = requests.post('https://us-central1-future-aurora-269520.cloudfunctions.net/Load', json=data)
  return response.text
  c.close()