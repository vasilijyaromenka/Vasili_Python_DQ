from pub_txt_functions import fider_path, write_involid_publications
from pub_data_classes import NewsData, SportNewsData, PrivateAddData
from pub_classes import News, PrivateAd, SportNews
import json
import os

def publish_json(folder_name = '', directory = ''):

    pub_types = {
        "news"          : {"data_class" : NewsData, "pub_class" : News},
        "ad"            : {"data_class" : PrivateAddData, "pub_class" : PrivateAd},
        "sport_news"    : {"data_class" : SportNewsData, "pub_class" : SportNews}
    }
    
    unparsed_data = []

    fider_folder = fider_path(folder_name, directory) # returns folder path

    json_files = [os.path.join(fider_folder, file) for file in os.listdir(fider_folder)  if os.path.isfile(os.path.join(fider_folder, file)) and file.endswith('.json')]

    if json_files:
        for json_file in json_files:
            try:
                json_dct = json.load(open (json_file))
                for dct in json_dct["pubs"]:
                    json_pub_type = dct.get("pub_type", '').lower()
                    if json_pub_type in pub_types.keys():
                        data_class = pub_types[json_pub_type]["data_class"]
                        fields = {f.name for f in data_class.__dataclass_fields__.values()} - {"pub_type", "status", "decision", "days_left"}
                        new_dct = {k: dct[k] for k in fields if k in dct and dct[k]}
                        record = data_class(**new_dct)

        
                        if record.status:
                            pub_cl = pub_types[json_pub_type]["pub_class"]()
                            pub_cl.publish_data(record)
                        else:
                            rec_json = json.dumps(dct , indent = 4, sort_keys = True)
                            unparsed_data.append(f"Bad {str(record.pub_type.capitalize())} JSON data\n{record.decision} \n{rec_json}")

                    else:
                        rec_json = json.dumps(dct , indent = 4, sort_keys = True)
                        unparsed_data.append(f"Wrong JSON publication type \n{rec_json}")
                
                os.remove(json_file)

            except Exception as e:
                unparsed_data.append(f"An unexpected error while reading json files: {e}")

    else:   
        unparsed_data.append(f"No JSON files found in the folder")

    write_involid_publications( unparsed_data)
                                     
    return None
                
if __name__ == '__main__':
    publish_json()

