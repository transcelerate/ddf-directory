# TransCelerate's DDF Catalog Hosting and Automation

The purpose of this document is to provide version/contact information and instructions for installation of the solution.

## Description

[Problem Statement goes here]

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

## Authors

* Colin Bradshaw - Colin.Bradshaw@PACONSULTING.COM

* Luke Thompson - Luke.Thompson@PACONSULTING.COM

## Version History

* 1.0 - 02/07/2024
	* First release: Insert github form answers into a markdown table.