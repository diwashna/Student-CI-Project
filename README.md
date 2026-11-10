# Student CI Project

CMSC 426 Jenkins and GitHub continuous integration assignment.

## Requirements
Python 3 and Git. No additional Python packages are required.

## Run the application
python3 app.py

## Run automated tests
python3 -m unittest discover -s tests -v

## Continuous integration
The Jenkins job Student-CI-Project retrieves this repository and runs
the application and automated tests. A failing test must fail the build.
