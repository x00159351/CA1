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

  total = 0
  first = 0
  second = 0
  third = 0
  fourth = 0
  fifth = 0
  for i in range(100):
    c.perform()
    total = total + c.getinfo(c.TOTAL_TIME)
    if i == 19:
      first = round(total / 20, 5)
      total = 0
    if i == 39:
      second = round(total / 20, 5)
      total = 0
    if i == 59:
      third = round(total / 20, 5)
      total = 0
    if i == 79:
      fourth = round(total / 20, 5)
      total = 0
    if i == 99:
      fifth = round(total / 20, 5)

  currentDT = datetime.datetime.now()
  data =	{
    "filename": "LoadTest" + currentDT.strftime("%m%d%H%M%S"),
    "plottype": "line",
    "x": ["1", "2", "3", "4", "5"],
    "y": [first, second, third, fourth, fifth],
    "ylab": "Comparison"
  }

  requests.post('https://us-central1-future-aurora-269520.cloudfunctions.net/Load', json=data)
  c.close()