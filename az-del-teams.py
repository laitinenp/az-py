from az import *
import json
import sys

# Generate az command for removing the teams and students from azure devops organizations
def placeRemoveAzCommands( teamDefs ):
    for t in teamDefs["teams"]:
        # Need to know what is the project id by asking the Azure
        azCommand = "az devops project show --project \"" + t["teamName"] + "\" --organization " + teamDefs["organization"] + " --query \"id\""
        projid, err = az_cli( azCommand )
        # Produce az command for removing the project
        print(
            "az devops project delete --id \"" +
            projid +
            "\" --organization " +
            teamDefs["organization"]
        )
        # Produce az command for removing the team members from the Azure devops organization
        for s in t["teamMembers"]:
            print(
                "az devops user remove --user " +
                s["Email"] +
                " --organization " +
                teamDefs["organization"] +
                " --yes"
            )
    pass

# Read teams definitions from json file
def read_teams( jsonfile ):
    with open( jsonfile ) as teams:
        data = teams.read()
    return json.loads( data )

# Main function
def main():

    if len(sys.argv) != 2:
        print("usage: py az-del-teams.py <teams-file.json>")
        return -1
        
    try:
        # read teams data as json
        teams = read_teams( sys.argv[1] )
        # generate az command according to the result of the above
        placeRemoveAzCommands(teams)

    except FileNotFoundError:
        print("Could not read teams from " + sys.argv[1] + ". Exiting.")
        return -1
    except:
        print("Could not generate commands. The input file may be corrupted. Exiting.")
        return -1
    except:
        print("Could not generate az commands. You may have not logged in (using az login) or the teams or users in the Azure do not exist.")
        return -1

    return 0

if __name__ == "__main__":
    main()
