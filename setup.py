import json 
import subprocess

env = {}
User =subprocess.run("whoami", capture_output=True).stdout.decode("utf-8").strip()
home_directory = f"/home/{User}" if User != "root" else "/root"
env["root"] = f"{home_directory}/.id1fs/ID1FS"
env["bf"] = f"{home_directory}/.id1fs/ID1FS/backup"
env["md"] = f"{home_directory}/.id1fs/ID1FS/metadata"
env["log"] = f"{home_directory}/.id1fs/ID1FS/system/log"
env["systm"] = f"{home_directory}/.id1fs/ID1FS/system"
env["cwd"] = f"/home"

with open(f"{home_directory}/.id1fs/ID1FS/system",'w') as f:
    json.dump(env, f, indent=4)

with open('system/logs','w') as f:
    f.write("")
