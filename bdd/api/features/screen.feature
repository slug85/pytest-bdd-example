@api
Feature: Главный экран

  Scenario: Получение Главный экран без авторизации
    Given Я отправляю GET запрос /api/v5/screens/main
