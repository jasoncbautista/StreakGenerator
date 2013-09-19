import re

def replacer(match):
        return "ONE"


f = open('sampleVC.js')
lines = f.readlines()
f.close()

rawString = "{{prefix_HelloWorld}}   testing this. {{_thiswillNotMatch}} {{prefix_Okay}}"





cleanLines = []

for line in lines:

    result = re.sub(r'\{\{replace_class\}\}', replacer, line)
    print result


