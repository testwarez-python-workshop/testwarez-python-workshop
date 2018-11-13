Feature: Reading users details
  As a data manager
  I want to read user detail
  So that I can deliver proper information

  @smoke
  Scenario: Check if database not empty
    Given server is responding
    Then I can get all data


  @smoke
  Scenario: Check if database consist of proper data
    Given server is responding
    When I get all data
    Then I can see following parameters
    |user|name        |
    |dejv|Dawid Pacia |
    |yoloxd|Bart Szulc|

  @empty_db
  Scenario Outline: Check if database consist of proper data
    Given server is responding
    When I get "<user>" data
    Then I can see name "<name>"

    Examples:
    |user|name|
    |dejv  |Dawid Pacia|
    |yoloxd|Bart Szulc |
