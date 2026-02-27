import os

KB_DIR = "docs/knowledge base"
YAML_FILE = "mkdocs.yml"
OUT_FILE = f"{KB_DIR}/tonghop.md"

def update_nav_and_tonghop():
    # 1. Update mkdocs.yml
    if os.path.exists(YAML_FILE):
        with open(YAML_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        kb_index = -1
        for i, line in enumerate(lines):
            if line.startswith("  - 🧠 Knowledge base:"):
                kb_index = i
                break

        if kb_index != -1:
            new_lines = lines[:kb_index]
            new_lines.append("  - 🧠 Knowledge base:\n")
            new_lines.append("    - Trang chủ KB: 'knowledge base/index.md'\n")
            new_lines.append("    - Tổng Hợp: 'knowledge base/tonghop.md'\n")

            sections = {
                "background": "🗂 Background",
                "research": "📊 Research",
                "specs": "⚙️ Specs",
                "templates": "📄 Templates",
                "uiux-audit-output": "🔍 UIUX Audit Output",
                "ux-design-output": "✏️ UX Design Output"
            }

            def build_yaml(current_path, indent_level):
                items = []
                try:
                    entries = sorted(os.listdir(current_path))
                except FileNotFoundError:
                    return items
                
                folders = []
                files = []
                for e in entries:
                    if e.startswith('.'):
                        continue
                    full_path = os.path.join(current_path, e)
                    if os.path.isdir(full_path):
                        folders.append(e)
                    elif full_path.endswith(".md") and e not in ["index.md", "tonghop.md"]:
                        files.append(e)
                        
                for folder in folders:
                    section_title = sections.get(folder, f"📁 {folder.replace('-', ' ').title()}")
                    items.append(" " * indent_level + f"- {section_title}:\n")
                    items.extend(build_yaml(os.path.join(current_path, folder), indent_level + 2))
                    
                for f in files:
                    name = f[:-3].replace('_', ' ').replace('-', ' ').title()
                    rel_path = os.path.relpath(os.path.join(current_path, f), "docs").replace("\\", "/")
                    items.append(" " * indent_level + f"- '{name}': '{rel_path}'\n")
                    
                return items

            new_lines.extend(build_yaml(KB_DIR, 4))

            with open(YAML_FILE, "w", encoding="utf-8") as f:
                f.writelines(new_lines)

    # 2. Re-create simple tonghop.md
    if os.path.exists(KB_DIR):
        content = [
            "# 📚 Tổng Hợp Knowledge Base",
            "",
            "Toàn bộ tài liệu báo cáo, nghiên cứu và cấu hình đã được tự động tổng hợp thành **cây thư mục Menubar (Cột bên trái)**. 👈",
            "",
            "> 💡 **Hãy bấm trực tiếp vào các danh mục cha bên trái để xổ ra các bài viết con tương ứng!**",
            ""
        ]
        with open(OUT_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))

if __name__ == '__main__':
    update_nav_and_tonghop()
