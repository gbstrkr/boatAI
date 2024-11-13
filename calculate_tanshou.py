import pandas as pd

# ファイルを読み込む
odds_data = pd.read_csv('odds_data.csv')
order_data = pd.read_csv('order.csv')

# 最終的な値を計算する変数を用意
final_value = 0
cnt_true = 0
cnt_false = 0

# odds_dataを1行ずつ処理
for i, odds_row in odds_data.iterrows():
    # order_dataの対応する6行を取得
    order_rows = order_data.iloc[i*6+1:(i+1)*6+1]
    
    # order_dataで予測結果が1の行を抽出
    first_place_row = order_rows[order_rows['予測着順'] == 1]

    # 確認のために1行目が存在するかチェック
    if not first_place_row.empty:
        # 予測結果が1の艇番を取得
        predicted_boat_number = first_place_row.iloc[0]['艇番']
        if first_place_row.iloc[0]['予測']>0.65:
            # 単勝番号と予測結果1の艇番が一致するか確認
            if odds_row['単勝番号'] == predicted_boat_number:
                # 一致すれば単勝オッズを加算
                final_value += odds_row['単勝オッズ']
                final_value -= 100
                cnt_true+=1
            else:
                # 一致しなければ-100を減算
                final_value -= 100
                cnt_false+=1
    else:
        # 対応する予測結果がない場合はスキップ
        print(f"Warning: No first place prediction found for odds row {i}")

# 最終的な値を出力
print(f"最終的な値: {final_value}")
print(f"勝ち数：{cnt_true}")
print(f"負け数：{cnt_false}")
