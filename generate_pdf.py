#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将新人教学流程图转换为 PDF 文档
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Frame, PageTemplate, Image, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
import os

# 注册中文字体（使用 macOS 系统字体）
font_paths = [
    '/System/Library/Fonts/PingFang.ttc',
    '/System/Library/Fonts/Supplemental/PingFang.ttc',
    '/Library/Fonts/AppleLiSung.ttf',
    '/System/Library/Fonts/STHeiti Light.ttc',
]

# 尝试注册中文字体
registered = False
for font_path in font_paths:
    if os.path.exists(font_path):
        try:
            pdfmetrics.registerFont(TTFont('Chinese', font_path))
            registered = True
            print(f"成功注册字体：{font_path}")
            break
        except Exception as e:
            continue

if not registered:
    print("警告：未找到中文字体，PDF 可能无法正确显示中文")
    # 使用默认字体
    pdfmetrics.registerFont(TTFont('Chinese', 'Helvetica'))

# 流程图数据
flowchart_data = {
    'title': 'CodeMaker 新人教学流程',
    'subtitle': '一步步带你配置公司破译版小龙虾 AI 助手',
    'phases': [
        {
            'name': '第一阶段：环境准备',
            'steps': [
                {'number': '步骤 1', 'title': '📥 下载 VSCode', 'desc': '安装 Visual Studio Code 编辑器'},
                {'number': '步骤 2', 'title': '📄 打开 MD 文档', 'desc': '打开提供的说明文档',
                 'image': '/Users/hehuiqian/Desktop/wuzucatProject/.cowork-temp/attachments/manual/image_2026-03-27_072924-1774596564148-o1f4m3.png',
                 'caption': '图 1：打开 MD 文档'},
                {'number': '步骤 3', 'title': '✅ 完成第一步和第二步', 'desc': '根据 MD 文档说明完成前两步配置',
                 'image': '/Users/hehuiqian/Desktop/wuzucatProject/.cowork-temp/attachments/manual/image_2026-03-27_072945-1774596585661-w7rpca.png',
                 'caption': '图 3：CodeMaker 小龙虾界面'},
            ]
        },
        {
            'name': '第二阶段：启动 CodeMaker',
            'steps': [
                {'number': '步骤 4', 'title': '💻 CMD 打开终端', 'desc': '完成配置后，使用 CMD 打开命令行终端',
                 'image': '/Users/hehuiqian/Desktop/wuzucatProject/.cowork-temp/attachments/manual/image_2026-03-27_081813-1774599493916-nt18cy.png',
                 'caption': '图：使用 CMD 打开终端'},
                {'number': '步骤 5', 'title': '🚀 输入 codemaker', 'desc': '在终端输入 codemaker（注意没有空格）',
                 'image': '/Users/hehuiqian/Desktop/wuzucatProject/.cowork-temp/attachments/manual/image_2026-03-27_082101-1774599661057-a5zy02.png',
                 'caption': '图：在终端输入 codemaker'},
                {'number': '步骤 6', 'title': '🦞 出现小龙虾界面', 'desc': '公司破译版本的小龙虾 AI 界面',
                 'image': '/Users/hehuiqian/Desktop/wuzucatProject/.cowork-temp/attachments/manual/image_2026-03-27_073002-1774596602762-4lyvyu.png',
                 'caption': '图 4：复制路径让 CodeMaker 学习'},
            ]
        },
        {
            'name': '第三阶段：学习配置',
            'steps': [
                {'number': '步骤 7', 'title': '📚 让 CodeMaker 学习', 'desc': '复制 MD 文档路径，让它自主学习',
                 'image': '/Users/hehuiqian/Desktop/wuzucatProject/.cowork-temp/attachments/manual/image_2026-03-27_081822-1774599502972-9mx4pg.png',
                 'caption': '图：让 CodeMaker 学习',
                 'extra': '现在你就可以开始养龙虾了'},
            ]
        },
        {
            'name': '第四阶段：POPO 机器人配置（可选）',
            'steps': [
                {'number': '步骤 8', 'title': '🤖 需要配置 POPO 机器人？', 'desc': '如需配置 POPO 机器人，继续以下步骤', 'decision': True},
                {'number': '步骤 9', 'title': '🌐 打开 POPO 开发平台', 'desc': '访问 https://open-dev.popo.netease.com/robot'},
                {'number': '步骤 10', 'title': '📝 创建机器人并填写信息', 'desc': '与 CodeMaker 沟通，填写相关配置信息',
                 'image': '/Users/hehuiqian/Desktop/wuzucatProject/.cowork-temp/attachments/manual/image_2026-03-27_073012-1774596612968-564r90.png',
                 'caption': '图 5：POPO 开发平台创建机器人'},
                {'number': '步骤 11', 'title': '✅ 测试 POPO 机器人对话', 'desc': '验证 POPO 龙虾机器人是否可以正常对话'},
            ]
        },
        {
            'name': '第五阶段：Skill 扩展（可选）',
            'steps': [
                {'number': '步骤 12', 'title': '🔧 需要安装 Skill？', 'desc': '如需扩展功能，可以安装各种 Skill', 'decision': True},
                {'number': '步骤 13', 'title': '📦 访问技能平台', 'desc': '打开 https://skills.netease.com/'},
                {'number': '步骤 14', 'title': '⬇️ 下载推荐技能', 'desc': '点击下载技能，复制文件信息',
                 'image': '/Users/hehuiqian/Desktop/wuzucatProject/.cowork-temp/attachments/manual/image_2026-03-27_073031-1774596631048-lvjhhv.png',
                 'caption': '图 6：技能平台页面'},
                {'number': '步骤 15', 'title': '📖 让 CodeMaker 学习技能', 'desc': '复制文件信息给 CodeMaker，让它学习新技能',
                 'image': '/Users/hehuiqian/Desktop/wuzucatProject/.cowork-temp/attachments/manual/image_2026-03-27_073058-1774596658471-h2m3cp.png',
                 'caption': '图 7：下载技能文件'},
            ]
        },
    ],
    'completion': {
        'title': '🎉 完成配置！',
        'desc': '现在可以正常使用 CodeMaker 小龙虾 AI 助手了'
    },
    'notes': [
        'POPO 机器人配置和 Skill 安装为可选步骤，根据实际需求选择',
        '带菱形的步骤为判断节点，根据实际需求选择分支',
        '如有问题可随时与 CodeMaker 沟通',
        '推荐下载的技能可以让 CodeMaker 更强大'
    ]
}

