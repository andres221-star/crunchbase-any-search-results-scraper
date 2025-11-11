thonimport json

def export_to_json(data, file_name="data_output.json"):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)