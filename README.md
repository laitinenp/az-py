# az-py
Python utilities for managing Azure resources in education.

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

> py az-teams.py teams.json > azconf.bat

Program 3: gen-teams-az.bat
Description: generate az commands and teams.json according to org-conf.json and students list in the Peppi-generated Students.xls list.

> gen-teams-az.bat

Program 4: az-del-teams.py
Description: generate az commands for removing existing azure teams and organization members using teams json file.
Prerequisite: Azure resources created using the script created by the gen-teams-az.bat

> py gen-del-teams.py teams.json > del-teams-az.bat
