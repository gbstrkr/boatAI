import re
import csv

# テキストファイルを読み込む関数（エンコーディングを指定）
def read_text_file(file_path):
    with open(file_path, 'r', encoding='shift_jis') as file:
        return file.read()

# 単勝・複勝の番号とオッズを正規表現で抽出する関数
def extract_tansho_fukusho_odds(text_data):
    # 単勝の正規表現パターン
    tansho_pattern = r"単勝\s+(\d+)\s+(\d+)"
    # 複勝の正規表現パターン：1組または2組のペアに対応
    fukusho_pattern = r"複勝\s+(\d+)\s+(\d+)(?:\s+(\d+)\s+(\d+))?"

    # 正規表現で抽出
    tansho_matches = re.findall(tansho_pattern, text_data)
    fukusho_matches = re.findall(fukusho_pattern, text_data)

    # 複勝の抽出結果を整形（空のマッチ部分を除外）
    formatted_fukusho = []
    for match in fukusho_matches:
        if match[2] and match[3]:  # 2組のペアがある場合
            formatted_fukusho.append((match[0], match[1], match[2], match[3]))
        else:  # 1組のペアのみの場合
            formatted_fukusho.append((match[0], match[1]))

    return tansho_matches, formatted_fukusho

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
        # ヘッダーを書き込む
        writer.writerow(headers)

        # データを書き込む
        for row in data:
            writer.writerow(row)

# メイン処理
if __name__ == "__main__":
    # テキストファイルのパス
    text_file_path = 'race_data/K200210.TXT'  # 必要に応じてファイルパスを変更

    # テキストファイルを読み込む
    text_data = read_text_file(text_file_path)

    # 単勝・複勝のデータを抽出
    tansho_odds, fukusho_odds = extract_tansho_fukusho_odds(text_data)

    # 抽出されたデータが不足していないか確認
    if len(tansho_odds) != len(fukusho_odds):
        print(f"Warning: The number of tansho entries ({len(tansho_odds)}) and fukusho entries ({len(fukusho_odds)}) do not match.")

    # 単勝と複勝のデータを1つのファイルにまとめて保存
    combined_tansho_fukusho = []
    for i, tansho in enumerate(tansho_odds):
        if i < len(fukusho_odds) and len(fukusho_odds[i]) == 4:
            combined_tansho_fukusho.append([
                tansho[0], tansho[1], fukusho_odds[i][0], fukusho_odds[i][1], fukusho_odds[i][2], fukusho_odds[i][3]
            ])
        else:
            print(f"Skipping entry {i} due to missing fukusho data.")

    save_to_csv('odds_data.csv', combined_tansho_fukusho,
                ['単勝番号', '単勝オッズ', '複勝番号1', '複勝オッズ1', '複勝番号2', '複勝オッズ2'])

    print("単勝と複勝データが 'odds_data.csv' に保存されました。")

    # 三連単と三連複の番号とオッズを抽出
    trifecta_odds, triple_odds = extract_trifecta_odds(text_data)

    # 三連単・三連複データを1着、2着、3着、三連単オッズ、三連複オッズにまとめる
    combined_trifecta_data = []
    for trifecta, triple in zip(trifecta_odds, triple_odds):
        combined_trifecta_data.append([trifecta[0], trifecta[1], trifecta[2], trifecta[3], triple[3]])

    # 三連単・三連複データをCSVに保存
    save_to_csv('trifecta_combined_data.csv', combined_trifecta_data,
                ['1着', '2着', '3着', '三連単オッズ', '三連複オッズ'])

    print("三連単と三連複データが 'trifecta_combined_data.csv' に保存されました。")
