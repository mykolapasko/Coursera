import re
x = "\"<p>Please click <a href=\"http://www.dr-chuck.com\">here</a></p>\""
y = re.findall(r"http://.*", x)
print y