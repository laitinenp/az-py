# az-py
Python utilities for managing Azure resources in education.

Required Python libraries:
- xlrd
- random
- math
- json
- sys
- subprocess

Program 1: teamify.py
Description: create random teams structure from students list extracted from Peppi system.

Input:
org-conf.json - basic configuration information
Excel-file

Output:
teams in json format

Example run:
> py teamify.py org-conf.json > teams.json

Program 2: az-teams.py
Description: generate azure az commands to produce devops teams using teams json file.

> py az-teams.py teams.json > teams-az.bat

Program 3: az-users.py
Description: generate az commands to produce devops users az commands.

> py az-users.py teams.json > users-az.bat

Program 4: az-del-teams.py
Description: generate az commands for removing existing azure teams and organization members using teams json file.
Prerequisite: Azure resources created using the script created by the programs 2 and 3.

> py gen-del-teams.py teams.json > del-teams-users-az.bat
