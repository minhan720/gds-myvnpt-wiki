import os
import glob

KB_DIR = "docs/knowledge base"
OUT_FILE = f"{KB_DIR}/tonghop.md"

def generate_tonghop():
    if not os.path.exists(KB_DIR):
        print(f"Directory {KB_DIR} not found.")
        return

    content = [
        "---",
        "hide:",
        "  - toc",
        "---",
        "# 📚 Tổng Hợp Knowledge Base",
        "",
        "Dưới đây là danh mục tự động tổng hợp toàn bộ tài liệu nghiên cứu và thiết lập của dự án. Hệ thống sẽ tự động cập nhật danh sách này bất cứ khi nào có bản báo cáo mới được khai báo vào thư viện `knowledge base`.",
        "",
    ]

    # Sections mapping
    sections = {
        "background": "🗂 Background",
        "research": "📊 Research",
        "specs": "⚙️ Specs",
        "templates": "📄 Templates",
        "uiux-audit-output": "🔍 UIUX Audit Output",
        "ux-design-output": "✏️ UX Design Output"
    }

    # Iterate through all subdirectories
    printed_sections = set()
    
    # Sort for deterministic output
    directories = []
    for root, dirs, files in os.walk(KB_DIR):
        directories.append((root, dirs, files))
    directories.sort(key=lambda x: x[0])
    
    for root, dirs, files in directories:
        # Ignore root folder itself
        if root == KB_DIR:
            continue
            
        md_files = [f for f in files if f.endswith('.md')]
        if not md_files:
            continue

        # Determine section name
        rel_path = os.path.relpath(root, KB_DIR)
        parts = rel_path.split(os.sep)
        top_folder = parts[0]
        
        section_title = sections.get(top_folder, f"📁 {top_folder.replace('-', ' ').title()}")
        
        if top_folder not in printed_sections:
            content.append(f"## {section_title}")
            printed_sections.add(top_folder)
            
        if len(parts) > 1:
            sub_title = f"### {' '.join(parts[1:]).replace('-', ' ').title()}"
            content.append(sub_title)
            
        # Add files
        md_files.sort()
        for md_file in md_files:
            name = md_file[:-3].replace('_', ' ').replace('-', ' ').title()
            # Handle special cases manually or keep title case
            rel_file_path = os.path.relpath(os.path.join(root, md_file), KB_DIR)
            content.append(f"- [{name}]({rel_file_path})")
            
        content.append("")

    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))

if __name__ == '__main__':
    generate_tonghop()
