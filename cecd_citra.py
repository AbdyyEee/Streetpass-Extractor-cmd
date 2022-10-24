\from yaml import safe_load
from os import getcwd, listdir

if "config.yml" not in listdir():
    print("WARNING: Config.yml is not found in the current directory.")
    input()

with open("config.yml") as f:
    config_file = safe_load(f)
    citra_path = config_file["citra_path"]
    default_file_name = config_file["default_file_name"]

STREETPASS_LOCATION = rf"\nand\data\00000000000000000000000000000000\sysdata\00010026\{default_file_name}"
EVENT_LOG_LOCATION = STREETPASS_LOCATION[:-9]

if citra_path is None:
    print(
        "WARNING: The path for your Citra installation is not set. Paste the path in config.yml."
    )

from os.path import isdir
from shutil import move, rmtree
from subprocess import call

if default_file_name in listdir():
    print("Streetpassing... \n")
    call(
        ["python", "disa-extract.py", rf"{getcwd()}\{default_file_name}", getcwd()],
        cwd="Extractors",
    )
    print("Checking if path exists")
    if isdir(rf"{citra_path}{STREETPASS_LOCATION}\CEC"):
        rmtree(rf"{citra_path}{STREETPASS_LOCATION}\CEC")
    print("Moving CEC")
    move(f"CEC", rf"{citra_path}{STREETPASS_LOCATION}")
    print("Streetpass complete!")
else:
    print("The CECD file is not found in the current directory. Make sure the file has same as defined in config.yml. By default, the name is '00000000'.")
    
input()
