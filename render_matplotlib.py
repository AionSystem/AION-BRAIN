import re
import os
import sys
import matplotlib.pyplot as plt
import numpy as np  # Common import; add others if needed
import importlib  # For dynamic imports if code requires

def process_md(file_path, diagrams_dir='diagrams'):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex for python code blocks
    pattern = r'```python\n(.*?)\n```'
    matches = re.findall(pattern, content, re.DOTALL)

    new_content = content
    offset = 0  # Track position shifts from replacements

    for i, code in enumerate(matches):
        if 'matplotlib' in code or 'plt' in code:
            try:
                # Prepare safe globals/locals with common libs
                globals_dict = {
                    'plt': plt,
                    'np': np,
                    # Add more: 'pd': importlib.import_module('pandas') if needed
                }
                locals_dict = {}

                # Redirect stdout to capture prints if any
                old_stdout = sys.stdout
                sys.stdout = StringIO()

                # Exec code
                exec(code, globals_dict, locals_dict)

                sys.stdout = old_stdout

                # Get current figure if exists
                fig = plt.gcf()
                if fig.get_axes():  # If a plot was created
                    # Generate unique filename
                    base_name = os.path.basename(file_path)[:-3]  # e.g., README
                    filename = f'plot_{base_name}_{i}.png'
                    filepath = os.path.join(diagrams_dir, filename)
                    os.makedirs(diagrams_dir, exist_ok=True)

                    # Save figure
                    fig.savefig(filepath, format='png', bbox_inches='tight')
                    plt.clf()  # Clear for next

                    # Append image link after code block
                    image_md = f'\n![Plot {i}]({filepath})\n'
                    block = f'```python\n{code}\n```'
                    new_block = block + image_md

                    # Find position and replace
                    block_start = new_content.find(block, offset)
                    if block_start != -1:
                        block_end = block_start + len(block)
                        new_content = new_content[:block_end] + image_md + new_content[block_end:]
                        offset = block_end + len(image_md)

            except Exception as e:
                print(f"Error rendering plot {i} in {file_path}: {e}", file=sys.stderr)

    # Write back updated content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python render_matplotlib.py path/to/file.md")
        sys.exit(1)
    process_md(sys.argv[1])