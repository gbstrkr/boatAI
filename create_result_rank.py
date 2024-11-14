import re
import pandas as pd
"""
txtからデータを抽出しcsvに変換
"""
# テキストファイルのパス
file_path = '/Users/issahirasawa/Desktop/kyotei/race0210/K200210.TXT'

# テキストファイルを読み込み
# with open(file_path, 'r', encoding='utf-8') as file:
with open(file_path, 'r', encoding='shift_jis') as file:
    lines = file.readlines()

# 「着」「艇」「登番」「選手名」「モーター」「ボート」「展示」「進入」「スタートタイミング」「レースタイム」を抽出
# 選手名に漢字、ひらがな、カタカナ、スペースを許可
pattern = re.compile(
    r'^\s*(\d{1,2}|F|S0|S1|S2|L0|L1|K0|K1)\s+'    # 着
    r'(\d+)\s+'                                     # 艇番
    r'(\d+)\s+'                                     # 登録番号
    r'([\u4e00-\u9fff\u3040-\u309F\u30A0-\u30FF々\s]+)\s+'  # 選手名
    r'(\d+)\s+'                                     # モーター
    r'(\d+)\s+'                                     # ボート
    r'(\d+\.\d+|K|\.\s*)\s+'                        # 展示
    r'(\d+)?\s*'                                    # 進入（空白を許可）
    r'(F\d+\.\d+|\d+\.\d+|F|K|\.\s*)\s+'            # スタートタイミング
    r'([\d\.]+|F|L|K|\.\s*)'                        # レースタイム
)

# データを格納するリスト
data_records = []

# テキストデータから各カラムを抽出
for line in lines:
    match = pattern.match(line)
    if match:
        data_records.append(list(match.groups()))

# カラム名を定義
columns = ["着", "艇番", "登録", "選手名", "モーター",
           "ボート", "展示", "進入", "スタートタイミング", "レースタイム"]

# 抽出したデータをデータフレームに変換
df = pd.DataFrame(data_records, columns=columns)

# CSVファイルに保存
csv_file_path = 'result.csv'
df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

print(f"フライング情報や欠損データも含めたデータが以下のCSVファイルに保存されました: {csv_file_path}")
