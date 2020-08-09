# HearQAChallenge

## Good to know:
- UI tests have been done using Python 3.6 and Pytest 6.0.1 and Selenium Webdriver
- API testcases have been written using SOAP UI
- The following tests have not been completed:
	* Exit intent (UI test)
	*API search query

## Where to find the tests
UI tests will found in CodeChallenge folder and API test is represented by the chuckNorris xml file


## How to execute the tests
### For the UI tests
1. copy the tests to a local machine
2. In a terminal/console, go into the CodeChallenge/TestSuites/ and execute the following command
pytest --html=report.html -v -s
3. In the CodeChallenge/TestSuites/ folder path, report.html file will be created along wih a logfile.log with all the logs created during the execution
