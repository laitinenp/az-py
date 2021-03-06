from az import *
import json
import sys

def placeAzCommands( teamDefs ):
    for t in teamDefs["teams"]:
        print(
            "call az devops project create --name \"" +
            t["teamName"] +
            "\" --description \"Project for team " +
            t["teamName"] +
            "\" --process " +
            teamDefs["process"] +
            " --organization " +
            teamDefs["organization"]
        )
    pass

def read_teams( jsonfile ):
    with open( jsonfile ) as teams:
        data = teams.read()
    return json.loads( data )

def main():
    if len(sys.argv) != 2:
        print("usage: py az-teams.py <teams-file.json>")
        return -1
    try:
        teams = read_teams( sys.argv[1] )
        placeAzCommands(teams)
    except FileNotFoundError:
        print("Could not find file " + sys.argv[1] + ". Exiting.")
        return -1
    except:
        print("Could not generate commands. The input file may be corrupted. Exiting.")
        return -1
    return 0

if __name__ == "__main__":
    main()
