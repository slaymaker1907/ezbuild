# ezbuild
A simple multi-language build system using python script files.

This build system is designed to be both easy to use for end users, powerful due to its basis in a full-featured programming language (Python), have a large number of helper methods to ease in building many languages, and (eventually) cross-platform through the abstractions offered by Python.

Unlike many build systems, this build system is centered on the idea that while build systems may have complex helper libraries, building a single module ought to have a single authorative source file for the build process and that once this library and Python 3 are installed, a user ought to be able to build the module by simple clicking on a single script with no additional configuration files, scripts that generate build files, etc. All building behavior should be controlled through one script.

Of course, sometimes modifications might be necessary in order to facilitate quick building, but this library should be able to build any of the languages supported without additional build tools (by build tools, I mean those outside of the core build tools like Make or autoconf).

The current version of ezbuild only supports Java compilation. However, Groovy support is currently under development and future support for CSharp and C++ is planned.
