# DemoTeam Project

## Overview
This project demonstrates a simple deployment of a "Hello World" Python application to Databricks using GitHub Actions and Databricks Asset Bundles.

## Setup
1. Ensure Python and Databricks CLI are installed.
2. Set up the necessary Azure AD and Databricks configurations.
3. Clone this repository and push changes to trigger the deployment.

## Usage
Once deployed, the application will simply print "Hello World" in a Databricks notebook environment.

## Testing
Run the tests using the command:
```bash
python -m unittest discover -s tests
