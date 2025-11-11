thonimport requests
import json
from bs4 import BeautifulSoup

def fetch_data(url, cookies):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Cookie': cookies
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to fetch page content")
    return response.text

def parse_crunchbase_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = []

    companies = soup.find_all('div', class_='company-details')  # Adjust based on actual HTML structure
    for company in companies:
        company_name = company.find('a', class_='company-name').text.strip()
        funding_round = company.find('span', class_='funding-round').text.strip()
        acquisition = company.find('span', class_='acquisition').text.strip()
        people = [{'name': person.text.strip(), 'role': role.text.strip()} for person, role in zip(company.find_all('span', class_='person-name'), company.find_all('span', class_='role'))]

        data.append({
            'company_name': company_name,
            'funding_round': funding_round,
            'acquisition': acquisition,
            'people': people
        })
    return data

def save_to_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    url = "https://www.crunchbase.com/search"
    cookies = "your_session_cookie_here"
    html = fetch_data(url, cookies)
    data = parse_crunchbase_page(html)
    save_to_json(data, 'output.json')

if __name__ == "__main__":
    main()