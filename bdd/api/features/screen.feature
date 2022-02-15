@api
Feature: Главный экран

  Scenario: Получение Главный экран без авторизации
    Given Я отправляю GET запрос /mobile/api/v5/screens/main
