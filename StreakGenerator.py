
# USage: python thisFile.py w ClassName
import re
import os, errno
import sys


from os.path import expanduser
homePath = expanduser("~")

# Our variables that we got passed in:


arguments = sys.argv

pathToMailFoo = homePath + "/MailFoo/"

typeOfFile =   "modules" if (arguments[1] == "m") else "widgets"
className =  arguments[2]


basePathToPathsFiles = pathToMailFoo + "builders/buildSettings/"
# Paths
jsPaths = basePathToPathsFiles + "clientBuildJavascriptPaths.txt"
cssPaths =basePathToPathsFiles +  "clientBuildCSSPaths.txt"
htmlPaths = basePathToPathsFiles + "clientBuildHTMLPaths.txt"


modulesAndWidgetsRelativePath = "extensions/common/js/"
modulesAndWidgetsPaths = pathToMailFoo +  modulesAndWidgetsRelativePath



pathOfTargetFiles = modulesAndWidgetsPaths + typeOfFile + "/"
# This is used to inject path into .txt paths files
relativePathOfTargetFiles = modulesAndWidgetsRelativePath + typeOfFile + "/"


# 'builders/buildSettings/clientBuildJavascriptPaths.txt'


def generteJavascriptClassFromTemplate (className, lowerCaseClassName, classType):
    # Open up our file
    templateFileName = "template" + classType + ".js"
    tempalteFile = open(templateFileName)
    lines = tempalteFile.readlines()
    tempalteFile.close()

    # Open a new file

    targetFileName = lowerCaseClassName +  "/" + lowerCaseClassName + classType   + ".js"
    pathToTargetFile = pathOfTargetFiles + targetFileName
    targetFile = open(pathToTargetFile, 'w')

    # Now we generate the lines with our classname
    cleanLines = []
    for line in lines:
        result = re.sub(r'\{\{replace_class\}\}', lambda match:  className, line)
        result = re.sub(r'\{\{replace_MorW\}\}', lambda match:  typeOfFile.capitalize(), result)
        targetFile.write(result);
        cleanLines.append(result)
    targetFile.close()

    relativePathToTarget =  relativePathOfTargetFiles + targetFileName
    addPathToFile(jsPaths, relativePathToTarget)

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



# Path Functions
# ------------------------------------------------------------

def addPathToFile (pathsFile, path):
    paths = open(pathsFile, "a")
    paths.write(path + '\n')
    paths.close()



def addEmptyLineToPathFile(pathsFile):
    paths = open(pathsFile, "a")
    paths.write( '\n')
    paths.close()


# Create CSS and HTML files
# ------------------------------------------------------------

def generteCSSClassFromTemplate (className, lowerCaseClassName):

    targetFileName = lowerCaseClassName +  "/" + lowerCaseClassName + ".css"
    pathToTargetFile = pathOfTargetFiles + targetFileName
    targetFile = open(pathToTargetFile, 'w')
    targetFile.write("")
    targetFile.close()

    relativePathToTarget =  relativePathOfTargetFiles + targetFileName

    addPathToFile(cssPaths, relativePathToTarget)

#

def generteHTMLClassFromTemplate (className, lowerCaseClassName):

    targetFileName = lowerCaseClassName +  "/" + lowerCaseClassName + ".html"
    pathToTargetFile = pathOfTargetFiles + targetFileName
    targetFile = open(pathToTargetFile, 'w')
    targetFile.write("")
    targetFile.close()

    relativePathToTarget =  relativePathOfTargetFiles + targetFileName
    addPathToFile(htmlPaths, relativePathToTarget)

# ------------------------------------------------------------

lowerCaseClassName = downcaseFirstLetter(className)

createDirectory(pathOfTargetFiles + lowerCaseClassName)
generteJavascriptClassFromTemplate(className, lowerCaseClassName, "VC")
generteJavascriptClassFromTemplate(className, lowerCaseClassName,  "View")
generteJavascriptClassFromTemplate(className, lowerCaseClassName,  "Model")

# Create the JS Files
generteCSSClassFromTemplate(className, lowerCaseClassName)
generteHTMLClassFromTemplate(className, lowerCaseClassName)

# We need to write our:
# - ViewController
# - View
# - Model
#
# - .html
# - .css



