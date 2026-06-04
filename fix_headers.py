import glob

html_files = glob.glob('**/*.html', recursive=True)

import re

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # We want to insert the Theme Switcher between the INR div and the bell/notifications div
    # Search for the INR div closing tag, which is followed by the notifications div or border-l div
    
    # First, let's find if it already has the theme switcher
    if 'data-lucide="sun"' in content:
        continue

    # Let's replace the block containing INR down to the border-l
    pattern = r'(<span class="text-xs font-bold text-slate-700">INR.*?</span>\s*<i data-lucide="chevron-down".*?</i>\s*</div>)'
    
    # Replacement string to append theme switcher
    replacement = r'\1\n\n                    <!-- Theme Switcher -->\n                    <button class="text-slate-400 hover:text-orange-500 transition-colors">\n                        <i data-lucide="sun" class="w-4 h-4"></i>\n                    </button>\n'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(file, 'w') as f:
            f.write(new_content)
        print(f"Fixed header in {file}")

