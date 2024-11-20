import subprocess
import re

def execute(command_parts):
    return subprocess.run(command_parts, capture_output=True).stdout.decode().strip()

class Exit(Exception):
    pass

def prompt_for_luminosity(output_prefix):
    color_hex = execute(["gpick", "-s", "-o"])
    match = re.match(r"#(..)(..)(..)", color_hex)
    if match is None:
        raise Exit()
    print(f"{output_prefix}: {color_hex}")
    r, g, b = map(lambda n: int(n, 16), match.groups())
    luminosity = 0.299*r + 0.587*g + 0.114*b
    return luminosity

try:
    while True:
        old_luminosity = prompt_for_luminosity("1. Old")
        new_luminosity = prompt_for_luminosity("2. New")
        print(f"3. old - new = {old_luminosity - new_luminosity}")
except Exit:
    pass
