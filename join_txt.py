import os
import chardet
"""
txtデータを順番通り結合してtxtで返す
"""

# 結合するフォルダのパスを指定
folder_path = "/Users/issahirasawa/Desktop/kyotei/race_data0201_09"  # フォルダのパスを指定

# 出力ファイルのパス
output_file_path = "combined_output.txt"

# 出力ファイルを開く
with open(output_file_path, "w", encoding="utf-8") as outfile:
    # フォルダ内の全てのファイルを取得し、ソートしてループ
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".TXT"):
            file_path = os.path.join(folder_path, filename)
            print(f"読み込み中のファイル: {filename}")

            # ファイルのエンコードを自動検出
            with open(file_path, "rb") as f:
                result = chardet.detect(f.read())
                encoding = result['encoding']
                print(f"検出したエンコード: {encoding}")

            # 検出したエンコードでファイルを開く
            with open(file_path, "r", encoding=encoding) as infile:
                file_content = infile.read()
                outfile.write(file_content)
                outfile.write("\n")

print("結合が完了しました。出力ファイル:", output_file_path)
