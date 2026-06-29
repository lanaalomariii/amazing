import sys

def read_configuration_file(filename:str) -> dict:
    configurations = {}
    try:
        with open(filename, "r") as f:
            for l in f:
               line =  l.strip()
               if line.startswith("#") or line == "":
                   continue
               if not "=" in line:
                   print("missing")
                   sys.exit(1)
                key, value = line.split("=")
                configurations[key.strip()] = value.strip()
        except FileNotFoundError:
            print(f"{filename} not found")
        return configurations

def validate_configuration(config:dict) ->:
    mandatory_keys = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT
