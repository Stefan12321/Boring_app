
from cx_Freeze import setup, Executable
import shutil
import os

try:
    shutil.rmtree('build')
    shutil.rmtree('dist')
except:
    pass
# base = 'Win32GUI'
base = None

executables = [Executable('main.py',
                          target_name='boring_app.exe',
                          base=base),
               ]

# packages = ["main"]
options = {
    'build_exe': {
        'include_msvcr': True,
    }
}

setup(
    name="Orion config",
    options=options,
    version=1.1,
    description='',
    executables=executables
)