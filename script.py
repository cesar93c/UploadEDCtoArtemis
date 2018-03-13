# In[15]:

from requests.auth import HTTPBasicAuth
import csv
import requests

user=''
pw=''
advertiserid=''
campaignid=''



url='https://artemis.havas.com/api/edc/upload/'+advertiserid+'/'+campaignid+'?info=1&process=1'
csvfile="xxxxxx.csv"

with open(csvfile, 'rb') as f:
    r = requests.post(url, files={'file': (csvfile, f, 'text/csv', {'Expires': '0'})}, auth=HTTPBasicAuth(user, pw))
    print(r.text)


# In[ ]:
