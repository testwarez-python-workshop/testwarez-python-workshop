Feature: Adding users

  @empty_db
  Scenario Outline: Checking if users added
    When I create "<user>" user with following data
    |key  |value |
    |name |<name>|
    |pet  |<pet>   |
    |hobby|<hobby> |
    And I get "<user>" data
    Then I can see name "<name>"

    Examples:
    |user|name|hobby|pet|
    |dd  |dd  |dd   |dd  |
    |ddd |ddd |ddd  |ddd |
    |c   |c   |c    |c   |
    |cc  |c   |c    |c   |

  Scenario: Check if correct number of user created
    When I get all data
    Then number of users is "4"