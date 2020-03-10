jsomark
#######

.. image:: https://travis-ci.org/knowark/jsomark.svg?branch=master
    :target: https://travis-ci.org/knowark/jsomark

.. image:: https://codecov.io/gh/knowark/jsomark/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/knowark/jsomark

JSON <-> XML parsing and composing convention.


What is jsomark?
================

jsomark is a JSON to XML translation convention. jsomark accepts json in an
standardized format and converts it to XML. It should as well reverse the
operation and produce a JSON document from an XML one.

Usage
=====

To **create an XML** from a **JSON** document just use
the **json_to_xml** function:

.. code-block:: python

    from jsomark import json_to_xml
    
    json_data = b'{"hello": "world"}'

    xml_data = json_to_xml(json_data)

    assert xml_data == b'<hello>world</hello>'

*jsomark* also supports more complex documents, like **nested json**
structures and Python json serializable **dictionaries**:


.. code-block:: python

    from jsomark import json_to_xml
    
    json_data = b'{"hello": "world"}'

    xml_data = json_to_xml(json_data)

    assert xml_data == (
        b'<Company><Name>Knowark</Name><Country>Colombia</Country></Company>')

