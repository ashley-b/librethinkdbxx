from sys import argv
from re import sub
from os import path

print("#include \"testlib.h\"");
print("void run_upstream_tests() {")
for file in argv[1:]:
    name = sub(r'[^a-zA-Z0-9_]', '_', path.splitext(file)[0])
    print("    extern void %s();" % name)
    print("    clean_slate();")
    print("    %s();" % name)
print("}")
