# tripal_tests


## Introduction
Test utilities based on [robotframework](http://robotframework.org/) using [SeleniumLibrary](https://github.com/robotframework/SeleniumLibrary) to test i5k contact page(https://i5k.nal.usda.gov/contact) and register page(https://i5k.nal.usda.gov/register/project-dataset/account). For more information, please refer to the summary document.

## Prerequisite
All automated tests for this repository must be executed on Jenkins CI.

## Usage
### Run the contact_register_test: 
* Python 
  * Quick start: `python contact_register_stage/contact_register_stage.py` 

* Robotframework
  * Quick start: `robot contact_register_stage/contact_register_stage.robot`
  
### Run the apollo2_register_test: 
* Python 
  * Quick start: `python apollo2_registration/apollo2_registration.py` 
  
### Run the request_project_test: 
* Python 
  * Quick start: `python request_project/request_project.py` 
