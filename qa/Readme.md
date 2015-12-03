#Liars Dice QA

These tests were written to test the RESTful endpoints served up by node.js. They do not test all the logic of the code. Unit tests should be added to the project to get more thorough test coverage. 

##Continuous Integration
Continuous integration tests have been set up in Jenkins. It polls the dev branch on github every 10 minutes and if it sees a change, it will check out the project, set up an environment to run on localhost:8080 and kick off the tests. The job will save the results of the test (*results.html*) as an archived item. 

What is missing from this set up is alerting. In a real world scenario, I would set up Jenkins to send emails and/or send notifications through IM on failure of a test.

If this were a larger, more complex system, a test environment, with servers and databases dedicated to QA would be used, instead of localhost.  Also, ideally, tests should be written using a database that can be pre-loaded with known data. 

You can take a look at the Jenkins job at [http://test.richmeglino.com:8081/jenkins/job/test-liars-dice/](http://test.richmeglino.com:8081/jenkins/job/test-liars-dice/) 

I have also added the jenkins job configuration file in qa/jenkins-job-config.

##The Tests
The tests were written in Python using Python's unittest framework. The qa portion of the project lives in the directory named 'qa'. The Python code lives in qa/LiarsDiceQA. The scripts directory holds the script that runs Jenkins. 

Additional tests can be written and placed in qa/LiarsDiceQA/tests.  Once the tests are ready to be used, simply add an import statement to qa/LiarsDiceQA/test/\__init__.py and they will automatically be added to the test suite.
