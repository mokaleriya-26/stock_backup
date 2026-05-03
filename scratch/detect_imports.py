import os
import re

def get_imports():
    imports = set()
    for root, dirs, files in os.walk('.'):
        if 'venv' in dirs:
            dirs.remove('venv')
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                    # Match "import package"
                    matches = re.findall(r'^import ([a-zA-Z0-9_]+)', content, re.MULTILINE)
                    for m in matches:
                        imports.add(m)
                    # Match "from package import ..."
                    matches = re.findall(r'^from ([a-zA-Z0-9_]+)', content, re.MULTILINE)
                    for m in matches:
                        imports.add(m)
    return imports

print("Detected imports:")
print(sorted(list(get_imports())))
