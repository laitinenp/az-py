echo off
echo Using the org-conf.json file for generating random teams...
echo on

py teamify.py org-conf.json > teams.json
py az-teams.py teams.json > az-create-teams.bat

echo off
echo ... done. If successfull, the teams.json file contains now teams-structure
echo and az-create-teams.bat file contains a set of az commands for creating azure
echo devops teams. Team members has to be added manually from the GUI since Ms has
echo not (yet) implemented az commands for the job.
echo .
echo You should now review the az-create-teams.bat contents and run the script.
echo .
echo Please use gen-del-teams-az.bat for generating az commands for removing the Azure
echo teams and users from the organization.
