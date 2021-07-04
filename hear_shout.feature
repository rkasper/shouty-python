Feature: Hearing a shout

  Shouty is a social networking application for people that are located close to each other

  Rule: Shouts have a range of approximately 1000 metres

    Scenario: In range shout is heard
        Given Lucy is at 0, 0
        And Sean is at 0, 900
        When Sean shouts
        Then Lucy should hear Sean

   Scenario: Out of range shout is not heard
        Given Lucy is at 0, 0
        And Sean is at 800, 800
        When Sean shouts
        Then Lucy should hear nothing
