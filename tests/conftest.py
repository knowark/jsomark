from pytest import fixture


@fixture
def simple_dict():
    return {
        "Hello": "World"
    }


@fixture
def simple_json():
    return '''{
        "Hello": "World"
    }'''


@fixture
def nested_json():
    return '''{
        "Invoice": {
            "ID": "F0001",
            "IssueDate": "2018-09-13",
            "IssueTime": "00:31:40-05"
        }
    }'''


@fixture
def nested_complex_json():
    return '''{
        "Invoice": {
            "ID": "F0001",
            "Party": {
                "PartyName": "Knowark"
            }
        }
    }'''


@fixture
def nested_attributes_json():
    return '''{
        "Invoice": {
            "ID": {
                "&": {"languageID": "es", "schemeID": "3"},
                "#": "F0001"
            }
        }
    }'''


@fixture
def nested_list_json():
    return '''{
        "Invoice": {
            "ID":  "F0001",
            "InvoiceLine": [
                {"Amount": 10},
                {"Amount": 20},
                {"Amount": 30}
            ]
        }
    }'''


@fixture
def nested_namespaces_json():
    return '''{
        "Invoice": {
            "cbc:ID": "F0001",
            "cac:Party": {
                "cbc:PartyName": "Knowark"
            }
        }
    }'''


@fixture
def not_basic_dict():
    return {
        "Invoice": {
            "key": lambda x: "value"
        }
    }
