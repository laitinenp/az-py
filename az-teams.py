from az import *
import json
import sys

def placeAzCommands( teamDefs ):
    for t in teamDefs["teams"]:
        print(
            "az devops project create --name '" +
            t["teamName"] +
            "' --description 'Project for team " +
            t["teamName"] +
            "' --process Scrum --organization " +
            teamDefs["organization"]
        )
        for s in t["teamMembers"]:
            print(
                "az devops user add --email-id " +
                s["Email"] +
                "--license-type express --send-email-invite true --organization " +
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
    teams = read_teams( sys.argv[1] )
    placeAzCommands(teams)
    return 0

if __name__ == "__main__":
    main()

# e = emails( wb )
# for x in e:
#    print( x )
