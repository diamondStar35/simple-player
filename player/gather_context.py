import os

def gather_context(root_dir, extensions=('.py',)):
    """Gathers file paths and contents for Gemini context."""
    for root, dirs, files in os.walk(root_dir):
        # Skip common non-source directories
        if any(d in root for d in ['.git', '__pycache__', 'venv', '.idea', '.vscode']):
            continue
            
        for file in files:
            if file.endswith(extensions):
                full_path = os.path.abspath(os.path.join(root, file))
                print(f"{full_path}")
                print("```" + (file.split('.')[-1] if '.' in file else ""))
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        print(f.read())
                except Exception as e:
                    print(f"Error reading file: {e}")
                print("```\n")

if __name__ == "__main__":
    # Run this from your project root
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    gather_context(project_root)