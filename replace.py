import re

# Our variables that we got passed in:
templateFileName = 'sampleVC.js'
className = "Cool"


# Open up our file
tempalteFile = open(templateFileName)
lines = tempalteFile.readlines()
tempalteFile.close()

# Open a new file
targetFileName = className + "VC.js"
targetFile = open(targetFileName, 'w')

# Now we generate the lines with our classname
cleanLines = []
for line in lines:
    result = re.sub(r'\{\{replace_class\}\}', lambda match:  className, line)
    targetFile.write(result);
    cleanLines.append(result)







