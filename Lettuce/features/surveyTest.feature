Feature: Test 1, Complete Test
Scenario: Fill out fields

  Given I go to "https://www.webtestapp.com/"
  When I start my test
  And I enter "Google Test" as Test Name
  And I complete the URL "maps"
  And I search for "Click on Element" in the dropdown
  And I add test step
  And I search for "Count"
  And I delete step
  And I run test
