# Tiedosto az.py
import subprocess
import json

def az_cli( cmd_str ):
    
    proc = subprocess.run(cmd_str, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)

    # reading output and error
    proc_stdout =  proc.stdout.decode("utf-8")
    proc_stderr = proc.stderr.decode("utf-8")

    # convert output to json
    out_json = json.loads(proc_stdout)

    return [ out_json, proc_stderr ]
