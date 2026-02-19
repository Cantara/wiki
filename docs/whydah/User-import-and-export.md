# User import and export

### WorkInPprogress - Rationale: 

User wants to import and export users and roles using CSV file. 
Choose to model this as a userImport resource instead of looping through all entries in UserAdminService because it is assumed to be easier to show the result in the GUI if the result of the import can be obtained from a single GET request. 
Communication should be asynchronous because the import can take some time. 

### Import

1. Upload CSV file in UserAdminWebapp. 
    1. Format is fixed. Not necessary to add functionality to the GUI to map between CSV format and expected format. Can support download of csv template and user can use spreadsheet program to edit the CSV to the chosen format. 
    1. Flat liste med bruker + rolle. To roller, to linjer. Oppdaterer og legger til, men ikke sletting. Med brukernavn som nøkkel. Endringer i role value og person data vil overskrive. 
    1. TODO: Erik legge inn faktisk CSV-template her. 
1. UserAdminWebapp receives CSV file and extracts the plain text. 
1. UserAdminService acts as proxy in front of UIB. 
1. UIB expose a _text/plain_ POST endpoint, e.g. /user/import/.  
    1. Create a new userImport job from the given plain text. Set an id and importStatus=in-progress. Persist in database. Return with a link to where the result can be found later.
    1. Perform import. Count number of successful rows. Create a result list of all failed rows. Persist success count and list of failed rows to database. 
1. UIB expose a GET endpoint, e.g. /user/import/\, which clients are expected to poll for the result of the import. 
    1. The result is JSON formatted and should contain the userImport id, successfulRowCount, list of rows that failed + error message per row. 

### Export
