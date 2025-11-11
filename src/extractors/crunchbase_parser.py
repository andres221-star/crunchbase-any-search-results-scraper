thonimport json

def extract_company_info(raw_data):
    parsed_data = []
    for entry in raw_data:
        company_info = {
            "company_name": entry.get("company_name"),
            "funding_round": entry.get("funding_round"),
            "acquisition": entry.get("acquisition"),
            "people": entry.get("people")
        }
        parsed_data.append(company_info)
    return parsed_data