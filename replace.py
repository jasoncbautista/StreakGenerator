import re


f = open('sampleVC.js')
lines = f.readlines()
f.close()

rawString = "{{prefix_HelloWorld}}   testing this. {{_thiswillNotMatch}} {{prefix_Okay}}"



cleanLines = []


className = "Cool"
for line in lines:

    result = re.sub(r'\{\{replace_class\}\}', lambda match:  className, line)
    print result


