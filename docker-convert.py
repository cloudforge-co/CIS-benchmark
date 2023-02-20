import json
import os

maincontrol = ""
subcontrol = ""
check = ""

header = "ID-ctrl-Description-ctrl-Result-ctrl-Details-ctrl-Comments"
print (header)

fileName = os.getenv("S3_FILE_NAME", None)

with open(fileName, 'r') as cis_file:
    cis_data = json.load(cis_file)

    for y in cis_data["tests"]:
        myId = y["id"]
        myText = y["desc"]
        subcontrol = (f'{myId}-ctrl-{myText}-ctrl--ctrl--ctrl-')
        print (subcontrol)

        for z in y["results"]:
            testNum = z["id"]
            testDesc = z["desc"]
            status = z["result"]
            actual = ""
            if "details" in z:
                actual = z["details"]

            check = (f'{testNum}-ctrl-{testDesc}-ctrl-{status}-ctrl-{actual}-ctrl-')
            print (check.replace("\n","\\n"))
