Feature: Managing users details
    As a customer


  @smoke
  Scenario:
    Given server is responding
    When I get all data
    Then I can see following parameters
    |user|name        |
    |dejv|Dawid Pacia |
    |yoloxd|Bart Szulc|


  Scenario Outline:
    Given server is responding
    When I get "<user>" data
    Then I can see name "<name>"

    Examples:
    |user|name|
    |dejv  |Dawid Pacia|
    |yoloxd|Bart Szulc |
