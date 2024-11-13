import re
import csv

# Function to read the text file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='shift_jis') as file:
        return file.read()

# Function to extract odds for 単勝 and 複勝
def extract_odds(text_data):
    # Adjusted patterns for "単勝" and "複勝"
    tansho_pattern = r"単勝\s+(\d+)\s+(\d+)|単勝\s+不成立"
    fukusho_pattern = r"複勝\s+(\d+)\s+(\d+)\s*(\d*)\s*(\d*)|複勝\s+不成立"

    # Match and process results for 単勝
    tansho_matches = re.findall(tansho_pattern, text_data)
    tansho_processed = [(match[0], match[1]) if match[1] else ('', '') for match in tansho_matches]

    # Match and process results for 複勝
    fukusho_matches = re.findall(fukusho_pattern, text_data)
    fukusho_processed = [(match[0], match[1], match[2], match[3]) if match[1] else ('', '', '', '') for match in fukusho_matches]

    return tansho_processed, fukusho_processed

# Function to save to CSV
def save_to_csv(filename, data, headers):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)

# Main function
def main():
    file_path = './race_data/K200210.TXT'
    text_data = read_text_file(file_path)
    tansho_odds, fukusho_odds = extract_odds(text_data)

    # Combine data for CSV output
    combined_data = []
    for i, tansho in enumerate(tansho_odds):
        if i < len(fukusho_odds):
            fukusho = fukusho_odds[i]
            combined_data.append([tansho[0], tansho[1], fukusho[0], fukusho[1], fukusho[2], fukusho[3]])

    # Save combined data to CSV
    save_to_csv('odds_data.csv', combined_data, ['単勝番号', '単勝オッズ', '複勝番号1', '複勝オッズ1', '複勝番号2', '複勝オッズ2'])
    print("単勝と複勝のオッズが 'odds_data.csv' に保存されました。")

# Run the main function
main()
