# CONVERTING XML TO DICTIONARY AND BACK (PYTHON RECIPE)
# http://code.activestate.com/recipes/573463-converting-xml-to-dictionary-and-back/

# PRINT PRETTY
# https://stackoverflow.com/questions/17402323/use-xml-etree-elementtree-to-print-nicely-formatted-xml-files/17402424

# FILE WRITE UNICODE
# https://www.pitt.edu/~naraehan/python3/reading_writing_methods.html


from xml.etree import ElementTree
from xml.dom import minidom
import inflect
p = inflect.engine()

class DictToXml():
    pretty = True
    encoding = 'utf-8'
    indent = '    ' # 4 spaces

    @classmethod
    def convert(cls, xmldict, roottag):
        my_dict = {}
        my_dict[roottag] = xmldict

        root = ElementTree.Element(roottag)
        try:
            cls.__ConvertDictToXmlRecurse(root, my_dict[roottag])
            xml = cls.__prettify(root)
            return xml
        except Exception as e:
            raise NotSupportFormatException('Not support given dict format')

    @classmethod
    def __ConvertDictToXmlRecurse(cls, parent, dictitem):
        assert type(dictitem) is not type([])

        if isinstance(dictitem, dict):
            for (tag, child) in dictitem.items():
                if str(tag) == '_text':
                    parent.text = str(child)
                elif type(child) is type([]):
                    # iterate through the array and convert
                    for listchild in child:
                        sing_tag = p.singular_noun(tag)
                        if sing_tag:
                            tag = sing_tag
                        
                        elem = ElementTree.Element(tag)
                        parent.append(elem)
                        cls.__ConvertDictToXmlRecurse(elem, listchild)
                else:                
                    elem = ElementTree.Element(tag)
                    parent.append(elem)
                    cls.__ConvertDictToXmlRecurse(elem, child)
        else:
            parent.text = str(dictitem)

    @classmethod
    def __prettify(cls, elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = ElementTree.tostring(elem, encoding=cls.encoding)
        if cls.pretty:
            reparsed = minidom.parseString(rough_string)
            pretty_string = reparsed.toprettyxml(indent=cls.indent)
            return pretty_string
        else:
            return rough_string


class NotSupportFormatException(Exception):
    pass

if __name__ == '__main__':
    my_dict = {
        'name':'Cube',
        'age': 25,
        'object': [
            {
                'name': 'sponge',
                'bndbox': {
                    'xmin': 82
                }
            },
            {
                'name': 'sponge',
                'bndbox': {
                    'xmin': 83
                }
            },
            {
                'name': 'sponge',
                'bndbox': {
                    'xmin': 84
                }
            }]
    }

    xml = DictToXml.convert(my_dict, 'annotation')
    myfile = open("output.xml", "w", encoding='utf-8')  
    myfile.write(xml)