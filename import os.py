import os

mapping = {
    'dashboard.html': 'dashboard',
    'dataroom.html': 'data-room',
    'team.html': 'team-management',
    'payments.html': 'payments-invoices',
    'reports.html': 'reports-analytics',
    'settings.html': 'settings'
}

with open('index.html', 'r') as f:
    base_html = f.read()

for filename, section_id in mapping.items():
    filepath = os.path.join('pages', filename)
    
    # Replace the initialization section
    new_html = base_html.replace("changeSection('dashboard');", f"changeSection('{section_id}');")
    
    with open(filepath, 'w') as f:
        f.write(new_html)
    print(f"Generated {filepath} for section {section_id}")
