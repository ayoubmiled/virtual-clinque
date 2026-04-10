import json
import codecs

notebook_path = r'c:\Users\AYOUB\classification\brain_tumor_text\brain_tumor_pipeline.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open('cells_dump.txt', 'w', encoding='utf-8') as f:
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            src = ''.join(cell['source'])
            f.write(f'=== Cell {i} ===\n')
            f.write(src)
            f.write('\n\n')
        elif cell['cell_type'] == 'markdown':
            f.write(f'=== Markdown Cell {i} ===\n')
            f.write('\n\n')
