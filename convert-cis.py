import json
import os

maincontrol = ""
subcontrol = ""
check = ""

header = "ID-ctrl-Recommendation-ctrl-Status-ctrl-Value-ctrl-Audit"
print (header)

fileName = os.getenv("S3_FILE_NAME", None)

with open(fileName, 'r') as cis_file:
    cis_data = json.load(cis_file)
    for x in cis_data["Controls"]:
        myId = x["id"]
        myText = x["text"]
        maincontrol = (f'{myId}-ctrl-{myText}-ctrl--ctrl--ctrl-')
        print (maincontrol)

        for y in x["tests"]:
            myId = y["section"]
            myText = y["desc"]
            subcontrol = (f'{myId}-ctrl-{myText}-ctrl--ctrl--ctrl-')
            print (subcontrol)

            for z in y["results"]:
                testNum = z["test_number"]
                testDesc = z["test_desc"]
                status = z["status"]
                actual = z["actual_value"]
                audit = z["audit"]

                check = (f'{testNum}-ctrl-{testDesc}-ctrl-{status}-ctrl--ctrl-{audit}')
                print (check.replace("\n","\\n"))
