import pandas as pd

# CSVファイルを読み込み
df = pd.read_csv('i.csv')

# データの2行目以降を取得し、インデックスをリセットして再構成
df_data = df.iloc[1:].copy().reset_index(drop=True)

# 6行ごとに「予測」カラムの値に基づいて「予測着順」を付ける関数
def assign_ranks(group):
    group['予測着順'] = group['予測'].rank(ascending=False, method='first').astype(int)
    return group

# 6行ごとにグループ化し、「予測着順」カラムを追加
df_data = df_data.groupby(df_data.index // 6).apply(assign_ranks).reset_index(drop=True)

# 元のデータフレームに「予測着順」カラムを追加
df['予測着順'] = None
df.iloc[1:, df.columns.get_loc('予測着順')] = df_data['予測着順'].values

# 1行目の「予測着順」を1として補完
df.at[0, '予測着順'] = 1

# CSVに結果を保存
df.to_csv('order.csv', index=False)
