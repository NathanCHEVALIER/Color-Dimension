import sys
from cx_Freeze import setup, Executable

#build_exe_options = {"packages" : [os], "excludes" :["tkinter"]}

options = {
    'build_exe' : {
        'includes' : ["Game", "entities/Entities"],
        'path' : sys.path + ['game']
    }
}

setup(
    name = "exe",
    version = "0.1",
    description = "Jeux",
    executables = [Executable("main.py")],
    #options=options
)