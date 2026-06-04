import re

with open('pages/mandates.html', 'r') as f:
    content = f.read()

# Replace button onclick
old_btn = """<button onclick="changeSection('create')" class="bg-[#F97316] hover:bg-[#EA580C] text-white font-bold text-xs py-2.5 px-6 rounded-md transition-all shadow-md shadow-orange-500/10 flex items-center gap-1.5">
                                <i data-lucide="plus" class="w-4 h-4"></i>
                                <span>Assign Mandate</span>
                            </button>"""
new_btn = """<button onclick="triggerAssignMandateModal()" class="bg-[#F97316] hover:bg-[#EA580C] text-white font-bold text-xs py-2.5 px-6 rounded-md transition-all shadow-md shadow-orange-500/10 flex items-center gap-1.5">
                                <i data-lucide="plus" class="w-4 h-4"></i>
                                <span>Assign Mandate</span>
                            </button>"""

if old_btn in content:
    content = content.replace(old_btn, new_btn)

# Now inject the new modal function
# We can just put it at the bottom before </body> or inside a <script> block
modal_func = """
        function triggerAssignMandateModal() {
            const container = document.getElementById('modal-container');
            const mandatesListHTML = appState.mandates.map(m => `<option value="${m.id}">${m.name} - ${m.company}</option>`).join('');
            const ibPersons = ['Akash Kumar', 'Neha Sharma', 'Vikram Das', 'Priya Singh'];
            const ibPersonsHTML = ibPersons.map(p => `<option value="${p}">${p} (IB Person)</option>`).join('');

            container.innerHTML = `
                <div class="bg-white rounded-md p-6 max-w-lg w-full shadow-2xl border border-slate-100 space-y-4 fade-in-view">
                    <div class="flex justify-between items-center border-b pb-3">
                        <h3 class="text-base font-black text-slate-900 tracking-tight">Assign Mandate</h3>
                        <button onclick="closeModal()" class="text-slate-400 hover:text-slate-600"><i data-lucide="x" class="w-5 h-5"></i></button>
                    </div>
                    <div class="space-y-4">
                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">Select Mandate</label>
                            <select id="assign-mandate-select" class="w-full p-2 border border-slate-200 rounded-md text-xs focus:outline-none focus:border-orange-500">
                                ${mandatesListHTML}
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">Assign to IB Person</label>
                            <select id="assign-ib-select" class="w-full p-2 border border-slate-200 rounded-md text-xs focus:outline-none focus:border-orange-500">
                                ${ibPersonsHTML}
                            </select>
                        </div>
                    </div>
                    <div class="flex justify-end gap-3 pt-4">
                        <button onclick="closeModal()" class="px-4 py-2 border border-slate-200 text-slate-600 rounded-md text-xs font-bold hover:bg-slate-50 transition">Cancel</button>
                        <button onclick="triggerToast('Mandate assigned successfully to IB Person.'); closeModal();" class="px-4 py-2 bg-orange-600 text-white rounded-md text-xs font-bold hover:bg-orange-700 transition">Assign Mandate</button>
                    </div>
                </div>
            `;
            container.classList.remove('hidden');
            container.classList.add('modal-active');
            lucide.createIcons();
        }
"""

if "function triggerAssignMandateModal" not in content:
    content = content.replace("</script>\n</body>", modal_func + "\n</script>\n</body>")
    
with open('pages/mandates.html', 'w') as f:
    f.write(content)

print("Updated mandates.html successfully")
