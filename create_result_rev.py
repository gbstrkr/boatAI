import re
import csv
import os

# テキストファイルを読み込む関数
def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='shift_jis') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# 単勝・複勝の番号とオッズを正規表現で抽出する関数
def extract_tansho_fukusho_odds(text_data):
    tansho_pattern = r"単勝\s+(\d+)\s+(\d+)"
    fukusho_pattern = r"複勝\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)"
    tansho_matches = re.findall(tansho_pattern, text_data)
    fukusho_matches = re.findall(fukusho_pattern, text_data)
    return tansho_matches, fukusho_matches

# 三連単・三連複の番号とオッズを正規表現で抽出する関数
def extract_trifecta_odds(text_data):
    trifecta_pattern = r"３連単\s+(\d+)-(\d+)-(\d+)\s+(\d+)"
    triple_pattern = r"３連複\s+(\d+)-(\d+)-(\d+)\s+(\d+)"
    trifecta_matches = re.findall(trifecta_pattern, text_data)
    triple_matches = re.findall(triple_pattern, text_data)
    return trifecta_matches, triple_matches

# CSVファイルに保存する関数
def save_to_csv(filename, data, headers):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

# メイン処理
if __name__ == "__main__":
    file_prefix = 'race_data/K20020'
    files = [f"{file_prefix}{i:01}.TXT" for i in range(1, 11)]

    combined_tansho_fukusho = []
    combined_trifecta_data = []

    for text_file_path in files:
        if os.path.exists(text_file_path):
            print(f"Reading file: {text_file_path}")
            text_data = read_text_file(text_file_path)
            if text_data:
                # 単勝・複勝のデータを抽出
                tansho_odds, fukusho_odds = extract_tansho_fukusho_odds(text_data)
                print(f"単勝データ: {tansho_odds}")  # 抽出結果を出力
                print(f"複勝データ: {fukusho_odds}")
                
                # 結果がない場合の警告
                if not tansho_odds:
                    print(f"No tansho odds found in {text_file_path}")
                if not fukusho_odds:
                    print(f"No fukusho odds found in {text_file_path}")
                
                for i, tansho in enumerate(tansho_odds):
                    if i < len(fukusho_odds) and len(fukusho_odds[i]) == 4:
                        combined_tansho_fukusho.append([
                            tansho[0], tansho[1], fukusho_odds[i][0], fukusho_odds[i][1], fukusho_odds[i][2], fukusho_odds[i][3]
                        ])

                # 三連単・三連複の番号とオッズを抽出
                trifecta_odds, triple_odds = extract_trifecta_odds(text_data)
                print(f"三連単データ: {trifecta_odds}")  # 抽出結果を出力
                print(f"三連複データ: {triple_odds}")

                if not trifecta_odds:
                    print(f"No trifecta odds found in {text_file_path}")
                if not triple_odds:
                    print(f"No triple odds found in {text_file_path}")

                for trifecta, triple in zip(trifecta_odds, triple_odds):
                    combined_trifecta_data.append([trifecta[0], trifecta[1], trifecta[2], trifecta[3], triple[3]])
            else:
                print(f"Failed to read data from {text_file_path}")
        else:
            print(f"File not found: {text_file_path}")

    # 単勝・複勝データをCSVに保存
    save_to_csv('odds_data.csv', combined_tansho_fukusho,
                ['単勝番号', '単勝オッズ', '複勝番号1', '複勝オッズ1', '複勝番号2', '複勝オッズ2'])
    print("単勝と複勝データが 'odds_data.csv' に保存されました。")

    # 三連単・三連複データをCSVに保存
    save_to_csv('trifecta_combined_data.csv', combined_trifecta_data,
                ['1着', '2着', '3着', '三連単オッズ', '三連複オッズ'])
    print("三連単と三連複データが 'trifecta_combined_data.csv' に保存されました。")
