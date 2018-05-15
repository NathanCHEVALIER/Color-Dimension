import sys
import os
from cx_Freeze import setup, Executable

#buildOptions = dict(include_files = ["../music/"])
#options = dict(build_exe = buildOptions)

options = {"include_files" : ["../music/", "../font/", "../data/", "../img/"]

}

setup(
    name = "exe",
    version = "0.1",
    description = "Jeux",
    executables = [Executable("main.py")],
    options={"build_exe":options}
)