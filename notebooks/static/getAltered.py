import glob
import os.path, time
import convert_one_file

def getChanged():
    print("-------start----------")
    pyFiles = glob.glob("/notebooks/*.ipynb") + glob.glob("/notebooks/**/*.ipynb") + glob.glob("/notebooks/**/**/*.ipynb")

    tc = 0
    tsFile = 'tsFile.txt'
    if os.path.exists('tsFile.txt'):
        f = open('tsFile.txt', 'r')
        t = f.readline()
        f.close()
        tc = time.gmtime(float(t))

    t=time.time()
    f = open('tsFile.txt','w')
    f.write(str(t)) # python will convert \n to os.linesep
    f.close()


    changed = list({f for f in pyFiles if time.gmtime(os.path.getmtime(f)) > tc})
    print("-------changed----------")
    print(changed)
    print("-------changed----------")
    return changed

changed_nbs = getChanged()
print('hello')
print(changed_nbs)
for nb in changed_nbs:
    print("-------",nb)
    convert_one_file.convert_one(nb)

