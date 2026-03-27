#!/bin/bash

# CodeMaker 新人教学流程图 - GitHub 部署脚本

echo "🚀 开始部署到 GitHub..."

# 1. 检查是否已配置 git
if ! git config user.name &> /dev/null; then
    echo "⚠️  请先配置 git 用户信息"
    read -p "请输入 git 用户名：" git_user
    read -p "请输入 git 邮箱：" git_email
    git config user.name "$git_user"
    git config user.email "$git_email"
fi

# 2. 添加所有文件
echo "📦 添加文件..."
git add .

# 3. 提交
echo "💾 提交更改..."
git commit -m "Update: CodeMaker 新人教学流程图"

# 4. 检查是否有 remote
if ! git remote get-url origin &> /dev/null; then
    echo ""
    echo "⚠️  请先在 GitHub 创建仓库，然后输入仓库地址"
    echo "   创建地址：https://github.com/new"
    echo ""
    read -p "请输入仓库地址 (例如：https://github.com/你的用户名/wuzucatProject.git): " repo_url
    git remote add origin "$repo_url"
fi

# 5. 推送
echo ""
echo "📤 推送到 GitHub..."
git branch -M main
git push -u origin main

echo ""
echo "✅ 部署完成！"
echo ""
echo "📌 下一步：启用 GitHub Pages"
echo "   1. 访问：https://github.com/你的用户名/wuzucatProject/settings/pages"
echo "   2. Source 选择 'main branch'"
echo "   3. 点击 Save"
echo ""
echo "   启用后访问：https://你的用户名.github.io/wuzucatProject/index.html"
echo ""
