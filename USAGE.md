# Kirito's Blog - 使用说明

## 📖 概述

这是一个简洁的静态博客系统，前端只使用 HTML + CSS + JavaScript，不依赖任何 Markdown 解析库。所有文章都是 HTML 格式，通过 Python 脚本自动生成索引文件。

## 🚀 快速开始

### 1. 添加新文章

在相应的文件夹下创建 HTML 文件：

- **算法文章**: `articles/algorithms/your-article.html`
- **工程文章**: `articles/engineering/your-article.html`  
- **C++ 文章**: `articles/programming/cpp/your-article.html`
- **Java 文章**: `articles/programming/java/your-article.html`
- **Python 文章**: `articles/programming/python/your-article.html`

### 2. HTML 文章模板

确保你的 HTML 文件包含以下元素：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>文章标题 - Kirito's Blog</title>
    <meta name="description" content="文章简介描述">
    <!-- 其他样式和脚本 -->
</head>
<body>
    <h1>文章标题</h1>
    <p>文章内容...</p>
</body>
</html>
```

**重要信息提取：**
- **标题**: 优先从 `<h1>` 标签提取，其次从 `<title>` 标签
- **描述**: 从 `<meta name="description">` 标签提取
- **日期**: 自动使用文件的最后修改时间

### 3. 生成文章索引

在项目根目录运行：

```bash
python scripts/generate_json.py
```

这将自动扫描所有文章文件夹，为每个文件夹生成 `articles.json` 索引文件。

## 📁 项目结构

```
Kiritobl.github.io/
├── index.html                 # 首页
├── articles.html              # 文章总览
├── about.html                 # 关于页面
├── scripts/
│   └── generate_json.py      # JSON 生成脚本
└── articles/
    ├── algorithms/            # 算法文章
    │   ├── articles.json     # 自动生成的索引
    │   └── *.html            # 文章文件
    ├── engineering/           # 工程文章
    │   ├── articles.json
    │   └── *.html
    └── programming/           # 编程文章
        ├── cpp/
        │   ├── articles.json
        │   └── *.html
        ├── java/
        │   ├── articles.json
        │   └── *.html
        └── python/
            ├── articles.json
            └── *.html
```

## 🔧 工作流程

1. **创建文章**: 编写 HTML 文件并保存到对应文件夹
2. **生成索引**: 运行 `python scripts/generate_json.py`
3. **提交代码**: `git add . && git commit -m "Add new article" && git push`
4. **自动部署**: GitHub Pages 自动部署更新

## ✨ 特性

- ✅ **纯 HTML**: 不需要 Markdown 解析，加载速度快
- ✅ **自动索引**: Python 脚本自动生成文章列表
- ✅ **响应式设计**: 适配各种设备屏幕
- ✅ **简单维护**: 添加文章只需两步（创建 HTML + 运行脚本）
- ✅ **统一导航**: 所有页面共享导航栏和底部栏样式

## 📝 注意事项

1. **文件名**: 建议使用英文和连字符，避免中文文件名
2. **描述信息**: 添加 `<meta name="description">` 可以在列表中显示文章简介
3. **标题提取**: 确保 HTML 中有 `<h1>` 或有意义的 `<title>` 标签
4. **索引更新**: 每次添加/修改文章后都要运行生成脚本

## 🛠️ 脚本说明

### generate_json.py

**功能**: 扫描指定文件夹下的所有 HTML 文件，提取文章信息并生成 JSON 索引

**扫描的文件夹**:
- `articles/algorithms/`
- `articles/engineering/`
- `articles/programming/cpp/`
- `articles/programming/java/`
- `articles/programming/python/`

**生成的 JSON 格式**:
```json
[
  {
    "title": "文章标题",
    "file": "article.html",
    "date": "2025-11-14",
    "description": "文章描述"
  }
]
```

## 📧 联系方式

- **GitHub**: [Kiritobl](https://github.com/Kiritobl)
- **Email**: your-email@example.com

## 📄 许可证

© 2025 Kirito's Blog. All rights reserved.
