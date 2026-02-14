import re
import os
import sys
import matplotlib.pyplot as plt
import numpy as np  # Common import; add others if needed
import importlib    # For dynamic imports if code requires
from io import StringIO  # ← The dragon scale we kept forgetting!

def process_md(file_path, diagrams_dir='diagrams'):
    """
    Process a markdown file: find python code blocks with matplotlib,
    execute them, save generated plots as PNG, and embed image links.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to capture everything between ```python and the next ```
    pattern = r'```python\n(.*?)\n```'
    matches = re.findall(pattern, content, re.DOTALL)

    new_content = content
    offset = 0  # Track insertion point shifts

    for i, code in enumerate(matches):
        # Only attempt render if it looks like a plotting script
        if 'matplotlib' in code.lower() or 'plt' in code:
            try:
                # Safe globals with pre-imported libs
                globals_dict = {
                    'plt': plt,
                    'np': np,
                    # Extend here if your plots need pandas, etc.:
                    # 'pd': importlib.import_module('pandas'),
                }
                locals_dict = {}

                # Capture any print() output (for debugging)
                old_stdout = sys.stdout
                output_buffer = StringIO()
                sys.stdout = output_buffer

                try:
                    # Execute the plotting code
                    exec(code, globals_dict, locals_dict)
                finally:
                    # Always restore stdout — even if exec explodes
                    sys.stdout = old_stdout

                # Optional: log captured output (uncomment for debug runs)
                # captured = output_buffer.getvalue()
                # if captured.strip():
                #     print(f"[DEBUG] Captured output from plot {i} in {file_path}:\n{captured}", file=sys.stderr)

                # Grab the current figure if one was created
                fig = plt.gcf()
                if fig.get_axes():  # Actually has a plot
                    # Create unique, readable filename
                    base_name = os.path.basename(file_path).replace('.md', '')
                    filename = f"plot_{base_name}_{i}.png"
                    filepath = os.path.join(diagrams_dir, filename)
                    os.makedirs(diagrams_dir, exist_ok=True)

                    # Save with nice margins
                    fig.savefig(filepath, format='png', bbox_inches='tight', dpi=150)
                    plt.clf()  # Clear figure for next plot

                    # Prepare markdown image embed
                    image_md = f'\n![Generated Plot {i+1} — {base_name}]({filepath})\n'

                    # Reconstruct the original block for replacement
                    block = f'```python\n{code}\n```'
                    new_block = block + image_md

                    # Find and replace in content (using offset to handle multiple)
                    block_start = new_content.find(block, offset)
                    if block_start != -1:
                        block_end = block_start + len(block)
                        new_content = (
                            new_content[:block_end]
                            + image_md
                            + new_content[block_end:]
                        )
                        offset = block_end + len(image_md)

                else:
                    print(f"[SKIP] No plot generated in code block {i} of {file_path}", file=sys.stderr)

            except Exception as e:
                print(f"Error rendering plot {i} in {file_path}: {type(e).__name__}: {e}", file=sys.stderr)

    # Write the updated markdown back to disk
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Processed {file_path} — {len(matches)} python blocks checked", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python render_matplotlib.py path/to/file.md")
        sys.exit(1)
    process_md(sys.argv[1])