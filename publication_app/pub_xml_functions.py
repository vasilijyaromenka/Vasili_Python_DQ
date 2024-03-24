from pub_txt_functions import fider_path, write_involid_publications
from pub_data_classes import NewsData, SportNewsData, PrivateAddData
from pub_classes import News, PrivateAd, SportNews
import os
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString

def publish_xml(folder_name = '', directory = ''):

    pub_types = {
        "news"          : {"data_class" : NewsData, "pub_class" : News},
        "ad"            : {"data_class" : PrivateAddData, "pub_class" : PrivateAd},
        "sport_news"    : {"data_class" : SportNewsData, "pub_class" : SportNews}
    }
    
    unparsed_data = []

    fider_folder = fider_path(folder_name, directory) # returns folder path

    xml_files = [os.path.join(fider_folder, file) for file in os.listdir(fider_folder)  if os.path.isfile(os.path.join(fider_folder, file)) and file.endswith('.xml')]

    if xml_files:
        for xml_file in xml_files:
            try:
                tree = ET.parse(xml_file)
                root = tree.getroot()

                for pub in root.findall('pub'):
                    pub_type = pub.get('pub_type')
                    if pub_type and pub_type.lower() in pub_types:
                        data = {child.tag: child.text for child in pub if child.text and child.text.strip()}
                        data_class = pub_types[pub_type.lower()]["data_class"]
                        record = data_class(**data)

                        if record.status:
                            pub_cl = pub_types[pub_type.lower()]["pub_class"]()
                            pub_cl.publish_data(record)
                        else:
                            xml_string = ET.tostring(pub, encoding='utf-8').decode('utf-8')
                            dom = parseString(xml_string)
                            pretty_xml = dom.toprettyxml(indent="\t")
                            unparsed_data.append(f"Bad {pub_type.capitalize()} XML data\n{record.decision}\n{pretty_xml}")
                    else:
                        unparsed_data.append(f"Wrong XML publication type\n{ET.tostring(pub, encoding='utf-8')}")

                os.remove(xml_file)
            except Exception as e:
                unparsed_data.append(f"An unexpected error while reading XML files: {e}")
    else:   
        unparsed_data.append(f"No XML files found in the folder")

    write_involid_publications(unparsed_data)

    return None

if __name__ == '__main__':
    publish_xml()