def create_pdf():
    # 创建 PDF 文档
    doc = SimpleDocTemplate(
        "新人教学流程图.pdf",
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    story = []
    styles = getSampleStyleSheet()

    # 定义自定义样式
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontName='Chinese',
        fontSize=24,
        textColor=HexColor('#333333'),
        spaceAfter=12,
        alignment=TA_CENTER
    )

    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontName='Chinese',
        fontSize=12,
        textColor=HexColor('#666666'),
        spaceAfter=30,
        alignment=TA_CENTER
    )

    phase_style = ParagraphStyle(
        'PhaseTitle',
        parent=styles['Heading2'],
        fontName='Chinese',
        fontSize=16,
        textColor=colors.white,
        backColor=HexColor('#f5576c'),
        spaceBefore=20,
        spaceAfter=15,
        alignment=TA_CENTER,
        borderRadius=10
    )

    step_number_style = ParagraphStyle(
        'StepNumber',
        parent=styles['Normal'],
        fontName='Chinese',
        fontSize=10,
        textColor=colors.white,
        backColor=HexColor('#667eea'),
        spaceAfter=5,
        alignment=TA_CENTER
    )

    step_title_style = ParagraphStyle(
        'StepTitle',
        parent=styles['Normal'],
        fontName='Chinese',
        fontSize=14,
        textColor=HexColor('#333333'),
        spaceAfter=5,
        alignment=TA_CENTER
    )

    step_desc_style = ParagraphStyle(
        'StepDesc',
        parent=styles['Normal'],
        fontName='Chinese',
        fontSize=11,
        textColor=HexColor('#666666'),
        spaceAfter=10,
        alignment=TA_CENTER
    )

    extra_style = ParagraphStyle(
        'ExtraText',
        parent=styles['Normal'],
        fontName='Chinese',
        fontSize=12,
        textColor=HexColor('#f5576c'),
        spaceAfter=15,
        alignment=TA_CENTER
    )

    caption_style = ParagraphStyle(
        'Caption',
        parent=styles['Normal'],
        fontName='Chinese',
        fontSize=9,
        textColor=HexColor('#666666'),
        spaceAfter=15,
        alignment=TA_CENTER
    )

    arrow_style = ParagraphStyle(
        'Arrow',
        parent=styles['Normal'],
        fontName='Chinese',
        fontSize=18,
        textColor=HexColor('#667eea'),
        spaceBefore=5,
        spaceAfter=5,
        alignment=TA_CENTER
    )

    note_style = ParagraphStyle(
        'Note',
        parent=styles['Normal'],
        fontName='Chinese',
        fontSize=11,
        textColor=HexColor('#856404'),
        backColor=HexColor('#fff3cd'),
        leftIndent=10,
        rightIndent=10,
        spaceBefore=20,
        spaceAfter=10
    )

    # 标题
    story.append(Paragraph(flowchart_data['title'], title_style))
    story.append(Paragraph(flowchart_data['subtitle'], subtitle_style))

    # 各个阶段
    for phase in flowchart_data['phases']:
        story.append(Paragraph(phase['name'], phase_style))

        for i, step in enumerate(phase['steps']):
            # 步骤编号
            story.append(Paragraph(step['number'], step_number_style))

            # 步骤标题
            story.append(Paragraph(step['title'], step_title_style))

            # 步骤描述
            story.append(Paragraph(step['desc'], step_desc_style))

            # 额外文字（如"现在你就可以开始养龙虾了"）
            if 'extra' in step:
                story.append(Paragraph(step['extra'], extra_style))

            # 图片
            if 'image' in step:
                img_path = step['image']
                if os.path.exists(img_path):
                    try:
                        # 创建图片，限制宽度
                        img = Image(img_path, width=12*cm, height=8*cm)
                        story.append(img)
                        # 图片说明
                        if 'caption' in step:
                            story.append(Paragraph(step['caption'], caption_style))
                    except Exception as e:
                        print(f"图片加载失败 {img_path}: {e}")

            # 箭头（除了最后一个步骤）
            if i < len(phase['steps']) - 1:
                story.append(Paragraph('⬇️', arrow_style))

        story.append(Spacer(1, 15))

    # 完成步骤
    story.append(Paragraph('完成', step_number_style))
    story.append(Paragraph(flowchart_data['completion']['title'], step_title_style))
    story.append(Paragraph(flowchart_data['completion']['desc'], step_desc_style))

    # 注意事项
    story.append(Spacer(1, 20))
    story.append(Paragraph('📌 注意事项', phase_style))
    for note in flowchart_data['notes']:
        story.append(Paragraph(f'• {note}', note_style))

    # 生成 PDF
    doc.build(story)
    print("✅ PDF 生成成功：新人教学流程图.pdf")

if __name__ == '__main__':
    create_pdf()
