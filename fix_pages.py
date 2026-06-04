import os
import re
import glob

# The exact sidebar HTML to inject
sidebar_html = """        <!-- SIDEBAR -->
        <aside class="w-80 bg-[#0B0C0E] text-[#94A3B8] flex flex-col fixed h-screen z-50">
            <!-- Brand Identity -->
            <div class="p-6 border-b border-zinc-900 flex-shrink-0">
                <a href="/index.html">
                    <img src="/assets/logo.png" width="200" alt="Charantra Logo" style="width: 200px; height: auto;">
                </a>
            </div>

            <!-- Sidebar Navigation Menu -->
            <div class="flex-1 overflow-y-auto sidebar-scroll p-4 space-y-1.5">
                <p class="text-[10px] uppercase font-bold tracking-widest text-zinc-600 px-3.5 mb-2 mt-2">Executive Desk</p>
                
                <a href="/pages/dashboard.html" class="block">
                    <button id="nav-dashboard" class="sidebar-btn w-full flex items-center gap-3 px-3.5 py-2.5 text-[13px] font-medium rounded-md text-[#94A3B8] hover:text-white hover:bg-[#1E2128]/40 transition-all">
                        <i data-lucide="layout-dashboard" class="w-4 h-4"></i>
                        <span>Dashboard</span>
                    </button>
                </a>
                
                <a href="/pages/crm.html" class="block">
                    <button id="nav-crm" class="sidebar-btn w-full flex items-center gap-3 px-3.5 py-2.5 text-[13px] font-medium rounded-md text-[#94A3B8] hover:text-white hover:bg-[#1E2128]/40 transition-all">
                        <i data-lucide="contact-2" class="w-4 h-4"></i>
                        <span>CRM & Users</span>
                    </button>
                </a>
                
                <a href="/pages/deals.html" class="block">
                    <button id="nav-deals" class="sidebar-btn w-full flex items-center gap-3 px-3.5 py-2.5 text-[13px] font-medium rounded-md text-[#94A3B8] hover:text-white hover:bg-[#1E2128]/40 transition-all">
                        <i data-lucide="git-pull-request" class="w-4 h-4"></i>
                        <span>Deals & M&A Pipeline</span>
                    </button>
                </a>

                <a href="/pages/mandates.html" class="block">
                    <button id="nav-mandates" class="sidebar-btn w-full flex items-center gap-3 px-3.5 py-2.5 text-[13px] font-medium rounded-md text-[#94A3B8] hover:text-white hover:bg-[#1E2128]/40 transition-all">
                        <i data-lucide="file-signature" class="w-4 h-4"></i>
                        <span>Mandates & Projects</span>
                    </button>
                </a>

                <p class="text-[10px] uppercase font-bold tracking-widest text-zinc-600 px-3.5 mb-2 mt-4">Audits & Governance</p>
                
                <a href="/pages/dataroom.html" class="block">
                    <button id="nav-data-room" class="sidebar-btn w-full flex items-center gap-3 px-3.5 py-2.5 text-[13px] font-medium rounded-md text-[#94A3B8] hover:text-white hover:bg-[#1E2128]/40 transition-all">
                        <i data-lucide="hard-drive" class="w-4 h-4"></i>
                        <span>Data Room</span>
                    </button>
                </a>

                <a href="/pages/team.html" class="block">
                    <button id="nav-team-management" class="sidebar-btn w-full flex items-center gap-3 px-3.5 py-2.5 text-[13px] font-medium rounded-md text-[#94A3B8] hover:text-white hover:bg-[#1E2128]/40 transition-all">
                        <i data-lucide="users-2" class="w-4 h-4"></i>
                        <span>Team Management</span>
                    </button>
                </a>

                <a href="/pages/payments.html" class="block">
                    <button id="nav-payments-invoices" class="sidebar-btn w-full flex items-center gap-3 px-3.5 py-2.5 text-[13px] font-medium rounded-md text-[#94A3B8] hover:text-white hover:bg-[#1E2128]/40 transition-all">
                        <i data-lucide="receipt" class="w-4 h-4"></i>
                        <span>Payments</span>
                    </button>
                </a>

                <a href="/pages/reports.html" class="block">
                    <button id="nav-reports-analytics" class="sidebar-btn w-full flex items-center gap-3 px-3.5 py-2.5 text-[13px] font-medium rounded-md text-[#94A3B8] hover:text-white hover:bg-[#1E2128]/40 transition-all">
                        <i data-lucide="bar-chart-3" class="w-4 h-4"></i>
                        <span>Reports & Analytics</span>
                    </button>
                </a>

                <a href="/pages/settings.html" class="block">
                    <button id="nav-settings" class="sidebar-btn w-full flex items-center gap-3 px-3.5 py-2.5 text-[13px] font-medium rounded-md text-[#94A3B8] hover:text-white hover:bg-[#1E2128]/40 transition-all">
                        <i data-lucide="settings" class="w-4 h-4"></i>
                        <span>Settings</span>
                    </button>
                </a>
            </div>
        </aside>"""

