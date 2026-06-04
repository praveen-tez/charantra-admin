import os
import glob

html_files = glob.glob('**/*.html', recursive=True)

old_str = """                    <div class="flex items-center gap-2 bg-slate-50 px-3 py-1.5 rounded-md border border-slate-100">
                        <span class="text-xs font-bold text-slate-700">INR (₹)</span>
                        <i data-lucide="chevron-down" class="w-3 h-3 text-slate-400"></i>
                    </div>

                    <div class="flex items-center gap-3 border-l border-slate-100 pl-6">"""

new_str = """                    <div class="flex items-center gap-2 bg-slate-50 px-3 py-1.5 rounded-md border border-slate-100 cursor-pointer">
                        <span class="text-xs font-bold text-slate-700">INR (₹)</span>
                        <i data-lucide="chevron-down" class="w-3 h-3 text-slate-400"></i>
                    </div>

                    <!-- Theme Switcher -->
                    <button class="text-slate-400 hover:text-orange-500 transition-colors">
                        <i data-lucide="sun" class="w-4 h-4"></i>
                    </button>
                    
                    <!-- Notifications -->
                    <button class="text-slate-400 hover:text-orange-500 transition-colors relative">
                        <i data-lucide="bell" class="w-4 h-4"></i>
                        <span class="absolute -top-1 -right-1 w-2 h-2 bg-orange-500 rounded-full"></span>
                    </button>

                    <div class="flex items-center gap-3 border-l border-slate-100 pl-6">"""

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(file, 'w') as f:
            f.write(content)
        print(f"Updated header in {file}")

