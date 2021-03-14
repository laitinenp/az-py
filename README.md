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
Description: generate azure az commands to produce devops teams.

> py az-teams.py teams.json > azconf.bat

Program 3: gen-teams-az.bat
Description: generate az commands and teams.json according to org-conf.json and students list in the Peppi-generated Students.xls list.

> gen-teams-az.bat
