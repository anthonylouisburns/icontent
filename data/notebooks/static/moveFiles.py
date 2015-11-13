import glob
import shutil
import os


def new_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


pyFiles = glob.glob("*.ipynb") + glob.glob("**/*.ipynb") + glob.glob("**/**/*.ipynb")
print(pyFiles)
for p in pyFiles:
    lastDash = p.rfind("/")+1
    pyDir = p[:lastDash]
    pyFile = p[lastDash:]
    htmlFile = pyFile.replace("ipynb", "html")
    htmlDir = "html/"+pyDir
    new_dir(htmlDir)
    if os.path.exists(htmlFile):
        shutil.move(htmlFile, htmlDir + htmlFile)
        print("moving:", htmlFile, htmlDir)