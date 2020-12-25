from pathlib import Path
import subprocess
import glob
import re
import os
import tempfile
import uuid
import datetime
from gcode import gcode

class SlicerWrapper:
    def __init__(self, config = None):
        self._config = config

    @staticmethod
    def get_available_configs():
        configs = glob.glob('*.ini')
        return configs

    def slice(self, file_path: str) -> str:
        temp_file_path = Path(tempfile.gettempdir()) / \
            '{}.{}'.format(uuid.uuid4().hex, 'gcode')
        print(temp_file_path)

        subprocess_args = [ "prusa-slicer-console", 
                            "-s", file_path, 
                            "--load", self._config, 
                            "-o", temp_file_path]
        subprocess.run(subprocess_args)

        g = gcode.from_file(temp_file_path)
        os.remove(temp_file_path)
        return g