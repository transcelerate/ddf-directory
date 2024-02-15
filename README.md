# TransCelerate's DDF Catalog Hosting and Automation

The purpose of this document is to provide version/contact information and instructions for installation of the solution.

## Description

This tool provides opportunities for solution providers and sponsors to connect and learn more about possible solutions utilizing Digital Data Flow (DDF) and the Unified Study Definitions Model (USDM).

## Design

The design is centered around leveraging Github's CI/CD tool, Github Actions, to modify a static file with the contents of an issue form upon its completion.

## Getting Started

### Installing

Simply extract this package to the root directory of any github repository

* File structure should be:
    * root
        * .github
            * ISSUE_TEMPLATE
                * new-catalog-entry.yml
	    * workflows
	        * update-catalog.yml
	* catalog
	    * add_row.py
        * catalog.md
	* README.md


### Executing program

Program is automatically executed every time the new-catalog-entry issue form is completed.
1. User submits a new issue by selecting "New Catalog Entry", and providing the required information in the form before submitting.
2. Submitting the form triggers GitHub to run an action detailed in "update-catalog.yml" which captures the form entry into a payload, saves the payload as an environment variable, and calls the "add_row.py" script.
3. "add_row.py" retrieves the payload from the environment variables, extracts the relevant solution information, and transforms it before loading it into "catalog.md"
4. Once "add_row.py" exits, the action then commits and pushes the "catalog.md" to the master site which redeploys and updates what is displayed on the public site "https://transcelerate.github.io/ddf-catalog/catalog/catalog.html"
 

### File Descriptions and Maintenance
    
* new-catalog-entry.yml
    * _Description_: File contains the code which captures the form information into a payload, before saving and passing the payload to "add_row.py".
    * _Maintenance_: If more information is required from solution submissions, this file will need to be updated with the specific fields and instructions for collecting this information. Otherwise, no regular maintenance is required.
* update-catalog.yml
    * _Description_: File contains the code which collects the information from the form entry, loads it into a payload before saving as an environment variable.
    * _Maintenance_: If changes are made to the "new-catalog-entry.yml" form, this file will need to be updated with code to handle the payload and variable creation. Otherwise, no regular maintenance is required.
* add_row.py
    * _Description_: File contains the code which transforms and loads the payload from the form entry, before adding the transformed information into the "catalog.md" for public display.
    * _Maintenance_: If changes are made to the "new-catalog-entry.yml" form, this file will need to be updated with code to handle ingesting and transforming the changed information. Otherwise, no regular maintenance is required.
* catalog.md
    * _Description_: File contains the instructions and formatting which presents the catalog as a public webpage. This file is also appended every time a new solution form is submitted, with the updated information being inserted at the bottom of the table on the page.
    * _Maintenance_: Over time, file will need to be maintained to reflect the latest instructions for how to read and submit solutions to the catalog. Any changes to the information captured should be reflected in the instructions at the top of the page. If there are manual modifications or corrections submitted by solution providers, this file will need to be manually edited before being committed and redeployed. This should only be done as a last resort measure, and instead solution providers should ensure their information is correct before submitting.
    * **Important: any changes to the file must not place ANY text below the catalog table, if there is text below the table it will cause the "add_row.py" script to malfunction and will change the page formatting.**
* README.md
    * _Description_: File contains basic information for the repository, including file structure, file descriptions, maintenance, usage, authors, and version history.
    * _Maintenance_: Updates will need to be made as changes to files, structures, or usage occurs. All updates should be reflected in the version history at the bottom of the page.

## Authors

* Colin Bradshaw - Colin.Bradshaw@PACONSULTING.COM
* Luke Thompson - Luke.Thompson@PACONSULTING.COM

## Version History

* 1.0 - 02/07/2024
	* First release: Insert github form answers into a markdown table.
