from pathlib import Path
import json

#=====================================================================#

def get_path(path):
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config[path]

#=====================================================================#