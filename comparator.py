import subprocess
import re

def execute(command_parts):
    return subprocess.run(command_parts, capture_output=True).stdout.decode()

class Exit(Exception):
    pass

def prompt_for_luminosity():
    match = re.match(r"#(..)(..)(..)", execute(["gpick", "-s", "-o"]))
    if match is None:
        raise Exit()
    r, g, b = map(lambda n: int(n, 16), match.groups())
    luminosity = 0.299*r + 0.587*g + 0.114*b
    return luminosity

try:
    while True:
        old_luminosity = prompt_for_luminosity()
        new_luminosity = prompt_for_luminosity()
        print(f"old - new = {old_luminosity - new_luminosity}")
except Exit:
    pass
