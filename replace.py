import re

# Our variables that we got passed in:
templateFileName = 'sampleVC.js'
className = "C11ool"




def generteJavascriptClassFromTemplate (className, classType):
    # Open up our file
    templateFileName = "template" + classType + ".js"
    tempalteFile = open(templateFileName)
    lines = tempalteFile.readlines()
    tempalteFile.close()

    # Open a new file
    targetFileName = className + classType   + ".js"
    targetFile = open(targetFileName, 'w')

    # Now we generate the lines with our classname
    cleanLines = []
    for line in lines:
        result = re.sub(r'\{\{replace_class\}\}', lambda match:  className, line)
        targetFile.write(result);
        cleanLines.append(result)




generteJavascriptClassFromTemplate(className, "VC")
generteJavascriptClassFromTemplate(className, "View")


# We need to write our:
# - ViewController
# - View
# - Model
#
# - .html
# - .css



