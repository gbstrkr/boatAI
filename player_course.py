import pandas as pd

# テキストファイルのパス
file_path = './data/2020_f.txt'

# 正しいエンコーディングを指定してテキストファイルを読み込み
with open(file_path, 'r', encoding='shift_jis') as file:
    lines = file.readlines()
for i in range (6):
    # データの変換処理
    data_records = []
    for line in lines:
        record = {
            "登録": line[0:4].strip(),
            f"{i+1}コース進入回数": line[72+i*13:75+i*13].strip(),
            f"{i+1}コース複勝率": line[75+i*13:79+i*13].strip(),
            f"{i+1}コース平均スタートタイミング": line[79+i*13:82+i*13].strip(),
            f"{i+1}コース平均スタート順位": line[82+i*13:85+i*13].strip(),
            f"{i+1}コース1着回数": line[188+i*34:191+i*34].strip(),
            f"{i+1}コース2着回数": line[191+i*34:194+i*34].strip(),
            f"{i+1}コース3着回数": line[194+i*34:197+i*34].strip(),
            f"{i+1}コース4着回数": line[197+i*34:200+i*34].strip(),
            f"{i+1}コース5着回数": line[200+i*34:203+i*34].strip(),
            f"{i+1}コース6着回数": line[203+i*34:206+i*34].strip(),
            f"{i+1}コースF回数": line[206+i*34:208+i*34].strip(),
            f"{i+1}コースL0回数": line[208+i*34:210+i*34].strip(),##
            f"{i+1}コースL1回数": line[210+i*34:212+i*34].strip(),
            f"{i+1}コースK0回数": line[212+i*34:214+i*34].strip(),
            f"{i+1}コースK1回数": line[214+i*34:216+i*34].strip(),
            f"{i+1}コースS0回数": line[216+i*34:218+i*34].strip(),
            f"{i+1}コースS1回数": line[218+i*34:220+i*34].strip(),
            f"{i+1}コースS2回数": line[220+i*34:222+i*34].strip()
        }
        data_records.append(record)

    # データフレームに変換
    df = pd.DataFrame(data_records)

    # CSVファイルに保存
    csv_file_path = f'course{i+1}_output.csv'
    df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')  # utf-8-sigを指定して保存

print(f"データは以下のCSVファイルに保存されました: {csv_file_path}")
