#!/usr/bin/python3
import sys

def usage():
    print("USAGE: correct_cdb [PATH TO CDB.json]")

if len(sys.argv) != 2:
    usage()
    sys.exit(1)

cdb_path = sys.argv[1]

import json
try:
    cdb_handle = open(cdb_path, "r+")
except Exception:
    print("This JSON file does not exist")
    cdb_handle.close()
    sys.exit(1)

try:
    cdb = json.load(cdb_handle)
except Exception:
    print("Provided file is not in JSON format")
    cdb_handle.close()
    sys.exit(1)

import subprocess
try:
    result = subprocess.run(['arm-none-eabi-gcc', '-dumpversion'], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8')
    version = result[:len(result) - 1]
except Exception:
    print("arm-none-eabi-gcc is not installed on your system")
    cdb_handle.close()
    sys.exit(1)

base_lib_path = "/usr/lib/gcc/arm-none-eabi/"
inc_folders = ["/include", "/include-fixed", "/../../../../arm-none-eabi/include"]


for data in cdb:
    try:
        for p in inc_folders:
            final_path_arg = "-I" + base_lib_path + version + p
            if final_path_arg not in data["arguments"]: 
                data["arguments"].append(final_path_arg)
    except Exception:
        print("File containes unacceptable sections")

cdb_handle.seek(0)

try:
    json.dump(cdb, cdb_handle, indent = 4)
except Exception:
    print("Dumping altered JSON failed")
    sys.exit(1)
cdb_handle.close()
