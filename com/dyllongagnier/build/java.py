from com.dyllongagnier.build.core import get_files
from os import makedirs, chdir, getcwd
import os.path
from pathlib import Path
import subprocess
from shutil import rmtree

def __get_class_path__(class_paths):
    class_paths = list(class_paths)
    class_path = ""
    for i in range(len(class_paths)):
        if i != len(class_paths) - 1:
            class_paths += class_paths[i] + ":"
        else:
            class_path += class_paths[i]
    return class_path

#class_paths also include jars
def build_classes(source_dir, bin_dir, recursive=True, *class_paths):
    if type(recursive) is not bool:
        raise ValueError("Recursive flag must be of type boolean")
    makedirs(bin_dir, exist_ok=True)
    args = ["javac", "-d", bin_dir]
    class_path = __get_class_path__(class_paths)
    if class_path != ""
        args = args + ["-cp"] + [class_path]
    to_compile = get_files(source_dir, recursive, '.java')
    args = args + to_compile
    subprocess.check_call(args)

def build_jar(input_dir, output_file, main_class=None):
    args = ["jar"]
    if main_class != None:
        args += ["cfen", output_file, main_class]
    else:
        args += ["cfn", output_file]
    args += ["-C", input_dir, "."]
    subprocess.check_call(args)
    subprocess.check_call(["jar", "i", output_file])

def extract_jar(input_jar, output_dir):
    makedirs(output_dir, exist_ok=True)
    old_cwd = getcwd()
    try:
        chdir(output_dir)
        subprocess.check_call(["jar", "xfn", input_jar])
    finally:
        chdir(old_cwd)

def combine_jars(jars, output_jar, main_class=None):
    internal_dir = "__pybuild_deps__"
    assert not os.path.exists(internal_dir)
    makedirs(internal_dir)
    try:
        for jar in jars:
            extract_jar(jar, internal_dir)
        build_jar(internal_dir, output_jar, main_class)
    finally:
        rmtree(internal_dir)

def append_jar(jar, base_dir, *files):
    files = list(files)
    args = ["jar", "ufMn", jar]
    for file_x in files:
        args.append("-C")
        args.append(base_dir)
        args.append(file_x)
    print(args)
    subprocess.check_call(args)
