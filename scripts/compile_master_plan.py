import subprocess
import os

markdown_file = "/Users/angelzaragoza/Desktop/KessokuDev/docs/mvp-estrategia/MASTER_PLAN_MVP_KESSOKU_DEV_2026.md"
html_file = "/Users/angelzaragoza/Desktop/KessokuDev/docs/mvp-estrategia/MASTER_PLAN_MVP_KESSOKU_DEV_2026.html"
pdf_file = "/Users/angelzaragoza/Desktop/KessokuDev/docs/mvp-estrategia/MASTER_PLAN_MVP_KESSOKU_DEV_2026.pdf"

with open(markdown_file, "r", encoding="utf-8") as f:
    md_content = f.read()

# Simple Markdown to clean HTML conversion
import re

html_body = md_content
# Code blocks
html_body = re.sub(r'```([a-z]*)\n(.*?)```', r'<pre><code>\2</code></pre>', html_body, flags=re.DOTALL)
# Tables
lines = html_body.split('\n')
in_table = False
table_lines = []
processed_lines = []

for line in lines:
    if line.strip().startswith('|') and line.strip().endswith('|'):
        if not in_table:
            in_table = True
            table_lines = [line]
        else:
            table_lines.append(line)
    else:
        if in_table:
            in_table = False
            # Render table
            headers = [h.strip() for h in table_lines[0].split('|')[1:-1]]
            html_table = '<div class="table-container"><table><thead><tr>'
            for h in headers:
                html_table += f'<th>{h}</th>'
            html_table += '</tr></thead><tbody>'
            for row in table_lines[2:]:
                cells = [c.strip() for c in row.split('|')[1:-1]]
                html_table += '<tr>'
                for c in cells:
                    html_table += f'<td>{c}</td>'
                html_table += '</tr>'
            html_table += '</tbody></table></div>'
            processed_lines.append(html_table)
            table_lines = []
        processed_lines.append(line)

if in_table:
    headers = [h.strip() for h in table_lines[0].split('|')[1:-1]]
    html_table = '<div class="table-container"><table><thead><tr>'
    for h in headers:
        html_table += f'<th>{h}</th>'
    html_table += '</tr></thead><tbody>'
    for row in table_lines[2:]:
        cells = [c.strip() for c in row.split('|')[1:-1]]
        html_table += '<tr>'
        for c in cells:
            html_table += f'<td>{c}</td>'
        html_table += '</tr>'
    html_table += '</tbody></table></div>'
    processed_lines.append(html_table)

html_body = '\n'.join(processed_lines)

# Headers
html_body = re.sub(r'^# (.*)$', r'<h1>\1</h1>', html_body, flags=re.MULTILINE)
html_body = re.sub(r'^## (.*)$', r'<h2>\1</h2>', html_body, flags=re.MULTILINE)
html_body = re.sub(r'^### (.*)$', r'<h3>\1</h3>', html_body, flags=re.MULTILINE)
html_body = re.sub(r'^#### (.*)$', r'<h4>\1</h4>', html_body, flags=re.MULTILINE)

# Bold & Italic
html_body = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_body)
html_body = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html_body)

# Blockquotes
html_body = re.sub(r'^> (.*)$', r'<blockquote>\1</blockquote>', html_body, flags=re.MULTILINE)

# Horizontal rule
html_body = re.sub(r'^---$', r'<hr/>', html_body, flags=re.MULTILINE)

# Paragraphs and lists
html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Master Plan MVP - Kessoku Dev 2026</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
  @page {{
    size: A4;
    margin: 18mm 16mm 20mm 16mm;
    @bottom-right {{
      content: counter(page);
    }}
  }}
  body {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #0f172a;
    line-height: 1.6;
    font-size: 12.5px;
    background: #fff;
    margin: 0;
    padding: 24px;
  }}
  h1 {{
    font-size: 22px;
    font-weight: 800;
    color: #1e3a8a;
    border-bottom: 2px solid #3b82f6;
    padding-bottom: 8px;
    margin-top: 0;
  }}
  h2 {{
    font-size: 16px;
    font-weight: 700;
    color: #1d4ed8;
    margin-top: 24px;
    margin-bottom: 10px;
    border-left: 4px solid #2563eb;
    padding-left: 8px;
  }}
  h3 {{
    font-size: 13.5px;
    font-weight: 700;
    color: #0f172a;
    margin-top: 18px;
    margin-bottom: 8px;
  }}
  pre {{
    background: #0f172a;
    color: #f8fafc;
    padding: 12px 16px;
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    overflow-x: auto;
    line-height: 1.45;
  }}
  code {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
  }}
  .table-container {{
    margin: 14px 0;
    overflow-x: auto;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 11px;
  }}
  th, td {{
    border: 1px solid #cbd5e1;
    padding: 7px 10px;
    text-align: left;
  }}
  th {{
    background: #f1f5f9;
    font-weight: 700;
    color: #0f172a;
  }}
  tr:nth-child(even) {{
    background: #f8fafc;
  }}
  blockquote {{
    border-left: 4px solid #d97706;
    background: #fffbeb;
    padding: 8px 14px;
    margin: 12px 0;
    font-size: 12px;
    color: #92400e;
  }}
  hr {{
    border: 0;
    border-top: 1px solid #e2e8f0;
    margin: 20px 0;
  }}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_doc)

chrome_cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--print-to-pdf={pdf_file}",
    html_file
]

subprocess.run(chrome_cmd, check=True)
print(f"Generated PDF successfully at {pdf_file}")
