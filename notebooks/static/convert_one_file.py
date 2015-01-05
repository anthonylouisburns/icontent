import subprocess
import shutil
import os

def convert_one(notebook):
    script = "ipython nbconvert --config /notebooks/static/set_const.py " + notebook

    print(script)
    subprocess.call(script, shell=True, cwd=r'/notebooks/static')

    html = notebook.replace(".ipynb", ".html").replace("/notebooks/", "/notebooks/static/")
    html_dest = html.replace("/notebooks/static/", "/notebooks/html/")

    if not os.path.exists(os.path.dirname(html_dest)):
        os.makedirs(os.path.dirname(html_dest))

    #if os.path.exists(html_dest):
    #    os.remove(html_dest)

    shutil.move(html, html_dest)