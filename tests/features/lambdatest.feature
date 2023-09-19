Feature: Lambdatest
  Converter files

    Scenario Outline: Test JSON to XML
    Given a JSON file is prepared: <json_file_name>
    And a XML file is prepared: <xml_file_name>
    When convert JSON to XML
    Then compare expected and actual XML
    Examples:
      | json_file_name     | xml_file_name    |
      | 1.json             | 1.xml            |
      | 2.json             | 2.xml            |


    Scenario Outline: Test extract TXT from JSON
    Given a JSON file is prepared: <json_file_name>
    And a TXT file is prepared: <txt_file_name>
    When extract TXT from JSON
    Then compare expected and actual TXT
    Examples:
      | json_file_name     | txt_file_name    |
      | 1.json             | 1.txt            |
      | 2.json             | 2.txt            |


    Scenario Outline: Test YAML validator
    Given a YAML file is prepared: <yaml_file_name>
    When validation YAML
    Then compare expected and actual string
    Examples:
      | yaml_file_name     |
      | 1.yml              |
      | 2.yml              |


    Scenario Outline: Test JSON to YAML
    Given a JSON file is prepared: <json_file_name>
    And a YAML file is prepared: <yaml_file_name>
    When convert JSON to YAML
    Then compare expected and actual YAML
    Examples:
      | json_file_name     | yaml_file_name    |
      | 1.json             | 1.yml             |
      | 2.json             | 2.yml             |


    Scenario Outline: Test XML to YAML
    Given a XML file is prepared: <xml_file_name>
    And a YAML file is prepared: <yaml_file_name>
    When convert XML to YAML
    Then compare expected and actual YAML
    Examples:
      | xml_file_name      | yaml_file_name    |
      | 1.xml              | 1.yml             |
      | 2.xml              | 2.yml             |


    Scenario Outline: Test YAML to JSON
    Given a YAML file is prepared: <yaml_file_name>
    And a JSON file is prepared: <json_file_name>
    When convert YAML to JSON
    Then compare expected and actual JSON
    Examples:
      | yaml_file_name     | json_file_name     |
      | 1.yml              | 1.json             |
      | 2.yml              | 2.json             |
