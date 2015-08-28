import subprocess
from com.dyllongagnier.build.core import get_files
from com.dyllongagnier.build.java import __get_class_path__
from os import makedirs

def build_groovy_classes(source_dir, bin_dir, recursive=True, *class_paths):
    if type(recursive) is not bool:
        raise ValueError("Recursive flag must be of type boolean")
    makedirs(bin_dir, exist_ok=True)
    cmd = ["groovyc"]
    class_path = __get_class_path__(class_paths)
    if class_path != "":
        cmd += ["-cp"] + [class_path]
    cmd = cmd + ["--temp"] + [bin_dir]
    to_compile = get_files(source_dir, recursive, '.groovy')
    cmd = cmd + to_compile
    subprocess.check_call(cmd)

# Don't use this unless there are cross-dependencies
def build_groovy_java(groovy_dir, java_dir, bin_dir, recursive=True, *class_paths):
    if type(recursive) is not bool:
        raise ValueError("Recursive flag must be of type boolean")
    makedirs(bin_dir, exist_ok=True)
    cmd = ["groovyc"]
    class_path = __get_class_path__(class_paths)
    if class_path != "":
        cmd += ["-cp"] + [class_path]

    cmd += ["-j", "-Jd=" + bin_dir, ]
    if class_path != "":
        cmd += ["-Jcp=" + class_path]
    cmd = cmd + ["--temp"] + [bin_dir]
    to_compile = get_files(groovy_dir, recursive, '.groovy') + get_files(java_dir, recursive, '.java')
    cmd = cmd + to_compile
    print(cmd)
    subprocess.check_call(cmd)
