import requests
import argparse
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://www.11888.gr/antistrofh-anazhthsh-me-arithmo-thlefwnou/",
    "X-Requested-With": "XMLHttpRequest",
}

def lookup_phone(phone_number):
    url = f"https://www.11888.gr/antistrofh-anazhthsh-me-arithmo-thlefwnou/?phone={phone_number}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json() 
    else:
        print(f"Failed: {response.status_code}")
        return None

def parse_result(data, phone_number):
    if data and 'data' in data and 'results' in data['data'] and 'wp' in data['data']['results'] and len(data['data']['results']['wp']) > 0:
        result = data['data']['results']['wp'][0]

        # Extract name, phone number, and address
        name = f"{result['name']['first']} {result['name']['middle']} {result['name']['last']}"
        address = f"{result['address']['street1']} {result['address']['number1']}, {result['address']['postal_code']} - {result['address']['region']['name']}, {result['address']['subregion']['name']}"

        return f"Phone: {phone_number}\nName: {name}\nAddress: {address}\n"
    else:
        return f"Phone: {phone_number}\nName: NULL\nAddress: NULL\n"

def main():
    parser = argparse.ArgumentParser(description='Phone Lookup Program')
    parser.add_argument('numbers', nargs='?', help='A single phone number or a file containing multiple numbers')
    parser.add_argument('-f', '--file', action='store', help='Input file containing numbers')
    parser.add_argument('-o', '--output', action='store', help='Output file to save results')

    args = parser.parse_args()

    output_file = None
    if args.output:
        output_file = open(args.output, 'w', encoding='utf-8')

    numbers_to_lookup = []
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as file:
                numbers_to_lookup = file.readlines()
        except UnicodeDecodeError:
            print("Error: The input file encoding is not UTF-8. Please convert it to UTF-8 and try again.")
            return
    elif args.numbers:
        numbers_to_lookup = [args.numbers]

    for phone_number in numbers_to_lookup:
        phone_number = phone_number.strip()
        if phone_number:
            print(f"Looking up: {phone_number}")
            result = lookup_phone(phone_number)
            
            result_output = parse_result(result, phone_number) if result else f"Phone: {phone_number}\nName: NULL\nAddress: NULL\n"

            if output_file:
                output_file.write(result_output + "\n")
            else:
                print(result_output)

    if output_file:
        output_file.close()

if __name__ == "__main__":
    main()
