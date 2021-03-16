from az import *
import json
import sys

def placeRemoveAzCommands( teamDefs ):
    for t in teamDefs["teams"]:
        azCommand = "az devops project show --project \"" + t["teamName"] + "\" --organization " + teamDefs["organization"] + " --query \"id\""
        projid, err = az_cli( azCommand )
        print(
            "az devops project delete --id \"" +
            projid +
            "\" --organization " +
            teamDefs["organization"]
        )
        for s in t["teamMembers"]:
            print(
                "az devops user remove --user " +
                s["Email"] +
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
        print("usage: py az-del-teams.py <teams-file.json>")
        return -1
    teams = read_teams( sys.argv[1] )
    placeRemoveAzCommands(teams)
    return 0

if __name__ == "__main__":
    main()
