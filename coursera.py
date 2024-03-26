!rm -f rklib.py
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-SN0101EN-SkillsNetwork/rklib.py

from rklib import submit
import json

key = "RrIb4SHNEeiLcw7AkKxwaA"
part = "zetaj"
email = "djfdfldf@gmail.com"
token = "dfjdhfdl" #you can obtain it from the grader page on Coursera (have a look here if you need more information https://youtu.be/GcDo0Rwe06U?t=276)


submit(email, token, key, part, [part], json.dumps(23))
