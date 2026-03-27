#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将 HTML 文件中的本地图片路径转换为 Base64 编码，生成单文件 HTML
"""

import base64
import re
import os

# 读取原始 HTML 文件
html_path = '/Users/hehuiqian/Desktop/wuzucatProject/新人教学流程图 - 带图示.html'
output_path = '/Users/hehuiqian/Desktop/wuzucatProject/新人教学流程图 - 单文件.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 找出所有图片路径
img_pattern = r'<img src="([^"]+)"'
img_matches = re.findall(img_pattern, html_content)

print(f"找到 {len(img_matches)} 张图片")

# 替换每张图片为 Base64 编码
for img_path in img_matches:
    print(f"处理图片：{img_path}")

    # 检查文件是否存在
    if not os.path.exists(img_path):
        print(f"  ⚠️ 文件不存在，跳过")
        continue

    # 读取图片并编码为 Base64
    with open(img_path, 'rb') as img_file:
        img_data = img_file.read()
        base64_data = base64.b64encode(img_data).decode('utf-8')

    # 确定图片类型
    if img_path.endswith('.png'):
        img_type = 'image/png'
    elif img_path.endswith('.jpg') or img_path.endswith('.jpeg'):
        img_type = 'image/jpeg'
    elif img_path.endswith('.gif'):
        img_type = 'image/gif'
    else:
        img_type = 'image/png'  # 默认

    # 生成 Base64 数据 URL
    base64_url = f'data:{img_type};base64,{base64_data}'

    # 替换 HTML 中的路径
    html_content = html_content.replace(f'src="{img_path}"', f'src="{base64_url}"')
    print(f"  ✅ 转换完成")

# 写入新的 HTML 文件
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"\n✅ 单文件 HTML 生成成功：{output_path}")
print(f"📦 现在你只需要分享这一个文件即可！")
