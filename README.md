Technical Challenge Senior Python Engineer

Candidate: Andres Balverde

Challenge Introduction
The challenge is to create a program that computes some basic statistics on a collection of small positive integers. You can assume all values will be less than 1,000. Implement this challenge in whatever programming language best highlights your skills. Also, please supply a README with details on how to setup and run your application.

Requirements
The DataCapture object accepts numbers and returns an object for querying statistics about the inputs. Specifically, the returned object supports querying how many numbers in the collection are less than a value, greater than a value, or within a range.

Conditions
1.	You cannot import a library that solves it instantly
2.	The methods add(), less(), greater(), and between() should have constant time O(1)
3.	The method build_stats() can be at most linear O(n)
4.	Apply the best practices you know
5.	Share a public repo with your project

Project Setup:
•	Create a local copy of the repository. 
•	Use Python 3.9 or superior version, create an environment for the project.
•	Install Requirements, i.e. through command line: 
	pip install –r requirements.txt

Project Execution:
Use one of the following options to execute the project:
•	From root folder, run main.py which includes a default test case to demonstrate all the features properly working
•	From /test folder, run test_cases.py using pytest, to verify every function is properly working under at least two different test cases for each.
o	Run all Test Functions using the command line:
	pytest test_cases.py

o	Run particular test cases to validate each of the functions: less, greater or between:
	pytest test_cases.py::test_greater_small_set
	pytest test_cases.py::test_greater_big_set

	pytest test_cases.py::test_less_small_set
	pytest test_cases.py::test_less_big_set

	pytest test_cases.py::test_between_small_set
	pytest test_cases.py::test_between_big_set


Solution Description:
A description of the solution, with helper graphics and examples, is provided under the file Solution.docx
