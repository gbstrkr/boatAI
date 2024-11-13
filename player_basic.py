import pandas as pd

# テキストファイルのパス
file_path = './data/2020_f.txt'

# 正しいエンコーディングを指定してテキストファイルを読み込み
with open(file_path, 'r', encoding='shift_jis') as file:
    lines = file.readlines()

# データの変換処理
data_records = []
for line in lines:
    record = {
        "登番": line[0:4].strip(),
        "名前漢字": line[4:12].strip(),
        "名前カナ": line[12:26].strip(),
        "支部": line[26:29].strip(),
        "級": line[29:31].strip(),
        "年号": line[31:32].strip(),
        "生年月日": line[32:38].strip(),
        "性別": line[38:39].strip(),
        "年齢": line[39:41].strip(),
        "身長": line[41:44].strip(),
        "体重": line[44:46].strip(),
        "血液型": line[46:48].strip(),
        "勝率": line[48:52].strip(),##
        "複勝率": line[52:56].strip(),
        "1着回数": line[56:59].strip(),
        "2着回数": line[59:62].strip(),
        "出走回数": line[62:65].strip(),
        "優出回数": line[65:67].strip(),
        "優勝回数": line[67:69].strip(),
        "平均スタートタイミング": line[69:72].strip(),
        "前期級": line[150:152].strip(),
        "前々期級": line[152:154].strip(),
        "前々々期級": line[154:156].strip(),
        "前期能力指数": line[156:160].strip(),
        "今期能力指数": line[160:164].strip(),
        "期": line[168:169].strip()
    }
    data_records.append(record)

# データフレームに変換
df = pd.DataFrame(data_records)

# CSVファイルに保存
csv_file_path = 'output.csv'
df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')  # utf-8-sigを指定して保存

print(f"データは以下のCSVファイルに保存されました: {csv_file_path}")
