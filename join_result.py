import pandas as pd
import os
"""
csvレースデータとcsv選手データを結合して返す
"""
# CSVファイルのパスを指定
result_path = '/Users/issahirasawa/Desktop/kyotei/result.csv'
player_path = '/Users/issahirasawa/Desktop/kyotei/player_2020f/player_basic.csv'
course_paths = {
    i: f'/Users/issahirasawa/Desktop/kyotei/player_2020f/course{i}_output.csv' for i in range(1, 7)}

# result.csvとplayer.csvを読み込む
result_df = pd.read_csv(result_path)
player_df = pd.read_csv(player_path)

# 登録番号でresult.csvとplayer.csvをマージ
merged_df = pd.merge(result_df, player_df, on='登録', how='left')

# 各行の艇番に基づいて、適切なcourseX_output.csvをマージする
for index, row in merged_df.iterrows():
    teiban = row['艇番']

    # 対応するcourseX_output.csvを読み込む（艇番に基づく）
    course_path = course_paths.get(teiban)
    if course_path:
        course_df = pd.read_csv(course_path)

        # 該当の行とcourseX_output.csvを登録番号でマージ
        merged_temp_df = pd.merge(pd.DataFrame(
            [row]), course_df, on='登録', how='left')

        # 重複した列を処理しつつ、merged_dfの該当行に上書き
        for col in merged_temp_df.columns:
            if col in merged_df.columns:
                # 既存の列を更新
                merged_df.at[index, col] = merged_temp_df.at[0, col]
            else:
                # 新しい列があれば追加
                merged_df[col] = None
                merged_df.at[index, col] = merged_temp_df.at[0, col]

# 結果をCSVに保存する
output_path = '/Users/issahirasawa/Desktop/kyotei/merged_result.csv'
merged_df.to_csv(output_path, index=False)

print("マージ完了。結果は", output_path, "に保存されました。")
