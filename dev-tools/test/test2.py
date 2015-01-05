import subprocess

notebook = '/notebooks/example.ipynb'

script = "ipython nbconvert --config /notebooks/static/set_const.py " + notebook

subprocess.call(script, shell=True)