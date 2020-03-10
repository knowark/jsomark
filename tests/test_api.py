from pytest import fixture
from lxml.etree import tostring
from jsomark import json_to_xml


def test_json_to_xml(nested_namespaces_json):
    namespaces = {
        None: 'urn:oasis:names:specification:ubl:schema:xsd:Invoice-2',
        'cbc': ("urn:oasis:names:specification:ubl:"
                "schema:xsd:CommonBasicComponents-2"),
        'cac': ("urn:oasis:names:specification:ubl:"
                "schema:xsd:CommonAggregateComponents-2")
    }

    result = json_to_xml(nested_namespaces_json, namespaces=namespaces)

    assert result == (
        b'<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:'
        b'Invoice-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:'
        b'xsd:CommonBasicComponents-2" xmlns:cac="urn:oasis:names:'
        b'specification:ubl:schema:xsd:CommonAggregateComponents-2">'
        b'<cbc:ID>F0001</cbc:ID><cac:Party><cbc:PartyName>Knowark'
        b'</cbc:PartyName></cac:Party></Invoice>')


def test_json_to_xml_dict(simple_dict):
    result = json_to_xml(simple_dict)
    assert result == b'<Hello>World</Hello>'
