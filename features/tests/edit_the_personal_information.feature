# Created by Shaheena at 11/8/24

Feature: Edit personal information from the settings

#  Scenario: User can go to settings and edit the personal information
#    Given Open the main page https://soft.reelly.io
#    When Log in to the page
#    And Click on settings option
#    And Click on Edit profile option
#    Then some test information in the input fields
#    And Check the right information is present in the input fields
#    Then Check “Close” and “Save Changes” buttons are available and clickable

  Scenario: User can go to settings and edit the personal information (FOR MOBILE CONFIG)
    Given Open the main page https://soft.reelly.io
    When Log in to the page
    And Click on Main Menu
    And Click Profile icon
    And Click on Edit profile option
    Then some test information in the input fields
    And Check the right information is present in the input fields
    Then Check “Close” and “Save Changes” buttons are available and clickable