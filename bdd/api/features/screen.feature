@api
Feature: Главный экран

  Scenario: Получение Главный экран
    Given Я авторизуюсь в апи
    Then Я отправляю GET запрос /mobile/api/v5/screens/main
