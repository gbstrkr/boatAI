import pandas as pd

# CSVファイルの読み込み
df = pd.read_csv('./testdata/data0210.csv')

# コースごとのカラム名を指定（1コースから6コースまで）
columns_to_merge = ['進入回数', '複勝率', '平均スタートタイミング', '平均スタート順位', '1着回数', '2着回数', '3着回数',
                '4着回数', '5着回数', '6着回数', 'F回数', 'L0回数', 'L1回数', 'K0回数', 'K1回数', 'S0回数', 'S1回数', 'S2回数']

# 結果を格納するためのデータフレーム
merged_data = pd.DataFrame()

for col in columns_to_merge:
    # 各コースのカラムを同じカテゴリに統合していく
    merged_data[f'コース{col}'] = df[[f'1コース{col}', f'2コース{col}', f'3コース{col}', f'4コース{col}', f'5コース{col}', f'6コース{col}']].fillna(0).sum(axis=1)

df = pd.concat([df, merged_data], axis=1)

# 結果をCSVとして保存する場合
for col in columns_to_merge:
    df = df.drop([f'1コース{col}', f'2コース{col}', f'3コース{col}', f'4コース{col}', f'5コース{col}', f'6コース{col}'], axis=1)



# 結果をCSVとして保存する場合
df.to_csv('cleaned_output.csv', index=False)
