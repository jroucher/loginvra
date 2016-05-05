Feature: Login section

  Scenario: [OK]Login vRA
    Given goto page
    When set "username" to "qa743jri.admin"
      And set "password" to "VMware01!"
      And login
    Then Open main section of App
      And userdata in header is equal to "Bienvenido/a, Organization Admin for qa743jri qa743jri.admin."

  Scenario: [NOK]Login vRA
    Given goto page
    When set "username" to "qa743jri.admin"
      And set "password" to "Pass_Falsa"
      And login
    Then Show Message "Las credenciales son incorrectas."

  Scenario: [OK]Login vCD
    Given goto page
    When set "username" to "qa743jri.admin"
      And set "password" to "VMware01!"
      And select choice "vcd"
      And login
    Then flash App is loaded

  Scenario: [NOK]Login vCD
  Given goto page
  When set "username" to "qa743jri.admin"
    And set "password" to "Pass_Falsa"
    And select choice "vcd"
    And login
  Then Show Message "La contraseña es incorrecta."
