import re
import os, errno

# Our variables that we got passed in:
className = "MailMerge"




def generteJavascriptClassFromTemplate (className, lowerCaseClassName, classType):
    # Open up our file
    templateFileName = "template" + classType + ".js"
    tempalteFile = open(templateFileName)
    lines = tempalteFile.readlines()
    tempalteFile.close()

    # Open a new file

    targetFileName = lowerCaseClassName +  "/" + lowerCaseClassName + classType   + ".js"
    targetFile = open(targetFileName, 'w')

    # Now we generate the lines with our classname
    cleanLines = []
    for line in lines:
        result = re.sub(r'\{\{replace_class\}\}', lambda match:  className, line)
        targetFile.write(result);
        cleanLines.append(result)


# Stackoverflow Helper Functions
# ------------------------------------------------------------
def createDirectory(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

downcaseFirstLetter = lambda s: s[:1].lower() + s[1:] if s else ''

# ------------------------------------------------------------



lowerCaseClassName = downcaseFirstLetter(className)

createDirectory(lowerCaseClassName)
generteJavascriptClassFromTemplate(className, lowerCaseClassName, "VC")
generteJavascriptClassFromTemplate(className, lowerCaseClassName,  "View")


# We need to write our:
# - ViewController
# - View
# - Model
#
# - .html
# - .css



