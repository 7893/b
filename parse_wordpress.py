#!/usr/bin/env python3
"""
WordPress XML to Hugo Markdown Converter

This script parses a WordPress export XML file and converts posts and pages
to Hugo-compatible Markdown files with proper front matter.
"""

import xml.etree.ElementTree as ET
import os
import re
import html
from datetime import datetime
from pathlib import Path

def clean_content(content):
    """Clean WordPress-specific content to make it Hugo-compatible"""
    if content is None:
        return ""
    
    # Decode HTML entities
    content = html.unescape(content)
    
    # Replace WordPress-specific shortcodes with Hugo equivalents where possible
    content = re.sub(r'\[\/?caption.*?\]', '', content)  # Remove caption shortcodes
    content = re.sub(r'\[\/?wp.*?\]', '', content)  # Remove other WordPress shortcodes
    content = re.sub(r'\[\/?embed.*?\]', '', content)  # Remove embed shortcodes
    
    # Convert WordPress image tags to Markdown
    content = re.sub(
        r'<img[^>]*src=["\']([^"\']*)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*>',
        r'![\2](\1)',
        content
    )
    
    # Clean up multiple newlines
    content = re.sub(r'\n\s*\n', '\n\n', content)
    
    return content.strip()

def format_frontmatter_value(value):
    """Format frontmatter values appropriately"""
    if isinstance(value, list):
        # Escape any special characters in tags/categories
        return [v.replace('"', "'").replace('\n', '').strip() for v in value if v.strip()]
    elif isinstance(value, str):
        # Escape quotes and remove newlines
        return value.replace('"', "'").replace('\n', ' ').strip()
    return value

def convert_to_hugo_format(xml_file_path, output_dir="content"):
    """Convert WordPress XML to Hugo-compatible markdown files"""
    
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    # Define namespaces
    namespaces = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
        'wfw': 'http://wellformedweb.org/CommentAPI/',
        'dc': 'http://purl.org/dc/elements/1.1/',
        'wp': 'http://wordpress.org/export/1.2/'
    }
    
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    posts_count = 0
    
    # Process each item in the XML
    for item in root.findall('.//item'):
        # Determine if this is a post or page
        post_type = item.find('.//wp:post_type', namespaces)
        if post_type is not None:
            post_type = post_type.text
        else:
            post_type = 'post'  # default
            
        # Skip if it's not a post or page
        if post_type not in ['post', 'page']:
            continue
            
        # Extract post information
        title = item.find('title').text or ''
        title = html.unescape(title) if title else ''
        
        # Get encoded content
        content_elem = item.find('.//content:encoded', namespaces)
        content = content_elem.text if content_elem is not None else ''
        content = clean_content(content)
        
        # Extract other fields
        post_name = item.find('.//wp:post_name', namespaces)
        slug = post_name.text if post_name is not None and post_name.text else ''
        
        post_date = item.find('.//wp:post_date', namespaces)
        date = post_date.text if post_date is not None else ''
        
        post_status = item.find('.//wp:status', namespaces)
        status = post_status.text if post_status is not None else 'publish'
        
        # Only process published posts
        if status != 'publish':
            continue
            
        # Extract categories and tags
        categories = []
        post_tags = []
        
        for category in item.findall('category'):
            domain = category.get('domain')
            nicename = category.get('nicename')
            cat_name = category.text
            
            if domain == 'category':
                if cat_name and cat_name != 'Uncategorized':
                    categories.append(cat_name)
            elif domain == 'post_tag':
                if cat_name:
                    post_tags.append(cat_name)
        
        # Use categories as Hugo categories and tags as Hugo tags
        # If no categories but has tags, use tags as categories for Hugo simplicity
        if not categories and post_tags:
            categories = post_tags[:1]  # Use first tag as category if no categories
            post_tags = post_tags[1:] if len(post_tags) > 1 else []
        
        # Format date for Hugo (expected format: 2006-01-02T15:04:05Z07:00)
        try:
            dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            formatted_date = dt.strftime('%Y-%m-%dT%H:%M:%S+00:00')
        except ValueError:
            formatted_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00')
        
        # Create filename
        if slug:
            filename = f"{slug}.md"
        else:
            # Create a slug from title if no post_name exists
            slug = re.sub(r'[^\w\s-]', '', title.lower()).strip()
            slug = re.sub(r'[-\s]+', '-', slug)
            filename = f"{slug}.md"
        
        # Determine output subdirectory based on post type
        if post_type == 'page':
            sub_dir = output_path / 'posts'  # Put pages in posts directory
        else:
            sub_dir = output_path / 'posts'
        
        sub_dir.mkdir(exist_ok=True)
        file_path = sub_dir / filename
        
        # Prepare front matter
        frontmatter = {
            'title': f'"{format_frontmatter_value(title)}"',
            'date': f'"{formatted_date}"',
            'draft': 'false',
        }
        
        if categories:
            frontmatter['categories'] = categories
        if post_tags:
            frontmatter['tags'] = post_tags
            
        # Create the markdown content with front matter
        frontmatter_str = "---\n"
        for key, value in frontmatter.items():
            if isinstance(value, list):
                frontmatter_str += f"{key}:\n"
                for v in value:
                    frontmatter_str += f"  - \"{v}\"\n"
            else:
                frontmatter_str += f"{key}: {value}\n"
        frontmatter_str += "---\n\n"
        
        # Write to file
        full_content = frontmatter_str + content
        
        # Clean up any duplicate frontmatter markers
        full_content = re.sub(r'---\n\s*---', '---', full_content, count=1)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"Converted: {title} -> {file_path}")
        posts_count += 1
    
    print(f"\nConversion complete! {posts_count} posts/pages converted.")
    print(f"Output directory: {output_path.absolute()}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 parse_wordpress.py <wordpress_xml_file>")
        sys.exit(1)
        
    xml_file = sys.argv[1]
    
    if not os.path.exists(xml_file):
        print(f"Error: File {xml_file} does not exist")
        sys.exit(1)
        
    convert_to_hugo_format(xml_file)