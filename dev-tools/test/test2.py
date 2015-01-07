import subprocess

notebook = '/notebooks/example.ipynb'

script = "ipython nbconvert --config /notebooks/static/config.py " + notebook

subprocess.call(script, shell=True)