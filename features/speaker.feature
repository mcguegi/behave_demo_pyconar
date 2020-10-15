# Created by mguerrerogir at 4/10/20
Feature: participate as a speaker
"""
    As a person i want to participate as a speaker and submit a
    talk at PyconAr 2020.
  """"

  Scenario: register as a Speaker
    Given I navigate to register page
    And I enter valid information about me
    When I click on Submit button
    Then  register is successful
    # Enter steps here