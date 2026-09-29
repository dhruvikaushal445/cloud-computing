# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(r"c:\Users\Dhruvi\Documents\Cloud Computing\index.html")
html = p.read_text(encoding="utf-8")


def insert_before(html: str, needle: str, diagram: str) -> str:
    if diagram.strip()[:50] in html:
        print("SKIP already:", needle[:60].replace("\n", " "))
        return html
    if needle not in html:
        raise SystemExit("MISSING needle:\n" + needle[:120])
    return html.replace(needle, diagram + "\n" + needle, 1)


pairs = [
    (
        """<h3 class="sec">Challenges of Cloud Computing</h3>
<p>From the study notes and challenge diagram, important challenges include:</p>""",
        """
<div class="ez-diag">
  <div class="dtitle">Cloud = Internet Access to Remote Services</div>
  <div class="ez-row">
    <div class="ez-box">Many Users</div>
    <span class="ez-arr">&rarr;</span>
    <div class="ez-cloud">Internet Cloud</div>
    <span class="ez-arr">&rarr;</span>
    <div class="ez-box">Remote Data Center</div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-1 E-Notes — Page 3</div>
</div>
""",
    ),
    (
        """<div class="remember"><strong>Important Points to Remember</strong><ul><li>Definition focuses on Internet-based storage and on-demand computing services.""",
        """
<div class="ez-diag">
  <div class="dtitle">Cloud Computing — Simple View</div>
  <div class="ez-row">
    <div class="ez-box">Users</div>
    <span class="ez-arr">&rarr;</span>
    <div class="ez-box">Internet</div>
    <span class="ez-arr">&rarr;</span>
    <div class="ez-cloud">Cloud Data Center<br><span class="ez-tiny">Servers · Storage · Network · DB</span></div>
  </div>
  <div class="ez-row" style="margin-top:.55rem">
    <div class="ez-box ez-soft">Backup</div>
    <div class="ez-box ez-soft">Collaboration</div>
    <div class="ez-box ez-soft">Accessibility</div>
    <div class="ez-box ez-soft">Mobility</div>
    <div class="ez-box ez-soft">Pay-per-use</div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-1 E-Notes — Pages 3–4</div>
</div>
""",
    ),
    (
        """<div class="remember"><strong>Important Points to Remember</strong><ul><li>Virtualization = virtual version of server/desktop/storage/OS/network.""",
        """
<div class="ez-diag">
  <div class="dtitle">Virtualization Idea (1 Physical → Many Virtual)</div>
  <div class="ez-vs">
    <div class="ez-box ez-bad">Without Virtualization<br><span class="ez-tiny">1 OS on 1 physical machine</span></div>
    <div class="ez-arr">&rArr;</div>
    <div class="ez-box ez-good">With Virtualization<br><span class="ez-tiny">VM1 · VM2 · VM3 on 1 physical host</span></div>
  </div>
  <div class="ez-row" style="margin-top:.55rem">
    <div class="ez-box">Physical Hardware</div>
    <span class="ez-arr">&uarr;</span>
    <div class="ez-cloud">Hypervisor / VMM</div>
    <span class="ez-arr">&uarr;</span>
    <div class="ez-box ez-soft">Multiple Users / OS</div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-1 E-Notes — Page 23 &amp; Unit-3 — Page 25</div>
</div>
""",
    ),
    (
        """<h3 class="sec">1. Hardware Virtualization</h3>""",
        """
<div class="ez-diag">
  <div class="dtitle">Types of Virtualization</div>
  <div class="ez-grid4">
    <div class="ez-box">Hardware<br><span class="ez-tiny">VMM on hardware</span></div>
    <div class="ez-box">Operating System<br><span class="ez-tiny">VMM on Host OS</span></div>
    <div class="ez-box">Server<br><span class="ez-tiny">1 server → many</span></div>
    <div class="ez-box">Storage<br><span class="ez-tiny">Many disks → 1 pool</span></div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-1 E-Notes — Pages 24–28</div>
</div>
""",
    ),
    (
        """<h3 class="sec">Key Points</h3>
<ol>
<li>Managed from a central location / hosted on a remote server</li>""",
        """
<div class="ez-diag">
  <div class="dtitle">How SaaS Works</div>
  <div class="ez-row">
    <div class="ez-box">User</div>
    <span class="ez-arr">&rarr;</span>
    <div class="ez-box">Web Browser</div>
    <span class="ez-arr">&rarr;</span>
    <div class="ez-box">Internet</div>
    <span class="ez-arr">&rarr;</span>
    <div class="ez-cloud">CSP Hosted App<br><span class="ez-tiny">e.g. Google Workspace</span></div>
  </div>
  <div class="ez-row" style="margin-top:.5rem">
    <div class="ez-box ez-good">No Install</div>
    <div class="ez-box ez-good">No Maintenance</div>
    <div class="ez-box ez-good">Auto Updates</div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on SaaS E-Notes — Pages 1–2 &amp; Unit-1 — Page 32</div>
</div>
""",
    ),
    (
        """<div class="remember"><strong>Important Points to Remember</strong><ul><li>Eight major SaaS challenges appear in the notes:""",
        """
<div class="ez-diag">
  <div class="dtitle">SaaS Challenges at a Glance</div>
  <div class="ez-grid4">
    <div class="ez-box ez-bad">Security &amp; Privacy</div>
    <div class="ez-box ez-bad">Internet Dependency</div>
    <div class="ez-box ez-bad">Limited Customization</div>
    <div class="ez-box ez-bad">Integration Complexity</div>
    <div class="ez-box ez-bad">Vendor Lock-in</div>
    <div class="ez-box ez-bad">Performance / Reliability</div>
    <div class="ez-box ez-bad">Compliance / Legal</div>
    <div class="ez-box ez-bad">Frequent Updates</div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on SaaS E-Notes — Pages 10–16</div>
</div>
""",
    ),
    (
        """<p><strong>Conclusion:</strong> Because of API differences, sync problems, error-handling complexity, legacy constraints and frequent vendor changes, SaaS integration is complex and time-consuming—hence the statement is justified.</p>""",
        """
<div class="ez-diag">
  <div class="dtitle">Why SaaS Integration is Hard</div>
  <div class="ez-row">
    <div class="ez-box">SaaS App A</div>
    <div class="ez-box">SaaS App B</div>
    <div class="ez-box">Legacy System</div>
  </div>
  <div class="ez-row" style="margin:.35rem 0"><span class="ez-arr">Different APIs · Sync issues · Updates break links</span></div>
  <div class="ez-row">
    <div class="ez-box ez-soft">Need: API knowledge</div>
    <div class="ez-box ez-soft">Middleware</div>
    <div class="ez-box ez-soft">iPaaS</div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on SaaS E-Notes — Pages 12, 16, 17, 21</div>
</div>
""",
    ),
    (
        """<h3 class="sec">Benefits</h3>
<ul>
<li>Centralized view of data across tools</li>""",
        """
<div class="ez-diag">
  <div class="dtitle">SaaS Integration Services</div>
  <div class="ez-row">
    <div class="ez-box">CRM</div>
    <div class="ez-box">ERP</div>
    <div class="ez-box">HRM</div>
  </div>
  <div class="ez-row" style="margin:.4rem 0"><span class="ez-arr">connected by</span></div>
  <div class="ez-row">
    <div class="ez-box ez-good">APIs</div>
    <div class="ez-box ez-good">Middleware</div>
    <div class="ez-box ez-good">iPaaS</div>
  </div>
  <div class="ez-row" style="margin-top:.4rem"><div class="ez-cloud">Consistent data flow · Automated processes · No silos</div></div>
  <div class="cap"><strong>Diagram Source:</strong> Based on SaaS E-Notes — Pages 17–20</div>
</div>
""",
    ),
    (
        """<div class="remember"><strong>Important Points to Remember</strong><ul><li>Product integration links CRM/ERP/HRM/Marketing/E-commerce tools.""",
        """
<div class="ez-diag">
  <div class="dtitle">Product + Platform Integration</div>
  <div class="ez-grid2">
    <div>
      <div class="ez-box" style="width:100%;margin-bottom:.35rem">Products</div>
      <div class="ez-box ez-soft" style="width:100%;margin-bottom:.25rem">CRM → Marketing / ERP</div>
      <div class="ez-box ez-soft" style="width:100%;margin-bottom:.25rem">ERP → HRM / Finance</div>
      <div class="ez-box ez-soft" style="width:100%">E-Commerce → Inventory</div>
    </div>
    <div>
      <div class="ez-box" style="width:100%;margin-bottom:.35rem">Platforms</div>
      <div class="ez-box ez-soft" style="width:100%;margin-bottom:.25rem">AWS — Hosting / AI</div>
      <div class="ez-box ez-soft" style="width:100%;margin-bottom:.25rem">Azure — Identity (AD)</div>
      <div class="ez-box ez-soft" style="width:100%">Heroku — Deploy SaaS</div>
    </div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on SaaS E-Notes — Pages 22–24</div>
</div>
""",
    ),
    (
        """<div class="remember"><strong>Important Points to Remember</strong><ul><li>IaaS = rent virtualized infrastructure over Internet (also called HaaS).""",
        """
<div class="ez-diag">
  <div class="dtitle">IaaS Model</div>
  <div class="ez-vs">
    <div class="ez-box ez-bad">Buy Own Hardware<br><span class="ez-tiny">High cost &amp; maintenance</span></div>
    <div class="ez-arr">&rArr;</div>
    <div class="ez-box ez-good">Rent from CSP (IaaS)<br><span class="ez-tiny">VM · Storage · Network</span></div>
  </div>
  <div class="ez-row" style="margin-top:.5rem">
    <div class="ez-box ez-soft">On-demand</div>
    <div class="ez-box ez-soft">Scalable</div>
    <div class="ez-box ez-soft">Pay-as-you-go</div>
    <div class="ez-box ez-soft">Virtualized</div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-3 Notes — Pages 1–3 &amp; Unit-1 — Page 30</div>
</div>
""",
    ),
    (
        """<div class="remember"><strong>Important Points to Remember</strong><ul><li>Virtual provisioning = on-demand allocation from a shared storage pool""",
        """
<div class="ez-diag">
  <div class="dtitle">Traditional vs Virtual Provisioning</div>
  <div class="ez-vs">
    <div class="ez-box ez-bad">Traditional<br><span class="ez-tiny">Allot for future growth now → Over-provisioning → Waste</span></div>
    <div class="ez-arr">vs</div>
    <div class="ez-box ez-good">Virtual Provisioning<br><span class="ez-tiny">Larger LUN shown · Physical storage allotted on demand</span></div>
  </div>
  <div class="ez-row" style="margin-top:.5rem">
    <div class="ez-cloud">Shared Storage Pool</div>
    <span class="ez-arr">on-demand</span>
    <div class="ez-box">Application / VM</div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-3 Notes — Pages 7–9</div>
</div>
""",
    ),
    (
        """<h3 class="sec">Migration Techniques</h3>
<p>Two important techniques are <strong>Pre-Copy Migration</strong> and <strong>Post-Copy Migration</strong>.</p>""",
        """
<div class="ez-diag">
  <div class="dtitle">VM Migration Types</div>
  <div class="ez-row">
    <div class="ez-box">Source Host</div>
    <span class="ez-arr">VM moves</span>
    <div class="ez-box">Destination Host</div>
  </div>
  <div class="ez-row" style="margin-top:.55rem">
    <div class="ez-box ez-soft">Cold<br><span class="ez-tiny">Power off first</span></div>
    <div class="ez-box ez-soft">Warm<br><span class="ez-tiny">No suspend source</span></div>
    <div class="ez-box ez-good">Live<br><span class="ez-tiny">Running VM moves</span></div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-3 Notes — Page 11</div>
</div>
""",
    ),
    (
        """<h3 class="sec">Steps of Integration</h3>""",
        """
<div class="ez-diag">
  <div class="dtitle">Integration of Public + Private = Hybrid</div>
  <div class="ez-row">
    <div class="ez-box ez-soft">Private Cloud<br><span class="ez-tiny">Control · Security · Sensitive data</span></div>
    <span class="ez-arr">+</span>
    <div class="ez-box ez-soft">Public Cloud<br><span class="ez-tiny">Scale · Elastic · On-demand</span></div>
    <span class="ez-arr">=</span>
    <div class="ez-cloud">Hybrid Cloud</div>
  </div>
  <div class="ez-row" style="margin-top:.5rem">
    <div class="ez-box">Private (normal load)</div>
    <span class="ez-arr">Cloud Bursting</span>
    <div class="ez-box ez-good">Public (peak demand)</div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-3 Notes — Pages 20–22</div>
</div>
""",
    ),
    (
        """<div class="remember"><strong>Important Points to Remember</strong><ul><li>Three core technologies in notes: Virtualization, SOA, Grid Computing""",
        """
<div class="ez-diag">
  <div class="dtitle">Three Cloud Technologies</div>
  <div class="ez-row">
    <div class="ez-box ez-good">1. Virtualization<br><span class="ez-tiny">Many OS on one machine</span></div>
    <div class="ez-box ez-good">2. SOA<br><span class="ez-tiny">Services communicate on network</span></div>
    <div class="ez-box ez-good">3. Grid Computing<br><span class="ez-tiny">Big job split across machines</span></div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-3 Notes — Pages 25–27</div>
</div>
""",
    ),
    (
        """<div class="source"><strong>Source from Provided Material</strong><br>Unit-1 E-Notes — Pages 7–12</div>""",
        """
<div class="ez-diag">
  <div class="dtitle">Public vs Private — Quick Picture</div>
  <div class="ez-vs">
    <div class="ez-box ez-soft">Public Cloud<br><span class="ez-tiny">Open to all · CSP managed · Pay-per-use · Less secure</span></div>
    <div class="ez-arr">vs</div>
    <div class="ez-box ez-good">Private Cloud<br><span class="ez-tiny">Internal · Full control · High security · Skilled staff needed</span></div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-1 E-Notes — Pages 7–12</div>
</div>
""",
    ),
    (
        """<p><strong>Examples:</strong> Google Application Suite (Gmail, Google Apps, Google Drive), Office 365, Amazon Web Services.</p>
<h3 class="sec">Advantages</h3>""",
        """
<div class="ez-diag">
  <div class="dtitle">Hybrid Cloud Formula</div>
  <div class="ez-row">
    <div class="ez-cloud">Public Cloud</div>
    <span class="ez-arr">+</span>
    <div class="ez-box">Private Cloud</div>
    <span class="ez-arr">=</span>
    <div class="ez-box ez-good">Hybrid Cloud</div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-1 E-Notes — Page 13</div>
</div>
""",
    ),
    (
        """<p><strong>Example:</strong> Health Care community cloud.</p>""",
        """
<div class="ez-diag">
  <div class="dtitle">Community Cloud</div>
  <div class="ez-row">
    <div class="ez-box">Org A</div>
    <div class="ez-box">Org B</div>
    <div class="ez-box">Org C</div>
  </div>
  <div class="ez-row" style="margin:.35rem 0"><span class="ez-arr">share</span></div>
  <div class="ez-row"><div class="ez-cloud">Community Cloud<br><span class="ez-tiny">e.g. Health Care community</span></div></div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-1 E-Notes — Pages 16–17</div>
</div>
""",
    ),
    (
        """<table class="cmp">
<thead><tr><th>Basis</th><th>IaaS</th><th>PaaS</th><th>SaaS</th></tr></thead>""",
        """
<div class="ez-diag">
  <div class="dtitle">Service Model Pyramid</div>
  <div class="svc-stack" style="margin:.2rem auto">
    <div class="layer saas">SaaS — Use software</div>
    <div class="layer paas">PaaS — Build apps</div>
    <div class="layer iaas">IaaS — Rent infrastructure</div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-1 E-Notes — Pages 30–32</div>
</div>
""",
    ),
    (
        """<h3 class="sec">Characteristics</h3>
<ol>
<li>Accessible to various users via the same development application</li>""",
        """
<div class="ez-diag">
  <div class="dtitle">PaaS for Developers</div>
  <div class="ez-row">
    <div class="ez-box">Programmer</div>
    <span class="ez-arr">&rarr;</span>
    <div class="ez-cloud">PaaS Platform<br><span class="ez-tiny">Develop · Test · Run · Manage</span></div>
    <span class="ez-arr">&rarr;</span>
    <div class="ez-box ez-good">Application</div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-1 E-Notes — Page 31</div>
</div>
""",
    ),
    (
        """<h3 class="sec">Methods</h3>
<ol>
<li><span class="pt">Static Provisioning:</span> Predictable and unchanging demands;""",
        """
<div class="ez-diag">
  <div class="dtitle">Resource Provisioning Methods</div>
  <div class="ez-row">
    <div class="ez-box ez-soft">Static<br><span class="ez-tiny">Fixed / advance / flat fee</span></div>
    <div class="ez-box ez-good">Dynamic<br><span class="ez-tiny">Add/remove as demand changes</span></div>
    <div class="ez-box ez-soft">User-Self<br><span class="ez-tiny">Buy from web + account</span></div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-3 Notes — Pages 29–30</div>
</div>
""",
    ),
    (
        """<p><strong>Cloud infrastructure management</strong> comprises the processes and tools needed to effectively allocate and deliver key resources when and where they are required.""",
        """
<div class="ez-diag">
  <div class="dtitle">Cloud Infrastructure Building Blocks</div>
  <div class="ez-row">
    <div class="ez-box">Compute<br><span class="ez-tiny">(Server)</span></div>
    <div class="ez-box">Networking</div>
    <div class="ez-box">Storage</div>
    <div class="ez-box">Virtualization</div>
  </div>
  <div class="ez-row" style="margin-top:.45rem"><div class="ez-cloud">Managed via UI / Dashboard</div></div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-1 E-Notes — Pages 19–20</div>
</div>
""",
    ),
    (
        """<p>From the SaaS E-Notes, important characteristics are:</p>""",
        """
<div class="ez-diag">
  <div class="dtitle">SaaS Characteristics</div>
  <div class="ez-grid4">
    <div class="ez-box ez-soft">Multi-tenancy</div>
    <div class="ez-box ez-soft">Subscription scale</div>
    <div class="ez-box ez-soft">Auto updates</div>
    <div class="ez-box ez-soft">Anywhere access</div>
    <div class="ez-box ez-soft">Security &amp; SLAs</div>
    <div class="ez-box ez-soft">Central management</div>
    <div class="ez-box ez-soft">Remote hosting</div>
    <div class="ez-box ez-soft">Pay-as-per-use</div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on SaaS E-Notes — Page 3 &amp; Unit-1 — Page 32</div>
</div>
""",
    ),
    (
        """<h3 class="sec">Utility Computing</h3>""",
        """
<div class="ez-diag">
  <div class="dtitle">Grid Computing Idea</div>
  <div class="ez-row">
    <div class="ez-box ez-bad">Huge Job</div>
    <span class="ez-arr">split</span>
    <div class="ez-box">PC 1</div>
    <div class="ez-box">PC 2</div>
    <div class="ez-box">PC 3</div>
    <span class="ez-arr">&rarr;</span>
    <div class="ez-box ez-good">Result</div>
  </div>
  <div class="cap"><strong>Diagram Source:</strong> Based on Unit-3 Notes — Page 27</div>
</div>
""",
    ),
]

# Fix accidental wrong closing tags in diagrams (used </div> instead of </span> for ez-arr)
fixed_pairs = []
for needle, diagram in pairs:
    diagram = diagram.replace('<div class="ez-arr">&rArr;</div>', '<span class="ez-arr">&rArr;</span>')
    diagram = diagram.replace('<div class="ez-arr">vs</div>', '<span class="ez-arr">vs</span>')
    fixed_pairs.append((needle, diagram))

for needle, diagram in fixed_pairs:
    html = insert_before(html, needle, diagram)

p.write_text(html, encoding="utf-8")
print("Done. Size:", p.stat().st_size)
print("ez-diag count:", html.count('class="ez-diag"'))
