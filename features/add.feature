Feature: Adding

  Scenario: add two numbers
     Given we have math_complicated imported
      When we call add with "1" and "5"
      Then it will return "6"

  Scenario: add two negative numbers
     Given we have math_complicated imported
      When we call add with "-1" and "-5"
      Then it will return "-6"
