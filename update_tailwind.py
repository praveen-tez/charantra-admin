import os
import glob

html_files = glob.glob('**/*.html', recursive=True)

tailwind_config = """    <script>
        tailwind.config = {
            theme: {
                extend: {
                    borderRadius: {
                        'none': '0',
                        'sm': '16px',
                        DEFAULT: '16px',
                        'md': '16px',
                        'lg': '16px',
                        'xl': '16px',
                        '2xl': '16px',
                        '3xl': '16px',
                        'full': '9999px'
                    }
                }
            }
        }
    </script>"""

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    if "tailwind.config" not in content and "<script src=\"https://cdn.tailwindcss.com\"></script>" in content:
        content = content.replace("<script src=\"https://cdn.tailwindcss.com\"></script>", "<script src=\"https://cdn.tailwindcss.com\"></script>\n" + tailwind_config)
        with open(file, 'w') as f:
            f.write(content)
        print(f"Updated {file}")

