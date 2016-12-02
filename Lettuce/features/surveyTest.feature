Feature: Test 1, Complete Test
Scenario: Fill out fields

  Given I go to "https://www.webtestapp.com/"
  When I enter a website "http://www.google.com"
  And I start my test
  And I enter "Google Test" as Test Name
  And I search for "Click on Element" in the dropdown
