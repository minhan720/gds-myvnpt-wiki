import os
import subprocess
import shutil

def build_kb_nav():
    KB_DIR = "docs/knowledge base"
    if not os.path.exists(KB_DIR):
        print(f"Directory {KB_DIR} not found.")
        return []

    sections = {
        "background": "🗂 Background",
        "research": "📊 Research",
        "specs": "⚙️ Specs",
        "templates": "📄 Templates",
        "uiux-audit-output": "🔍 UIUX Audit Output",
        "ux-design-output": "✏️ UX Design Output"
    }

    def build_struct(current_path):
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
            sub_items = build_struct(os.path.join(current_path, folder))
            if sub_items:
                items.append({section_title: sub_items})
            
        for f in files:
            name = f[:-3].replace('_', ' ').replace('-', ' ').title()
            rel_path = os.path.relpath(os.path.join(current_path, f), "docs").replace("\\", "/")
            items.append({name: rel_path})
            
        return items

    kb_nav = [
        {"Trang chủ KB": "knowledge base/index.md"},
        {"Tổng Hợp": "knowledge base/tonghop.md"}
    ]
    
    kb_nav.extend(build_struct(KB_DIR))
    
    return kb_nav

def on_config(config, **kwargs):
    # This edits the config nav dynamically!
    
    kb_nav = build_kb_nav()
    is_kb_only = os.environ.get("BUILD_KB_ONLY") == "1"
    
    if is_kb_only:
        # If this is the standalone KB build, wipe out all other nav items, 
        # and set nav to ONLY Knowledge base
        config['nav'] = [
            {"🧠 Knowledge base": kb_nav}
        ]
        config['site_name'] = "GDS-MyVNPT Knowledge Base"
        print("Hook initialized: Standalone KB mode.")
    else:
        # Standard build - keep all other nav items, but ensure KB is a simple link
        for item in config.get('nav', []):
            if "🧠 Knowledge base" in item:
                # keep it as simple link
                item["🧠 Knowledge base"] = "knowledge base/index.md"
        print("Hook initialized: Standard mode.")
                
    return config

def on_post_build(config, **kwargs):
    is_kb_only = os.environ.get("BUILD_KB_ONLY") == "1"
    if not is_kb_only:
        print("Hook: Starting secondary build for standalone Knowledge Base...")
        
        # 1. build simple tonghop.md
        KB_DIR = "docs/knowledge base"
        OUT_FILE = f"{KB_DIR}/tonghop.md"
        if os.path.exists(KB_DIR):
            content = [
                "---",
                "hide:",
                "  - toc",
                "---",
                "# 📚 Tổng Hợp Knowledge Base",
                "",
                "Toàn bộ tài liệu báo cáo, nghiên cứu và cấu hình đã được tự động tổng hợp thành **cây thư mục Menubar (Cột bên trái)**. 👈",
                "",
                "> 💡 **Hãy bấm trực tiếp vào các danh mục cha bên trái để xổ ra các bài viết con tương ứng!**",
                ""
            ]
            with open(OUT_FILE, 'w', encoding='utf-8') as f:
                f.write('\n'.join(content))

        # 2. Run mkdocs build AGAIN, but with env var to trigger standalone config
        my_env = os.environ.copy()
        my_env["BUILD_KB_ONLY"] = "1"
        
        try:
            subprocess.run(["python3", "-m", "mkdocs", "build", "-d", "site-kb"], env=my_env, check=True)
            
            # 3. Copy knowledge base folder from site-kb to site
            src = "site-kb/knowledge base"
            dst = config['site_dir'] + "/knowledge base"
            print(f"Hook: Copying standalone KB from {src} to {dst}")
            if os.path.exists(src):
                shutil.copytree(src, dst, dirs_exist_ok=True)
                print("Hook: Isolated Knowledge Base successfully merged!")
            else:
                print(f"Hook Error: {src} not found after secondary build.")
                
            # Clean up
            shutil.rmtree("site-kb", ignore_errors=True)
        except Exception as e:
            print(f"Hook Error during dual build: {e}")
