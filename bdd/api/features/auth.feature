@api
Feature: Авторизация

  Scenario: Получение токена
    Given Я получаю PIN
    Then Я получаю access_token