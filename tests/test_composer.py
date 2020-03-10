from pytest import fixture
from lxml.etree import tostring
from jsomark.composer import Composer


@fixture
def composer():
    return Composer()


def test_composer_simple(composer, simple_json):
    element = composer.compose(simple_json)
    assert tostring(element) == b'<Hello>World</Hello>'


def test_composer_nested(composer, nested_json):
    element = composer.compose(nested_json)

    assert tostring(element) == (
        b'<Invoice><ID>F0001</ID>'
        b'<IssueDate>2018-09-13</IssueDate>'
        b'<IssueTime>00:31:40-05</IssueTime></Invoice>')


def test_composer_nested_complex(composer, nested_complex_json):
    element = composer.compose(nested_complex_json)

    assert tostring(element) == (
        b'<Invoice><ID>F0001</ID>'
        b'<Party><PartyName>Knowark</PartyName>'
        b'</Party></Invoice>')


def test_composer_attributes(composer, nested_attributes_json):
    element = composer.compose(nested_attributes_json)

    assert tostring(element) == (
        b'<Invoice><ID languageID="es" schemeID="3">F0001</ID></Invoice>')


def test_composer_list(composer, nested_list_json):
    element = composer.compose(nested_list_json)
    assert tostring(element) == (
        b'<Invoice><ID>F0001</ID>'
        b'<InvoiceLine><Amount>10</Amount></InvoiceLine>'
        b'<InvoiceLine><Amount>20</Amount></InvoiceLine>'
        b'<InvoiceLine><Amount>30</Amount></InvoiceLine>'
        b'</Invoice>')


def test_composer_namespaces(composer, nested_namespaces_json):
    namespaces = {
        None: 'urn:oasis:names:specification:ubl:schema:xsd:Invoice-2',
        'cbc': ("urn:oasis:names:specification:ubl:"
                "schema:xsd:CommonBasicComponents-2"),
        'cac': ("urn:oasis:names:specification:ubl:"
                "schema:xsd:CommonAggregateComponents-2")
    }
    composer.namespaces = namespaces

    element = composer.compose(nested_namespaces_json)
    assert tostring(element) == (
        b'<Invoice xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:'
        b'CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:'
        b'specification:ubl:schema:xsd:CommonBasicComponents-2" '
        b'xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2">'
        b'<cbc:ID>F0001</cbc:ID><cac:Party><cbc:PartyName>Knowark'
        b'</cbc:PartyName></cac:Party></Invoice>'
    )
