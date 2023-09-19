from utils.file_utils import read_data_file
from pytest_bdd import given, when, then, scenarios, parsers

scenarios("lambdatest.feature")


@given(parsers.parse("a YAML file is prepared: {yaml_file_name}"), target_fixture="context")
def a_yaml_file_is_prepared(yaml_file_name, context):
    input_yaml = read_data_file(f"yaml/{yaml_file_name}")
    context["yaml"] = input_yaml

    return context


@given(parsers.parse("a JSON file is prepared: {json_file_name}"), target_fixture="context")
def a_json_file_is_prepared(json_file_name, context):
    input_json = read_data_file(f"json/{json_file_name}")
    context["json"] = input_json

    return context


@given(parsers.parse("a XML file is prepared: {xml_file_name}"), target_fixture=("context", "lambdatest_service"))
def a_xml_file_is_prepared(xml_file_name, context, lambdatest_service):
    expected_xml = read_data_file(f"xml/{xml_file_name}")
    mini_expected_xml = lambdatest_service.minify_xml(expected_xml)
    context["mini_expected_xml"] = mini_expected_xml

    return context


@given(parsers.parse("a TXT file is prepared: {txt_file_name}"), target_fixture="context")
def a_txt_file_is_prepared(txt_file_name, context):
    expected_txt = read_data_file(f"txt/{txt_file_name}")
    context["expected_txt"] = expected_txt

    return context


@when("convert YAML to JSON", target_fixture=("context", "lambdatest_service"))
def convert_yaml_to_json(context, lambdatest_service):
    actual_json = lambdatest_service.yaml_to_json(context["json"])
    context["actual_json"] = actual_json

    return context


@when("convert XML to YAML", target_fixture=("context", "lambdatest_service"))
def convert_xml_to_yaml(context, lambdatest_service):
    actual_yaml = lambdatest_service.xml_to_yaml(context["mini_expected_xml"])
    context["actual_yaml"] = actual_yaml

    return context


@when("convert JSON to YAML", target_fixture=("context", "lambdatest_service"))
def convert_json_to_yaml(context, lambdatest_service):
    actual_yaml = lambdatest_service.json_to_yaml(context["json"])
    context["actual_yaml"] = actual_yaml

    return context


@when("validation YAML", target_fixture=("context", "lambdatest_service"))
def validation_yaml(context, lambdatest_service):
    response = lambdatest_service.yaml_validator(context["yaml"])
    context["response"] = response

    return context


@when("extract TXT from JSON", target_fixture=("context", "lambdatest_service"))
def extract_text_from_json(context, lambdatest_service):
    actual_txt = lambdatest_service.extract_text_from_json(context["json"])
    context["actual_txt"] = actual_txt

    return context


@when("convert JSON to XML", target_fixture=("context", "lambdatest_service"))
def convert_json_to_xml(context, lambdatest_service):
    actual_xml = lambdatest_service.json_to_xml(context["json"])
    mini_actual_xml = lambdatest_service.minify_xml(actual_xml)
    context["mini_actual_xml"] = mini_actual_xml

    return context


@then("compare expected and actual JSON", target_fixture="context")
def compare_expected_and_actual_json(context):
    assert context["actual_json"].replace(' ', '') == context["json"].replace('\n', '').replace(' ', '')


@then("compare expected and actual YAML", target_fixture="context")
def compare_expected_and_actual_yaml(context):
    assert context["actual_yaml"] == f"{context['yaml']}\n"


@then("compare expected and actual string", target_fixture="context")
def compare_expected_and_actual_string(context):
    assert context["response"] == "Valid YAML"


@then("compare expected and actual TXT", target_fixture="context")
def compare_expected_and_actual_TXT(context):
    assert context["actual_txt"] == context["expected_txt"]


@then("compare expected and actual XML", target_fixture="context")
def compare_expected_and_actual_XML(context):
    assert context["mini_actual_xml"] == context["mini_expected_xml"]
