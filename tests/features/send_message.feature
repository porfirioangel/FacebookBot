Feature: Enviar mensaje
  Como un usuario del sistema
  Quiero enviar un mensaje por medio del chat
  Con la finalidad de comunicar algo a una persona

  Scenario: Enviar mensaje a Haydé
    Given inicio sesión con las credenciales mi_email y mi_password
    And ingreso a la url de perfil de un amigo: facebook_url
    When selecciono la opción para enviar mensaje
    And envío el mensaje Hola guapa
    Then el mensaje es mostrado en la ventana de chat