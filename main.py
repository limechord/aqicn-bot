import urllib2
from google.appengine.api import mail

url = "http://aqicn.org/?city=CITYNAME&widgetscript&size=xlarge"
result = urllib2.urlopen(url)
string = result.read()
string = string[:-2]
string = string[16:]

message = mail.EmailMessage(sender="AQICN Robot <me@APPNAME.appspotmail.com>",
                           subject="AQICN Report")

message.to = "YOURNAME <YOUREMAIL>",
message.html = "<html><body> %s </body></html>" % (string)


message.send()
