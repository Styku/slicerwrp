from pathlib import Path
import re
import os
import datetime

re_duration = re.compile(r'((?P<hours>\d+?)h\s)?((?P<minutes>\d+?)m\s)?((?P<seconds>\d+)s?)?')

def parse_duration(duration_str: str):
    parts = re_duration.match(duration_str)
    if not parts:
        return
    parts = parts.groupdict()
    time_params = {}
    for (name, param) in parts.items():
        if param:
            time_params[name] = int(param)
    return datetime.timedelta(**time_params)

class gcode:
    params = {  
        'print_time': 'estimated printing time (normal mode)',
        'filament_length': 'filament used [mm]'
    }
    param_conversion = {  
        'print_time': parse_duration, 
        'filament_length': float
    }
    params_set = set(params.values())


    def __init__(self, code: str):
        self._code = code
        self.parse_gcode_comments()

    @classmethod
    def from_string(cls, code: str):
        return gcode(code)

    @classmethod
    def from_file(cls, file_path: str):
        with open(file_path, 'r') as f:
            return gcode(f.read())

    def parse_gcode_comments(self) -> dict:
        read_params = re.compile(r'^;*([^=\n]+)=([^=\n]+)$', re.M)
        params = {m.group(1).strip(): m.group(2).strip() for m in read_params.finditer(self._code)}
        #print(gcode.params.items())
        #print(params)
        self._params = {k: gcode.param_conversion[k](params[v]) for k, v in gcode.params.items() if v in params}

    def __str__(self):
        return str(self._params)