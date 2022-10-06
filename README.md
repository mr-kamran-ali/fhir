# FHIR Profile Comparison Repo

This Repo is focused on comparing FHIR profiles of X-eHealth Project and Smart4Health Project. 

Already compared profile results are present in `comparisons` directory. 

## Profile Comparison GUI
* Profile Comparison GUI is a `Django` based wrapper for `validator_cli.jar`, it offers a simpler way of comparing two FHIR profiles. 
* It needs `validator_cli.jar` in root of `profile_compare_gui` to perform the actual comparison. [Download Validator](https://github.com/hapifhir/org.hl7.fhir.core/releases/latest/download/validator_cli.jar)


## Run locally
* Clone the repo and change directory to `profile_compare_gui` and install all requirements using `pip3 freeze > requirements.txt`
* Run `python manage.py runserver` and a development server will start at `127.0.0.1:8000`