import subprocess
import shutil
import os
import json
import itertools


def convert_one(notebook):

    with open(notebook) as data_file:
        data = json.load(data_file)

    script = "ipython nbconvert --config " + getConfig(data) + " " + notebook
    print(script)
    subprocess.call(script, shell=True, cwd=r'/notebooks/static')

    html = notebook.replace(".ipynb", ".html").replace("/notebooks/", "/notebooks/static/")
    html_dest = html.replace("/notebooks/static/", "/notebooks/icontent/")

    if not os.path.exists(os.path.dirname(html_dest)):
        os.makedirs(os.path.dirname(html_dest))

    #if os.path.exists(html_dest):
    #    os.remove(html_dest)

    shutil.move(html, html_dest)


def getConfig(nb):
    print('>>>>>>>>>setVariables')
    sourcelist = [cell["source"] for cell in nb["cells"] if cell["cell_type"] == 'markdown']
    allsource = list(itertools.chain(*sourcelist))

    config_script = "/notebooks/static/config.py"

    config_list = [s.partition("=")[2].strip() for s in allsource if s.partition("=")[0] == "config_script"]

    if len(config_list)>0: config_script=config_list[-1]

    return config_script