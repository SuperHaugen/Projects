import requests

url = 'http://www.novasoftware.se/webviewer/(S(2zz23555rmnhsq4532jncfef))/design1.aspx?schoolid=60700&code=116504'

r = requests.get(url)

r_html = r.text

print (r_html)
