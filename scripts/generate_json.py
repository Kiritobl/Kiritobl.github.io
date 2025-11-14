#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动生成 articles.json 文件
扫描指定文件夹下的所有 HTML 文件，提取标题、日期和描述信息，生成 JSON 文件
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path
from html.parser import HTMLParser


class HTMLTitleExtractor(HTMLParser):
    """提取 HTML 文件中的标题和描述"""
    def __init__(self):
        super().__init__()
        self.title = None
        self.description = None
        self.in_title = False
        self.in_meta = False
        self.current_h1 = None
        
    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.in_title = True
        elif tag == 'meta':
            attrs_dict = dict(attrs)
            if attrs_dict.get('name') == 'description':
                self.description = attrs_dict.get('content', '')
        elif tag == 'h1' and not self.current_h1:
            self.in_h1 = True
            
    def handle_data(self, data):
        if self.in_title and not self.title:
            self.title = data.strip()
        elif hasattr(self, 'in_h1') and self.in_h1 and not self.current_h1:
            self.current_h1 = data.strip()
            
    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        elif tag == 'h1':
            if hasattr(self, 'in_h1'):
                self.in_h1 = False


def extract_info_from_html(file_path):
    """从 HTML 文件中提取信息"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        parser = HTMLTitleExtractor()
        parser.feed(content)
        
        # 优先使用 h1 标题，其次使用 title 标签
        title = parser.current_h1 or parser.title
        if title:
            # 清理标题（移除网站名称后缀）
            title = re.sub(r'\s*[-|]\s*Kirito\'?s?\s*[Bb]log\s*$', '', title)
            title = title.strip()
        
        if not title:
            # 如果没有找到标题，使用文件名
            title = Path(file_path).stem.replace('-', ' ').replace('_', ' ').title()
        
        description = parser.description or "点击查看文章详情"
        
        return title, description
        
    except Exception as e:
        print(f"警告: 读取文件 {file_path} 时出错: {e}")
        filename = Path(file_path).stem
        return filename.replace('-', ' ').replace('_', ' ').title(), "点击查看文章详情"


def get_file_date(file_path):
    """获取文件的最后修改时间"""
    timestamp = os.path.getmtime(file_path)
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')


def generate_articles_json(folder_path, output_file='articles.json'):
    """生成指定文件夹的 articles.json"""
    articles = []
    
    # 遍历文件夹中的所有 HTML 文件
    for file in Path(folder_path).glob('*.html'):
        if file.name == 'articles.json':
            continue
            
        title, description = extract_info_from_html(file)
        date = get_file_date(file)
        
        article = {
            "title": title,
            "file": file.name,
            "date": date,
            "description": description
        }
        articles.append(article)
    
    # 按日期排序（最新的在前）
    articles.sort(key=lambda x: x['date'], reverse=True)
    
    # 写入 JSON 文件
    output_path = Path(folder_path) / output_file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已生成: {output_path} (共 {len(articles)} 篇文章)")
    return len(articles)


def main():
    """主函数：扫描所有需要的文件夹"""
    base_path = Path(__file__).parent.parent / 'articles'
    
    folders_to_scan = [
        base_path / 'algorithms',
        base_path / 'engineering',
        base_path / 'programming' / 'cpp',
        base_path / 'programming' / 'java',
        base_path / 'programming' / 'python',
    ]
    
    total_articles = 0
    
    print("=" * 60)
    print("开始生成 articles.json 文件...")
    print("=" * 60)
    
    for folder in folders_to_scan:
        if folder.exists():
            print(f"\n📁 扫描文件夹: {folder.relative_to(base_path.parent)}")
            count = generate_articles_json(folder)
            total_articles += count
        else:
            print(f"\n⚠️  文件夹不存在: {folder}")
    
    print("\n" + "=" * 60)
    print(f"✨ 完成！共处理 {total_articles} 篇文章")
    print("=" * 60)


if __name__ == '__main__':
    main()
