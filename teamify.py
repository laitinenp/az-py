from az import *
import xlrd
import random
import math
import json
import sys

# read students list from excel and return in json format
def read_students( loc ):
    wb = xlrd.open_workbook(loc)
    return wb.sheet_by_index(0)

# get email list form students excel sheet wb
def emails( wb ):
    res = []
    for i in range(1, wb.nrows):
        res.append(wb.cell_value(i, 3))
    return res

# Get one student in the line in dict format (json)
def getstu( wb, i ):
    return {
        "Last name": wb.cell_value(i + 1, 0),
        "First name": wb.cell_value(i + 1, 1),
        "Name": wb.cell_value(i + 1, 2),
        "Email":  wb.cell_value(i + 1, 3),
        #"Email oma": wb.cell_value(i + 1, 4),
        #"Student id": wb.cell_value(i + 1, 5),
        "Username": wb.cell_value(i + 1, 6),
        "State": wb.cell_value(i + 1, 7)
        #, "State code": wb.cell_value(i + 1, 8)
    }

# Convert excel sheet data structure wb to json format 
def getjson( wb ):
    res = []
    for i in range(1, wb.nrows-1):
        res.append(getstu(wb, i))
    return res

# Read input configuration file
def read_conf( jsonfile ):
    with open( jsonfile ) as conf:
        data = conf.read()
    return json.loads( data )

# Create random teams json document according to settings json data and students list
def teamify( settings, students ):
    org = settings['organization']
    teamNames = settings['teams']
    prefTeamSize = settings['prefTeamSize']
    process = settings['process']
    numTeamsNeeded = math.floor( len(students) / prefTeamSize )
    # This is the result we shall return in the end after having filled the teams list
    result = {
        "organization": org,
        "process": process,
        "teams": []
    }
    # Fill the team structures
    for n in teamNames[ : numTeamsNeeded ]:
        result["teams"].append({
            "teamName": n,
            "teamMembers": []
        })
    # We create random teams
    random.shuffle( students )
    # And finally add students list in to the team structures
    i = 0   # refers to team number which goes around 0 .. (numTeamsNeeded-1)
    for s in students:
        result["teams"][i]["teamMembers"].append(s)
        # fill only teams we need this time
        if i < (numTeamsNeeded - 1):
            i += 1
        else:
            i = 0
    return result

def main():
    if len(sys.argv) != 2:
        print("usage: py teamify.py <json-settings-file>")
        sys.exit(1)
    settings = read_conf( sys.argv[1] )
    wb = read_students( settings["studentsExcel"] )
    studs = getjson( wb )
    if settings["prefTeamSize"] > len(studs):
        print("Preferred team size exceeds the number of students. Can not generate teams. Exiting.")
        sys.exit(1)
    teams = teamify( settings, studs )
    json_teams = json.dumps( teams, indent = 4 )
    print(json_teams)

if __name__ == "__main__":
    main()
    sys.exit(0)
