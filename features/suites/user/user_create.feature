Feature: New user can be created

Scenario Outline: new user can be created
    Given user <user> not exists
    When create user <user> age <age>
    Then the response status code is 200
    Examples: user info
    |user   |age    |
    |admin  |30     |
    |root   |38     |