# Dynamic active class script
script_html = """
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const currentPath = window.location.pathname;
            const buttons = document.querySelectorAll('.sidebar-btn');
            buttons.forEach(btn => {
                const parent = btn.parentElement;
                if (parent && parent.tagName === 'A') {
                    const href = parent.getAttribute('href');
                    if (currentPath.includes(href.split('/').pop()) || (currentPath === '/' && href.includes('dashboard.html'))) {
                        btn.classList.add('sidebar-item-active');
                    }
                }
            });
        });
    </script>
"""

sidebar_regex = re.compile(r'<!-- SIDEBAR -->\s*<aside.*?</aside>', re.DOTALL)
toast_html_regex = re.compile(r'<!-- GLOBAL NOTIFICATION CONSOLE -->\s*<div id="toast-notif".*?</div>', re.DOTALL)

for file_path in glob.glob('pages/*.html') + ['index.html']:
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Replace sidebar
    if sidebar_regex.search(content):
        content = sidebar_regex.sub(sidebar_html, content)

    # 2. Add dynamic active script right before </body>
    if 'const currentPath = window.location.pathname;' not in content:
        content = content.replace('</body>', script_html + '\n</body>')

    # 3. Ensure border-radius: 6px in CSS for sidebar-item-active and rounded-md
    if 'border-radius: 6px !important;' not in content:
        content = content.replace('.sidebar-item-active {', '.sidebar-item-active {\n            border-radius: 6px !important;')

    # 4. Remove toasts elements
    content = toast_html_regex.sub('', content)

    # 5. Modify JS triggerToast to do nothing
    content = re.sub(r'function triggerToast\([^\)]*\)\s*{[^}]*}', 'function triggerToast(m) {}', content, flags=re.DOTALL)
    # Some have nested logic for triggerToast, lets just replace the body of triggerToast using a simpler regex
    content = re.sub(r'function triggerToast\([^)]*\)\s*\{([^}]*setTimeout[^}]*\}|.*?)\}', 'function triggerToast(msg) { console.log(msg); }', content, flags=re.DOTALL)
    # Fallback if complex
    content = re.sub(r'function triggerToast\((.*?)\) \{.*?\}', r'function triggerToast(\1) {}', content, flags=re.DOTALL)
    
    # Let's completely remove any triggerToast calls that might cause issues, or just define a dummy function if missing.
    # We will redefine it globally in head just in case.

    # 6. Change all `rounded-xl`, `rounded-full` related to UI if necessary? 
    # "follow with border radius as 6px, dont use fully rounded"
    # Replacing all `rounded-xl`, `rounded-2xl`, `rounded-3xl`, `rounded-lg`, `rounded-full` to `rounded-md` (which is 6px) across the whole HTML?
    # Wait, doing global replace on `rounded-xl` -> `rounded-md` might be too aggressive, but he said "follow wth border radius as 6px , dont use fully rounded... inall teh pages, nevr evr felliek differnt ahre"
    content = re.sub(r'rounded-([a-z0-9]+)', lambda m: 'rounded-md' if m.group(1) in ['lg', 'xl', '2xl', '3xl', 'full'] and not 'scrollbar-thumb' in content[m.start()-50:m.start()] else m.group(0), content)
    # Revert rounded-full on avatar elements or just let it be rounded-md. He said "dont use fully rounded".
    content = re.sub(r'rounded-full', 'rounded-md', content)

    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"Updated {file_path}")

