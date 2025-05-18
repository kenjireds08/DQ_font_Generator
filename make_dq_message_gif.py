import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio
import requests

# ドラクエ風フォント（PixelMplus）自動ダウンロード
FONT_PATH = "PixelMplus10-Regular.ttf"
if not os.path.exists(FONT_PATH):
    url = "https://github.com/itouhiro/PixelMplus/raw/master/PixelMplus10-Regular.ttf"
    r = requests.get(url)
    with open(FONT_PATH, "wb") as f:
        f.write(r.content)

# メッセージ内容
messages = [
    "ちーけんは　レベル43に　あがった！",
    "",
    "ちからが　1ポイント　さがった！",
    "すばやさが　2ポイント　さがった！",
    "たいりょくが　3ポイント　さがった！",
    "かしこさが　2ポイント　あがった！",
    "さいだいHPが　5ポイント　さがった！",
    "さいだいMPが　3ポイント　さがった！",
    "ろうがんが　3ポイント　すすんだ！",
    "",
    "じゅもん　モノワスレ　をおぼえた！"
]

# 設定
base_img = Image.open("hero.png").convert("RGBA")
w, h = base_img.size
window_height = int(h * 0.28)
window_y = h - window_height
margin = 24
font_size = 40
font = ImageFont.truetype(FONT_PATH, font_size)
line_height = font.getbbox("あ")[3] + 10

# メッセージウィンドウ描画関数
def draw_window(img, lines):
    img = img.copy()
    draw = ImageDraw.Draw(img)
    # ウィンドウ
    draw.rectangle([margin, window_y, w - margin, h - margin], fill="black", outline="white", width=4)
    # 内側枠
    draw.rectangle([margin+10, window_y+10, w-margin-10, h-margin-10], outline="white", width=2)
    # テキスト
    padding_x = 37  # 元々25+12
    padding_y = 32  # 元々20+12
    for i, line in enumerate(lines):
        draw.text((margin+padding_x, window_y+padding_y + i*line_height), line, font=font, fill="white")
    return img

# アニメーションフレーム生成
frames = []
current_lines = []
# ウィンドウ内に表示できる最大行数を計算
max_lines = (window_height - 40) // line_height

for msg in messages:
    current_lines.append("")  # 新しい行を追加
    for i in range(1, len(msg) + 1):
        current_lines[-1] = msg[:i]  # 1文字ずつ増やす
        # スクロール処理
        display_lines = current_lines[-max_lines:]
        frame = draw_window(base_img, display_lines)
        frames.append(np.array(frame))
    # 行が完成したら少し静止
    for _ in range(5):
        display_lines = current_lines[-max_lines:]
        frame = draw_window(base_img, display_lines)
        frames.append(np.array(frame))

# 最後に2秒間静止フレーム（GIFのduration=0.12なので約16フレーム）
for _ in range(16):
    display_lines = current_lines[-max_lines:]
    frames.append(np.array(draw_window(base_img, display_lines)))

# GIF保存
imageio.mimsave("dq_message.gif", frames, duration=0.12)

print("GIFを dq_message.gif として出力しました！")