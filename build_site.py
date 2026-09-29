# -*- coding: utf-8 -*-
"""Generate Cloud Computing A4 Exam Q&A study website from provided materials only."""
from pathlib import Path

OUT = Path(r"c:\Users\Dhruvi\Documents\Cloud Computing\index.html")

CSS = r"""
:root{
  --navy:#1a365d;
  --navy2:#2c5282;
  --ink:#1a202c;
  --muted:#4a5568;
  --paper:#fff;
  --bg:#d9dde3;
  --line:#cbd5e0;
  --source-bg:#f7fafc;
  --accent:#2b6cb0;
  --mark:#9b2c2c;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0;font-family:"Segoe UI",Tahoma,sans-serif;
  background:var(--bg);color:var(--ink);line-height:1.55;
}
.toolbar{
  position:sticky;top:0;z-index:100;
  background:var(--navy);color:#fff;
  display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;
  padding:.55rem .9rem;box-shadow:0 2px 8px rgba(0,0,0,.25);
}
.toolbar a,.toolbar button{
  color:#fff;text-decoration:none;background:transparent;
  border:1px solid rgba(255,255,255,.35);border-radius:4px;
  padding:.28rem .55rem;font-size:.82rem;cursor:pointer;
}
.toolbar a:hover,.toolbar button:hover{background:rgba(255,255,255,.12)}
.toolbar .search-wrap{margin-left:auto;display:flex;gap:.4rem;align-items:center}
.toolbar input[type=search]{
  border:none;border-radius:4px;padding:.35rem .55rem;min-width:180px;font-size:.85rem;
}
.site{max-width:920px;margin:1.2rem auto 3rem;padding:0 .75rem}
.a4{
  background:var(--paper);width:210mm;max-width:100%;
  min-height:297mm;margin:0 auto 1.25rem;
  padding:14mm 16mm 16mm;position:relative;
  box-shadow:0 2px 10px rgba(0,0,0,.18);
  page-break-after:always;break-after:page;
  font-family:"Times New Roman",Times,serif;font-size:12.2pt;
}
.page-header{
  border-bottom:2px solid var(--navy);padding-bottom:.35rem;margin-bottom:.9rem;
  display:flex;justify-content:space-between;gap:1rem;align-items:flex-end;
  font-family:"Segoe UI",Tahoma,sans-serif;font-size:.78rem;color:var(--muted);
}
.page-header strong{color:var(--navy);font-size:.9rem;display:block}
.page-footer{
  border-top:1px solid var(--line);margin-top:1.2rem;padding-top:.4rem;
  font-family:"Segoe UI",Tahoma,sans-serif;font-size:.72rem;color:var(--muted);
  display:flex;justify-content:space-between;
}
.meta-grid{
  display:grid;grid-template-columns:1fr 1fr;gap:.35rem .8rem;
  font-family:"Segoe UI",Tahoma,sans-serif;font-size:.8rem;color:var(--muted);
  margin-bottom:.8rem;border:1px solid var(--line);padding:.55rem .7rem;background:#fafbfc;
}
.meta-grid span{border-bottom:1px dotted #a0aec0}
.cover{text-align:center;display:flex;flex-direction:column;justify-content:center;min-height:250mm}
.cover h1{font-size:1.85rem;color:var(--navy);letter-spacing:.04em;margin:.4rem 0}
.cover h2{font-size:1.25rem;font-weight:600;margin:.2rem 0 1rem}
.cover .badge{
  display:inline-block;border:2px solid var(--navy);color:var(--navy);
  padding:.4rem 1rem;margin:1rem 0;font-family:"Segoe UI",sans-serif;font-size:.95rem;
}
.cover .uni{color:var(--mark);font-weight:700;font-size:1.05rem;margin-top:1.5rem}
.q-block{margin:1rem 0 1.4rem;break-inside:avoid}
.q-head{
  border:1.5px solid var(--navy);background:#eef3f9;padding:.55rem .75rem;margin-bottom:.7rem;
}
.q-head .qno{color:var(--navy);font-weight:700;font-family:"Segoe UI",sans-serif;font-size:.95rem}
.q-head .marks{float:right;color:var(--mark);font-weight:700;font-family:"Segoe UI",sans-serif;font-size:.85rem}
.q-head .qtext{clear:both;margin-top:.35rem;font-weight:700}
.ans-label{font-weight:700;color:var(--navy2);font-family:"Segoe UI",sans-serif;margin:.4rem 0}
h3.sec{font-size:1rem;color:var(--navy);margin:.85rem 0 .35rem;font-family:"Segoe UI",sans-serif}
p{margin:.35rem 0 .55rem}
ol,ul{margin:.3rem 0 .7rem;padding-left:1.3rem}
li{margin:.25rem 0}
li > span.pt{font-weight:700}
.source{
  margin-top:.85rem;padding:.5rem .7rem;background:var(--source-bg);
  border-left:3px solid var(--accent);font-family:"Segoe UI",sans-serif;font-size:.78rem;color:var(--muted);
}
.remember{
  margin-top:.7rem;padding:.55rem .7rem;border:1px dashed var(--navy2);background:#f8fbff;
  font-size:.95em;
}
.remember strong{font-family:"Segoe UI",sans-serif;color:var(--navy)}
table.cmp{
  width:100%;border-collapse:collapse;margin:.6rem 0 1rem;font-size:.92em;
  break-inside:avoid;
}
table.cmp th,table.cmp td{border:1px solid #718096;padding:.4rem .5rem;vertical-align:top}
table.cmp th{background:var(--navy);color:#fff;font-family:"Segoe UI",sans-serif;font-size:.85rem}
table.cmp tr:nth-child(even) td{background:#f7fafc}
.diagram{
  margin:.7rem auto;text-align:center;break-inside:avoid;max-width:100%;
}
.diagram img{max-width:100%;height:auto;border:1px solid var(--line)}
.diagram .cap{font-family:"Segoe UI",sans-serif;font-size:.75rem;color:var(--muted);margin-top:.3rem}
.toc a{color:var(--navy2);text-decoration:none}
.toc a:hover{text-decoration:underline}
.toc li{margin:.35rem 0}
.toc .marks{color:var(--mark);font-size:.85em}
.hl{background:#fefcbf}
.svc-stack{display:flex;flex-direction:column;gap:.35rem;max-width:420px;margin:.6rem auto}
.svc-stack .layer{
  border:2px solid var(--navy);padding:.55rem;text-align:center;font-family:"Segoe UI",sans-serif;font-weight:700;
}
.svc-stack .saas{background:#bee3f8}
.svc-stack .paas{background:#c6f6d5}
.svc-stack .iaas{background:#feebc8}
.flow{display:flex;flex-direction:column;align-items:center;gap:.25rem;font-family:"Segoe UI",sans-serif;font-size:.85rem;margin:.7rem 0}
.flow .box{border:1.5px solid var(--navy);padding:.35rem .7rem;min-width:220px;text-align:center;background:#f7fafc}
.flow .oval{border:1.5px solid var(--navy);border-radius:999px;padding:.3rem .9rem;background:#edf2f7}
.flow .diamond{border:1.5px solid var(--navy);padding:.45rem;background:#fffaf0;transform:rotate(0deg);max-width:260px;text-align:center}
.flow .arrow{color:var(--navy);font-weight:700}
.cloud-types{display:grid;grid-template-columns:repeat(2,1fr);gap:.5rem;margin:.6rem 0}
.cloud-types .ct{
  border:1.5px solid var(--navy2);padding:.55rem;text-align:center;font-family:"Segoe UI",sans-serif;font-size:.85rem;
}
.note-limited{background:#fff5f5;border-left:3px solid #c53030;padding:.5rem .7rem;margin:.5rem 0;font-size:.92em}
@media screen and (max-width:860px){
  .a4{width:100%;min-height:auto;padding:1rem}
  .meta-grid{grid-template-columns:1fr}
}
@media print{
  body{background:#fff}
  .toolbar{display:none!important}
  .site{max-width:none;margin:0;padding:0}
  .a4{
    box-shadow:none;margin:0;width:auto;min-height:auto;
    padding:12mm 14mm;page-break-after:always;
  }
  .q-block,.diagram,table.cmp,.remember,.source{break-inside:avoid}
  a{color:inherit;text-decoration:none}
}
@page{size:A4;margin:10mm}
"""

JS = r"""
(function(){
  const qBlocks=[...document.querySelectorAll('.q-block')];
  let idx=0;
  function go(i){
    if(!qBlocks.length)return;
    idx=(i+qBlocks.length)%qBlocks.length;
    qBlocks[idx].scrollIntoView({behavior:'smooth',block:'start'});
  }
  const prev=document.getElementById('btnPrev');
  const next=document.getElementById('btnNext');
  if(prev)prev.onclick=()=>go(idx-1);
  if(next)next.onclick=()=>go(idx+1);
  document.getElementById('btnPrint').onclick=()=>window.print();
  document.getElementById('btnDl').onclick=async()=>{
    try{
      const res=await fetch(location.href.split('#')[0]);
      const blob=await res.blob();
      const a=document.createElement('a');
      a.href=URL.createObjectURL(blob);
      a.download='Cloud_Computing_Exam_QA.html';
      a.click();
      URL.revokeObjectURL(a.href);
    }catch(e){alert('Open this file from disk, or use Print → Save as PDF.');}
  };
  const search=document.getElementById('searchBox');
  search.addEventListener('input',()=>{
    const term=search.value.trim().toLowerCase();
    document.querySelectorAll('.hl').forEach(n=>{
      const p=n.parentNode; while(n.firstChild)p.insertBefore(n.firstChild,n); p.removeChild(n);
    });
    if(!term){qBlocks.forEach(q=>q.style.outline='');return;}
    let first=null;
    qBlocks.forEach(q=>{
      const t=q.innerText.toLowerCase();
      if(t.includes(term)){
        q.style.outline='2px solid #d69e2e';
        if(!first)first=q;
      } else q.style.outline='';
    });
    if(first)first.scrollIntoView({behavior:'smooth',block:'start'});
  });
})();
"""

def page_open(title, page_no, total="—"):
    return f"""
<article class="a4">
  <div class="page-header">
    <div><strong>Cloud Computing — Exam Preparation Notes</strong>Subject: Cloud Computing | Prepared from Provided Study Material Only</div>
    <div>{title}</div>
  </div>
"""

def page_close(page_no, total):
    return f"""
  <div class="page-footer">
    <span>Prepared from Provided Study Material Only</span>
    <span>Page {page_no} of {total}</span>
  </div>
</article>
"""

def source(text):
    return f'<div class="source"><strong>Source from Provided Material</strong><br>{text}</div>'

def remember(items):
    lis="".join(f"<li>{i}</li>" for i in items)
    return f'<div class="remember"><strong>Important Points to Remember</strong><ul>{lis}</ul></div>'

def q_block(qid, qno, text, marks, body):
    return f"""
<section class="q-block" id="{qid}">
  <div class="q-head">
    <span class="marks">Marks: {marks}</span>
    <div class="qno">{qno}</div>
    <div class="qtext">{text}</div>
  </div>
  <div class="ans-label">Answer</div>
  {body}
</section>
"""

# Build content pages as list of HTML page bodies (without footer numbering yet)
pages = []

# COVER
pages.append("""
<div class="cover">
  <div class="uni">Institute of Advanced Research (IAR University)</div>
  <p style="margin-top:.3rem;color:#718096;font-size:.9rem">The University for Innovation</p>
  <div class="badge">EXAM PREPARATION NOTES</div>
  <h1>CLOUD COMPUTING</h1>
  <h2>Assignment Questions + Important Exam Questions</h2>
  <p style="max-width:460px;margin:1rem auto;font-size:1.05rem">
    Complete 5-mark Questions &amp; Answers prepared strictly from the supplied
    Assignment PDFs, E-Notes (Units 1–3), and screenshots.
  </p>
  <div class="meta-grid" style="text-align:left;max-width:480px;margin:1.5rem auto">
    <div>Student Name: <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></div>
    <div>Enrollment No.: <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></div>
    <div>Semester: <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></div>
    <div>Subject Code: <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></div>
    <div>Date: <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></div>
    <div>Marks per Q: <span>5</span></div>
  </div>
  <p style="margin-top:2rem;font-size:.95rem;color:#4a5568">
    Materials used: Assignment 1, 2 &amp; 3 · Unit-1 Introduction · SaaS Notes · IaaS/PaaS Notes
  </p>
</div>
""")

# TOC page
toc = """
<div id="toc"></div>
<h2 style="color:var(--navy);text-align:center;margin-top:0">Table of Contents</h2>
<div class="toc">
<h3 class="sec">Assignment 1</h3>
<ol>
<li><a href="#a1q1">Explain Challenges and Applications of Cloud Computing</a> — <span class="marks">5 Marks</span></li>
<li><a href="#a1q2">Define Cloud Computing and state its desirable features</a> — <span class="marks">5 Marks</span></li>
<li><a href="#a1q3">Explain various layers of Cloud Computing</a> — <span class="marks">5 Marks</span></li>
<li><a href="#a1q4">Write and explain various types of deployment models</a> — <span class="marks">5 Marks</span></li>
<li><a href="#a1q5">What is virtualization? Advantages in cloud computing</a> — <span class="marks">5 Marks</span></li>
<li><a href="#a1q6">Explain types of virtualization in brief</a> — <span class="marks">5 Marks</span></li>
</ol>
<h3 class="sec">Assignment 2</h3>
<ol>
<li><a href="#a2q1">Explain SaaS with an example</a> — <span class="marks">5 Marks</span></li>
<li><a href="#a2q2">What are challenges faced by SaaS? Explain in detail</a> — <span class="marks">5 Marks</span></li>
<li><a href="#a2q3">Justify the statement, “SaaS integration is hard”</a> — <span class="marks">5 Marks</span></li>
<li><a href="#a2q4">Explain SaaS integration services</a> — <span class="marks">5 Marks</span></li>
<li><a href="#a2q5">Explain SaaS Integration of Products and Platforms</a> — <span class="marks">5 Marks</span></li>
</ol>
<h3 class="sec">Assignment 3</h3>
<ol>
<li><a href="#a3q1">Explain IaaS in brief</a> — <span class="marks">5 Marks</span></li>
<li><a href="#a3q2">Discuss Virtual Provisioning in Virtualized Data Centre</a> — <span class="marks">5 Marks</span></li>
<li><a href="#a3q3">Explain Virtual Machine Migration Services</a> — <span class="marks">5 Marks</span></li>
<li><a href="#a3q4">Discuss Integration of Public and Private Cloud</a> — <span class="marks">5 Marks</span></li>
<li><a href="#a3q5">Explain any three Tools and Technology used in Cloud Computing</a> — <span class="marks">5 Marks</span></li>
</ol>
<h3 class="sec">Additional Important Exam Questions</h3>
<ol>
<li><a href="#addq1">Differentiate Public Cloud and Private Cloud</a></li>
<li><a href="#addq2">Explain Hybrid Cloud with advantages and disadvantages</a></li>
<li><a href="#addq3">Explain Community Cloud</a></li>
<li><a href="#addq4">Differentiate IaaS, PaaS and SaaS</a></li>
<li><a href="#addq5">Explain Platform as a Service (PaaS)</a></li>
<li><a href="#addq6">Explain Pre-Copy and Post-Copy Migration</a></li>
<li><a href="#addq7">Explain Resource Provisioning and its methods</a></li>
<li><a href="#addq8">Write a short note on Cloud Infrastructure</a></li>
<li><a href="#addq9">Explain Characteristics of SaaS</a></li>
<li><a href="#addq10">Explain Utility Computing and Grid Computing</a></li>
</ol>
<p><a href="#revision">Quick Revision — Definitions</a> · <a href="#diagrams">Important Diagrams</a></p>
</div>
"""
pages.append(toc)

# ========== ASSIGNMENT 1 ==========
a1q1 = q_block("a1q1","Q.1 — Assignment 1","Explain Challenges and Applications of Cloud Computing.",5,f"""
<p>Cloud Computing is defined as storing and accessing data and computing services over the Internet. It is the on-demand availability of computer services like servers, networking, databases, data storage, etc. The main goal of cloud computing is to give data centers access to many users for accessing data from remote servers.</p>

<h3 class="sec">Challenges of Cloud Computing</h3>
<p>From the study notes and challenge diagram, important challenges include:</p>
<ol>
<li><span class="pt">Internet Connectivity:</span> Cloud services depend on the Internet. Poor or unavailable connectivity affects performance and access.</li>
<li><span class="pt">Vendor lock-in:</span> Users may become dependent on a particular Cloud Service Provider and find it difficult to move services or data to another provider.</li>
<li><span class="pt">Limited Control:</span> Because infrastructure is managed by the provider, users may have limited control over underlying resources.</li>
<li><span class="pt">Security:</span> Storing and accessing data through cloud infrastructure creates security concerns. The challenges diagram also highlights Security &amp; Privacy.</li>
<li><span class="pt">Other challenges shown in the notes diagram:</span> Interoperability, Portability, Computing Performance, and Reliability &amp; Availability.</li>
<li><span class="pt">Public-cloud related issues:</span> Performance depends on a high-speed Internet link to the provider, and the client may have no/limited control of data.</li>
</ol>

<div class="diagram">
  <img src="assets/diagrams/challenges.png" alt="Cloud Computing Challenges Diagram">
  <div class="cap"><strong>Diagram Source:</strong> Unit-1 E-Notes — Page 21 (Challenges)</div>
</div>

<h3 class="sec">Applications of Cloud Computing</h3>
<p>According to the applications diagram in Unit-1 notes, cloud computing is applied in:</p>
<ol>
<li>Art</li>
<li>Business</li>
<li>Data Storage and Backup</li>
<li>Education</li>
<li>Entertainment</li>
<li>Management</li>
<li>Social</li>
</ol>
<p>From the handwritten assignment notes (supported by Unit-1 service-model content), practical application areas also include:</p>
<ul>
<li><strong>Data Storage:</strong> Users store data on remote servers and access it through the Internet.</li>
<li><strong>Data Backup &amp; Recovery:</strong> Backup and restore are listed as advantages; storage virtualization is mainly done for backup and recovery.</li>
<li><strong>Software Access (SaaS):</strong> Users access hosted applications via a browser (e.g., Google Apps, Salesforce, Dropbox, Slack).</li>
<li><strong>Application Development &amp; Testing (PaaS):</strong> Programmers develop, test, run and manage applications on a cloud platform.</li>
</ul>

<div class="diagram">
  <img src="assets/diagrams/applications.png" alt="Cloud Computing Applications">
  <div class="cap"><strong>Diagram Source:</strong> Unit-1 E-Notes — Page 22 (Cloud Computing Application)</div>
</div>

{remember([
'Cloud computing = storing/accessing data & services over the Internet.',
'Major challenges: connectivity, vendor lock-in, limited control, security, interoperability, portability, performance, reliability.',
'Applications include storage/backup, business, education, entertainment, social, SaaS access, and PaaS development.'
])}
{source('Unit-1 E-Notes — Pages 3–5, 9, 21–22, 28, 31–32; Assignment1_CC handwritten notes — Pages 1–2; WhatsApp Assignment-1 screenshot')}
""")

a1q2 = q_block("a1q2","Q.2 — Assignment 1","Define cloud computing and state its desirable features.",5,f"""
<p><strong>Definition:</strong> Cloud Computing is defined as storing and accessing data and computing services over the Internet. It is the on-demand availability of computer services like servers, networking, databases, data storage, etc. The main goal of cloud computing is to give data centers access to many users for accessing data from remote servers.</p>

<h3 class="sec">Desirable Features / Advantages</h3>
<p>The Unit-1 study notes list the following desirable features (advantages) of cloud computing:</p>
<ol>
<li><span class="pt">Back-up and restore data:</span> Cloud facilities help protect important files and restore them when required.</li>
<li><span class="pt">Improved collaboration:</span> Multiple users can access shared cloud resources and work together.</li>
<li><span class="pt">Excellent accessibility:</span> Services can be accessed over the Internet from remote locations.</li>
<li><span class="pt">Low maintenance cost:</span> Especially in public cloud, the CSP maintains the infrastructure.</li>
<li><span class="pt">Mobility:</span> Users are not restricted to a particular physical location.</li>
<li><span class="pt">Unlimited storage capacity:</span> The cloud provides large / virtually limitless storage space.</li>
<li><span class="pt">Data security:</span> Protective measures such as authentication, access control and backup support secure access.</li>
</ol>
<p>Additional desirable points from the assignment notes and IaaS characteristics include <strong>on-demand availability</strong> and the <strong>pay-per-use / pay-as-you-go</strong> model, where users pay according to resources consumed and avoid heavy initial hardware investment.</p>

{remember([
'Definition focuses on Internet-based storage and on-demand computing services.',
'Goal: remote access to data-center resources for many users.',
'Key features: backup/restore, collaboration, accessibility, low maintenance, mobility, storage, security, on-demand & pay-per-use.'
])}
{source('Unit-1 E-Notes — Pages 3–4; Unit-3 IaaS/PaaS Notes — Pages 2–3; Assignment1_CC handwritten notes — Pages 2–4')}
""")

pages.append(a1q1)
pages.append(a1q2)

a1q3 = q_block("a1q3","Q.3 — Assignment 1","Explain various layers of Cloud Computing.",5,f"""
<p>Cloud computing is commonly explained using three major service layers (service models). Unit-3 notes state that IaaS forms the foundational layer of cloud computing alongside PaaS and SaaS.</p>

<div class="svc-stack">
  <div class="layer saas">SaaS — Software as a Service (Top Layer)</div>
  <div class="layer paas">PaaS — Platform as a Service (Middle Layer)</div>
  <div class="layer iaas">IaaS — Infrastructure as a Service (Foundational Layer)</div>
</div>
<div class="diagram"><div class="cap"><strong>Diagram Source:</strong> Recreated from Unit-1 E-Notes Pages 29–32 &amp; Unit-3 Page 2 (service layers)</div></div>

<h3 class="sec">1. Infrastructure as a Service (IaaS)</h3>
<p>IaaS is also known as Hardware as a Service (HaaS). It is a computing infrastructure managed over the Internet. The main advantage is that users avoid the cost and complexity of purchasing and managing physical servers.</p>
<p><strong>Characteristics:</strong> Resources available as a service; highly scalable; dynamic and flexible; GUI and API-based access; automated administrative tasks.</p>
<p><strong>Examples:</strong> DigitalOcean, Linode, Amazon Web Services (AWS), Microsoft Azure, Google Compute Engine (GCE), Rackspace, Cisco Metacloud.</p>

<h3 class="sec">2. Platform as a Service (PaaS)</h3>
<p>PaaS is created for the programmer to develop, test, run, and manage applications. It builds on virtualization technology so resources can be scaled up or down as needed, and provides auto-scale ability.</p>
<p><strong>Characteristics:</strong> Accessible to various users via the same development application; integrates with web services and databases; supports multiple languages and frameworks.</p>
<p><strong>Examples:</strong> AWS Elastic Beanstalk, Windows Azure, Heroku, Force.com, Google App Engine, Apache Stratos, Magento Commerce Cloud, OpenShift.</p>

<h3 class="sec">3. Software as a Service (SaaS)</h3>
<p>SaaS is also known as “on-demand software.” Applications are hosted by a cloud service provider. Users access them with an Internet connection and web browser.</p>
<p><strong>Characteristics:</strong> Managed from a central location; hosted on a remote server; accessible over the Internet; users are not responsible for hardware/software updates (applied automatically); purchased on pay-as-per-use basis.</p>
<p><strong>Examples:</strong> BigCommerce, Google Apps, Salesforce, Dropbox, ZenDesk, Cisco WebEx, Slack, GoToMeeting.</p>

{remember([
'Three layers/models: IaaS, PaaS, SaaS.',
'IaaS = foundational virtualized infrastructure (HaaS).',
'PaaS = development/testing platform; SaaS = on-demand hosted applications.'
])}
{source('Unit-1 E-Notes — Pages 29–32; Unit-3 IaaS/PaaS Notes — Page 2; Assignment1_CC handwritten notes — Pages 4–6')}
""")

a1q4 = q_block("a1q4","Q.4 — Assignment 1","Write and explain various types of deployment models of Cloud Computing.",5,f"""
<p>Cloud deployment models define how cloud services are made available. Unit-1 notes describe four types of cloud:</p>

<div class="diagram">
  <img src="assets/diagrams/types-of-cloud.png" alt="Types of Cloud">
  <div class="cap"><strong>Diagram Source:</strong> Unit-1 E-Notes — Page 6 (Types of Cloud)</div>
</div>

<h3 class="sec">1. Public Cloud</h3>
<p>Public cloud is open to all to store and access information via the Internet using the pay-per-usage method. Computing resources are managed and operated by the Cloud Service Provider (CSP).</p>
<p><strong>Advantages:</strong> Lower cost; maintained by CSP; easier to integrate / flexible; location independent; highly scalable; accessible by the general public with no limit on number of users.</p>
<p><strong>Disadvantages:</strong> Less secure because resources are shared publicly; performance depends on high-speed Internet; client has no control of data.</p>
<p><strong>Examples:</strong> Amazon EC2, IBM SmartCloud Enterprise, Microsoft, Google App Engine, Windows Azure Services Platform.</p>

<h3 class="sec">2. Private Cloud</h3>
<p>Also known as an internal cloud or corporate cloud. Organizations build and manage their own data centers internally or by a third party. It can be deployed using open-source tools such as OpenStack and Eucalyptus.</p>
<p><strong>Advantages:</strong> High security and privacy; better performance; quick on-demand IT resource delivery; full organizational control.</p>
<p><strong>Disadvantages:</strong> Skilled people required; limited area of operations; not suitable without prebuilt infrastructure / sufficient manpower.</p>

<h3 class="sec">3. Hybrid Cloud</h3>
<p>Hybrid Cloud = Public Cloud + Private Cloud. It is partially secure: public services can be accessed by anyone, while private-cloud services are accessed only by the organization’s users.</p>
<p><strong>Advantages:</strong> More security than public cloud; faster delivery of products/services; reduces risk; flexible (public) + secure (private) resources.</p>
<p><strong>Disadvantages:</strong> Security not as good as private cloud; complex management; reliability depends on CSPs.</p>
<p><strong>Examples:</strong> Google Application Suite, Office 365, Amazon Web Services.</p>

<h3 class="sec">4. Community Cloud</h3>
<p>Allows systems and services to be accessible by a group of several organizations to share information within a specific community. Owned, managed and operated by one or more organizations, a third party, or a combination.</p>
<p><strong>Example:</strong> Health Care community cloud.</p>
<p><strong>Advantages:</strong> Cost-effective sharing; collaborative with better security than public cloud.</p>
<p><strong>Disadvantages:</strong> Not suitable for every organization; security not as good as private cloud; fixed storage/bandwidth shared among members.</p>

{remember([
'Four models: Public, Private, Hybrid, Community.',
'Public = CSP-managed, pay-per-use; Private = internal/corporate.',
'Hybrid = Public + Private; Community = shared by related organizations.'
])}
{source('Unit-1 E-Notes — Pages 6–18; Assignment1_CC handwritten notes — Pages 6–7; WhatsApp Assignment-1 screenshot')}
""")

pages.append(a1q3)
pages.append(a1q4)

a1q5 = q_block("a1q5","Q.5 — Assignment 1","What is virtualization? What is the advantage of Virtualization in cloud computing?",5,f"""
<p><strong>Definition:</strong> Virtualization is the “creation of a virtual (rather than actual) version of something, such as a server, a desktop, a storage device, an operating system or network resources.”</p>
<p>In other words, Virtualization is a technique which allows sharing a single physical instance of a resource or an application among multiple customers and organizations. It does this by assigning a logical name to a physical storage and providing a pointer to that physical resource when demanded.</p>

<h3 class="sec">Advantages of Virtualization in Cloud Computing</h3>
<p>From Unit-3 notes on cloud technologies:</p>
<ol>
<li><span class="pt">Hardware flexibility:</span> Virtualization offers unparalleled hardware flexibility.</li>
<li><span class="pt">Lower IT cost:</span> It significantly brings down IT maintenance and infrastructure costs.</li>
<li><span class="pt">Efficient multi-user distribution:</span> Cloud providers can bring multiple operating systems and computer systems under one virtual machine to efficiently distribute an application among multiple users within one organization or numerous organizations in a cost-efficient and convenient manner.</li>
</ol>
<p>Additional advantages reflected in the assignment notes (aligned with Unit-1 usage points):</p>
<ol>
<li><span class="pt">Efficient resource utilization:</span> Maximizes hardware usage by running multiple virtual machines.</li>
<li><span class="pt">Cost reduction:</span> Reduces need for multiple physical servers.</li>
<li><span class="pt">Scalability:</span> Resources can be scaled up or down easily.</li>
<li><span class="pt">Flexibility:</span> Supports different OS and apps on the same hardware.</li>
<li><span class="pt">Simplified management:</span> Controlling VMs is much easier than controlling a physical server (also stated under Hardware Virtualization usage).</li>
<li><span class="pt">Backup &amp; Recovery:</span> Storage virtualization is mainly done for backup and recovery purposes.</li>
</ol>

{remember([
'Virtualization = virtual version of server/desktop/storage/OS/network.',
'Shares one physical resource among many users via logical naming/pointers.',
'Key benefits: flexibility, lower cost, efficient utilization, easier VM management, backup/recovery.'
])}
{source('Unit-1 E-Notes — Pages 23, 25, 28; Unit-3 IaaS/PaaS Notes — Pages 25; Assignment1_CC handwritten notes — Pages 7–8')}
""")

a1q6 = q_block("a1q6","Q.6 — Assignment 1","Explain types of virtualization in brief.",5,f"""
<p>According to Unit-1 study notes, the types of virtualization are:</p>
<ol>
<li>Hardware Virtualization</li>
<li>Operating System Virtualization</li>
<li>Server Virtualization</li>
<li>Storage Virtualization</li>
</ol>

<h3 class="sec">1. Hardware Virtualization</h3>
<p>When the virtual machine software or Virtual Machine Manager (VMM) is directly installed on the hardware system, it is known as hardware virtualization. The main job of the hypervisor is to control and monitor the processor, memory and other hardware resources. After hardware virtualization, different operating systems can be installed and different applications can run on those OS.</p>
<p><strong>Usage:</strong> Mainly done for server platforms, because controlling virtual machines is much easier than controlling a physical server.</p>

<h3 class="sec">2. Operating System Virtualization</h3>
<p>When the VMM is installed on the Host operating system instead of directly on the hardware system, it is known as operating system virtualization.</p>
<p><strong>Usage:</strong> Mainly used for testing applications on different platforms of OS.</p>

<h3 class="sec">3. Server Virtualization</h3>
<p>When the VMM is directly installed on the Server system, it is known as server virtualization.</p>
<p><strong>Usage:</strong> A single physical server can be divided into multiple servers on demand and for balancing the load.</p>

<h3 class="sec">4. Storage Virtualization</h3>
<p>Storage virtualization is the process of grouping the physical storage from multiple network storage devices so that it looks like a single storage device. It is also implemented by using software applications.</p>
<p><strong>Usage:</strong> Mainly done for backup and recovery purposes.</p>

{remember([
'Four types: Hardware, OS, Server, Storage virtualization.',
'Hardware: VMM on hardware; OS: VMM on host OS; Server: split one physical server; Storage: pool devices as one.'
])}
{source('Unit-1 E-Notes — Pages 24–28; Assignment1_CC handwritten notes — Page 8')}
""")

pages.append(a1q5)
pages.append(a1q6)

# ========== ASSIGNMENT 2 ==========
a2q1 = q_block("a2q1","Q.1 — Assignment 2","Explain SaaS with an example.",5,f"""
<p><strong>Introduction:</strong> Software as a Service (SaaS) is a software distribution model in which applications are hosted by a service provider and are accessible via the Internet using a browser. It removes the need for installation, maintenance, or infrastructure management by the end user.</p>
<p>In Unit-1 notes, SaaS is also called “on-demand software.” Applications are hosted by a CSP; users access them with an Internet connection and web browser. Updates are applied automatically and services are purchased on a pay-as-per-use basis.</p>

<h3 class="sec">Key Points</h3>
<ol>
<li>Managed from a central location / hosted on a remote server</li>
<li>Accessible over the Internet</li>
<li>Users are not responsible for hardware and software updates</li>
<li>Multi-tenancy related delivery (from SaaS notes characteristics)</li>
</ol>

<h3 class="sec">Example</h3>
<p><strong>Google Workspace:</strong> Users can access Gmail, Docs, Sheets and Drive directly online without installing software locally. Other popular examples from the notes include Microsoft 365, Salesforce, Dropbox, Slack, Zoom, BigCommerce, ZenDesk, Cisco WebEx and GoToMeeting.</p>

{remember([
'SaaS = hosted applications accessed via browser (on-demand software).',
'No local installation/maintenance/infrastructure management by user.',
'Example: Google Workspace / Microsoft 365 / Salesforce.'
])}
{source('SaaS E-Notes — Pages 1–2, 3; Unit-1 E-Notes — Page 32; Assignment2_CC handwritten notes — Page 1; WhatsApp Assignment-2 screenshot')}
""")

a2q2 = q_block("a2q2","Q.2 — Assignment 2","What are challenges faced by SaaS? Explain in detail.",5,f"""
<p>Although SaaS provides flexible and scalable software delivery, the SaaS study notes describe several important challenges:</p>

<ol>
<li><span class="pt">Data Security &amp; Privacy:</span> SaaS applications store data on third-party servers. Risks include data breaches, unauthorized access, and data loss or leaks. Robust encryption, access control, and compliance with regulations (e.g., GDPR, HIPAA) are needed.</li>
<li><span class="pt">Internet Dependency:</span> SaaS requires a stable Internet connection. Downtime or latency affects user experience and business continuity. It is not ideal in regions with poor connectivity.</li>
<li><span class="pt">Limited Customization:</span> Products are standardized for multi-tenancy. UI customization, feature modification and workflow adjustments are limited; custom features may need costly enterprise plans.</li>
<li><span class="pt">Integration Complexity:</span> Businesses use multiple SaaS and on-premise tools. Integration with legacy systems can be technically complex, time-consuming and prone to data sync issues; APIs or platforms like MuleSoft/Zapier may be required.</li>
<li><span class="pt">Vendor Lock-in:</span> Migrating from one SaaS provider to another can be technically difficult, expensive and risky for data loss. Customers become dependent on a vendor’s ecosystem, pricing and uptime.</li>
<li><span class="pt">Performance and Reliability:</span> Shared infrastructure may cause performance degradation during peak hours, latency, or service interruptions. Organizations rely on SLAs for uptime guarantees.</li>
<li><span class="pt">Compliance and Legal Risks:</span> Providers may store data across borders, creating risks related to data residency laws, cross-border regulations, and audit/compliance requirements.</li>
<li><span class="pt">Frequent Updates and Changes:</span> Automatic updates may break integrations or custom workflows, introduce untested features, or require quick staff retraining.</li>
</ol>

{remember([
'Eight major SaaS challenges appear in the notes: security, Internet dependency, customization, integration, lock-in, performance, compliance, frequent updates.',
'Multi-tenancy improves efficiency but limits customization and can affect shared performance.'
])}
{source('SaaS E-Notes — Pages 10–16; Assignment2_CC handwritten notes — Pages 1–2')}
""")

pages.append(a2q1)
pages.append(a2q2)

a2q3 = q_block("a2q3","Q.3 — Assignment 2","Justify the statement, “SaaS integration is hard”.",5,f"""
<p>The statement “SaaS integration is hard” is justified by several points from the SaaS study notes on integration challenges and related SaaS challenges:</p>

<ol>
<li><span class="pt">Different API standards and limitations:</span> Applications may use different standards such as REST and SOAP, with version mismatches and API depreciation issues.</li>
<li><span class="pt">Real-time syncing issues:</span> Keeping data consistent across multiple apps in real time is difficult.</li>
<li><span class="pt">Error handling and logging complexity:</span> Debugging and logging across platforms is challenging.</li>
<li><span class="pt">Legacy / multi-tool environment:</span> Businesses use multiple SaaS and on-premise tools that do not automatically communicate; integrating with legacy systems can be technically complex and time-consuming.</li>
<li><span class="pt">Frequent updates:</span> SaaS providers push automatic updates that may break integrations or custom workflows.</li>
<li><span class="pt">Need for specialized solutions:</span> Integration often requires API knowledge or middleware/iPaaS platforms (e.g., MuleSoft, Zapier, Dell Boomi), which adds cost and technical expertise requirements.</li>
</ol>
<p><strong>Conclusion:</strong> Because of API differences, sync problems, error-handling complexity, legacy constraints and frequent vendor changes, SaaS integration is complex and time-consuming—hence the statement is justified.</p>

{remember([
'Hard because of APIs, real-time sync, error handling, legacy systems, and frequent SaaS updates.',
'Often needs middleware or iPaaS, which itself adds complexity.'
])}
{source('SaaS E-Notes — Pages 12, 16, 17, 21; Assignment2_CC handwritten notes — Page 2')}
""")

a2q4 = q_block("a2q4","Q.4 — Assignment 2","Explain SaaS integration services.",5,f"""
<p><strong>Why needed:</strong> Most businesses use multiple SaaS tools (CRM, ERP, HRM, etc.). These tools do not automatically communicate with each other. Integration services ensure consistent data flow, automated business processes, and elimination of data silos.</p>

<h3 class="sec">Types of SaaS Integration Services</h3>
<ol>
<li><span class="pt">APIs (Application Programming Interfaces):</span> Allow applications to send/receive data from one another. REST and SOAP are common API standards. Most modern SaaS platforms offer open or partner APIs.</li>
<li><span class="pt">Middleware / Integration Platforms:</span> Act as connectors between multiple SaaS apps. Examples: Zapier (no-code automation), MuleSoft (enterprise-grade), Dell Boomi, Workato, Informatica, Jitterbit.</li>
<li><span class="pt">iPaaS (Integration Platform as a Service):</span> Cloud-based integration services that connect SaaS, on-premise and cloud apps; orchestrate complex workflows; and ensure real-time or scheduled syncing. Suitable for enterprise-level needs.</li>
</ol>

<h3 class="sec">Benefits</h3>
<ul>
<li>Centralized view of data across tools</li>
<li>Improved workflow efficiency</li>
<li>Reduced manual effort and human error</li>
<li>Enables analytics/reporting by aggregating data sources</li>
<li>Scalability as businesses add more applications</li>
</ul>

{remember([
'Integration services connect multiple SaaS tools that otherwise stay in silos.',
'Main approaches: APIs, Middleware, iPaaS.',
'Benefits: centralized data, automation, fewer errors, better analytics.'
])}
{source('SaaS E-Notes — Pages 17–20; Assignment2_CC handwritten notes — Page 2')}
""")

a2q5 = q_block("a2q5","Q.5 — Assignment 2","Explain SaaS Integration of Products and Platforms.",5,f"""
<h3 class="sec">A. SaaS Integration with Products</h3>
<p>Different product categories integrate with related business systems as shown in the notes:</p>
<table class="cmp">
<thead><tr><th>Product Type</th><th>SaaS Example</th><th>Integrated With</th></tr></thead>
<tbody>
<tr><td>CRM</td><td>Salesforce</td><td>Marketing tools, ERP, email</td></tr>
<tr><td>ERP</td><td>SAP, NetSuite</td><td>HRM, finance, logistics</td></tr>
<tr><td>HRM</td><td>Workday, BambooHR</td><td>Payroll, ERP, recruitment tools</td></tr>
<tr><td>Marketing</td><td>HubSpot, Marketo</td><td>CRM, analytics, email systems</td></tr>
<tr><td>E-Commerce</td><td>Shopify, WooCommerce</td><td>Inventory, shipping, analytics</td></tr>
</tbody>
</table>
<p><strong>Benefits of Product Integration:</strong> Centralized data consistency; improved customer experience; streamlined sales, HR, finance and marketing operations; real-time business intelligence.</p>
<p><strong>Example workflow from notes:</strong> A lead is captured in HubSpot → synced to Salesforce CRM → creates a contact in Workday HRM (for recruitment) → automatically generates a report in Power BI.</p>

<h3 class="sec">B. SaaS Integration with Platforms</h3>
<table class="cmp">
<thead><tr><th>Platform</th><th>Role</th></tr></thead>
<tbody>
<tr><td>AWS</td><td>Cloud hosting, serverless compute, AI</td></tr>
<tr><td>Microsoft Azure</td><td>Enterprise cloud services, Active Directory</td></tr>
<tr><td>Google Cloud</td><td>Big data tools, APIs, ML/AI</td></tr>
<tr><td>Heroku</td><td>PaaS for deploying SaaS apps</td></tr>
</tbody>
</table>
<p><strong>Integration use cases:</strong> Hosting SaaS products on AWS EC2 or Lambda; using Google Cloud APIs (e.g., Translation, ML); Azure Active Directory for SaaS identity management; CI/CD integration with GitHub, Jenkins, DockerHub.</p>

{remember([
'Product integration links CRM/ERP/HRM/Marketing/E-commerce tools.',
'Platform integration uses AWS, Azure, Google Cloud, Heroku.',
'Goal: consistent data, automation, hosting, identity and CI/CD.'
])}
{source('SaaS E-Notes — Pages 22–24; Assignment2_CC handwritten notes — Pages 3–4')}
""")

pages.append(a2q3)
pages.append(a2q4)
pages.append(a2q5)

# ========== ASSIGNMENT 3 ==========
a3q1 = q_block("a3q1","Q.1 — Assignment 3","Explain IaaS in brief.",5,f"""
<p><strong>Definition:</strong> Infrastructure as a Service (IaaS) is a cloud computing delivery model that provides virtualized computing resources over the Internet. Instead of purchasing and maintaining physical servers, storage and networking equipment, users rent these resources on-demand from cloud service providers.</p>
<p>IaaS forms the foundational layer of cloud computing (alongside PaaS and SaaS) and offers flexibility, scalability and cost-effectiveness. In Unit-1 notes, IaaS is also known as Hardware as a Service (HaaS). The main advantage is that it helps users avoid the cost and complexity of purchasing and managing physical servers.</p>

<h3 class="sec">Key Characteristics</h3>
<ol>
<li><span class="pt">On-demand self-service:</span> Users provision resources as needed without human intervention from the provider.</li>
<li><span class="pt">Scalability:</span> Capacity can be increased or decreased dynamically.</li>
<li><span class="pt">Pay-as-you-go pricing:</span> Customers pay only for resources they consume.</li>
<li><span class="pt">Virtualization:</span> Resources are abstracted and delivered via virtual machines, containers and software-defined networks.</li>
<li>Also listed in Unit-1: resources as a service; dynamic and flexible; GUI and API-based access; automated administrative tasks.</li>
</ol>

<p><strong>Examples:</strong> DigitalOcean, Linode, Amazon Web Services (AWS)/EC2, Microsoft Azure, Google Compute Engine (GCE), Rackspace, Cisco Metacloud.</p>

{remember([
'IaaS = rent virtualized infrastructure over Internet (also called HaaS).',
'Foundational cloud layer with on-demand, scalable, pay-as-you-go resources.',
'Examples: AWS, Azure, GCE, Rackspace.'
])}
{source('Unit-3 IaaS/PaaS Notes — Pages 1–3; Unit-1 E-Notes — Page 30; Assignment_16190 Assignment 3 question paper; CC_Assign3 handwritten notes — Page 1')}
""")

a3q2 = q_block("a3q2","Q.2 — Assignment 3","Discuss Virtual Provisioning in Virtualized Data Centre.",5,f"""
<p><strong>Meaning:</strong> Virtual Provisioning (VMP) is the capability to present a LUN to a computer system with extra capacity than what is physically allotted to the LUN on the storage array. Physical storage is allotted only when compute needs it, and provisioning decisions are not bound by presently accessible storage. Physical storage is allotted from a shared pool of physical capacity to the application “on-demand.” This gives more efficient storage utilization by minimizing allotted but unused physical storage.</p>
<p>It can be implemented at the <strong>Computer layer</strong> and the <strong>Storage layer</strong>.</p>
<p>Virtual provisioning is also described as a virtual storage network (VSAN)-based technology in which storage space is allocated on demand to devices. This allows virtualized environments to control allocation and management of physical disk storage connected with virtual machines (VMs). Virtual Machine Management Service (VMMS / vmms.exe) is the main module in Microsoft Windows that controls aspects of Hyper-V server virtualization.</p>

<h3 class="sec">Need for Virtual Provisioning</h3>
<ol>
<li>Administrators typically allot storage based on anticipated growth to minimize later management overhead and application downtime.</li>
<li>This causes over-provisioning, leading to greater costs, more power/cooling/floor-space needs, and lower capacity utilization.</li>
<li>Virtual Provisioning addresses these challenges by more efficient utilization of storage.</li>
</ol>

<h3 class="sec">Advantages</h3>
<ul>
<li>Minimizes the operating and storage cost</li>
<li>Decreases downtime</li>
<li>Improves capacity utilization</li>
<li>Minimizes administrative overhead</li>
</ul>

{remember([
'Virtual provisioning = on-demand allocation from a shared storage pool (thin/over-presented LUN capacity).',
'Avoids over-provisioning cost, power, cooling and space waste.',
'Advantages: lower cost, less downtime, better utilization, less admin overhead.'
])}
{source('Unit-3 IaaS/PaaS Notes — Pages 7–10; Assignment_16190 Assignment 3')}
""")

pages.append(a3q1)
pages.append(a3q2)

a3q3 = q_block("a3q3","Q.3 — Assignment 3","Explain Virtual Machine Migration Services.",5,f"""
<p><strong>Definition:</strong> Virtual machine migration is the task of moving a virtual machine from one physical hardware environment to another.</p>

<h3 class="sec">Types of VM Migration</h3>
<table class="cmp">
<thead><tr><th>VM Migration Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Cold Migration</td><td>Before migration, the virtual machine must be powered off. After the task, the old one should be deleted from the source host. The VM need not be on shared storage.</td></tr>
<tr><td>Warm Migration</td><td>Whenever transferring OS and any application, there is no need to suspend the source host. It has high demand in public cloud.</td></tr>
<tr><td>Live Migration</td><td>Process of moving a running virtual machine without stopping the OS and other applications from source host to destination host.</td></tr>
</tbody>
</table>

<h3 class="sec">Migration Techniques</h3>
<p>Two important techniques are <strong>Pre-Copy Migration</strong> and <strong>Post-Copy Migration</strong>.</p>
<p><strong>Pre-Copy:</strong> Hypervisor copies all memory pages from source to destination while the VM is running. It has Warm-up Phase and Stop-and-Copy Phase. Dirty pages are recopied in warm-up; finally CPUs are suspended during downtime for remaining transfer.</p>
<p><strong>Post-Copy:</strong> VM at source is suspended first; CPU state/registers/non-pageable memory are transferred; remaining pages are sent (pre-paging). Page faults (network faults) at target are redirected to source.</p>

<div class="diagram">
  <img src="assets/diagrams/pre-copy.png" alt="Pre-Copy Migration Technique">
  <div class="cap"><strong>Diagram Source:</strong> Unit-3 IaaS/PaaS Notes — Page 16 (Pre-Copy Migration Technique)</div>
</div>
<div class="diagram">
  <img src="assets/diagrams/post-copy.png" alt="Post-Copy Migration Technique">
  <div class="cap"><strong>Diagram Source:</strong> Unit-3 IaaS/PaaS Notes — Page 19 (Post-Copy Migration Technique)</div>
</div>

{remember([
'VM migration moves a VM between physical hosts.',
'Cold / Warm / Live migration types.',
'Techniques: Pre-copy (copy while running, then stop-and-copy) and Post-copy (suspend first, then transfer pages).'
])}
{source('Unit-3 IaaS/PaaS Notes — Pages 11–19; Assignment_16190 Assignment 3; CC_Assign3 handwritten notes — Page 2')}
""")

a3q4 = q_block("a3q4","Q.4 — Assignment 3","Discuss Integration of Public and Private Cloud.",5,f"""
<p>Integrating public and private clouds creates a <strong>hybrid cloud</strong>.</p>
<ul>
<li><strong>Private cloud:</strong> Provides control, security, and customization for sensitive data and applications.</li>
<li><strong>Public cloud:</strong> Offers scalability, elasticity, and access to on-demand resources for flexible workloads.</li>
</ul>

<h3 class="sec">Steps of Integration</h3>
<ol>
<li><span class="pt">Identify Workloads and Data:</span> Decide suitability for public or private cloud based on regulatory, security or performance considerations.</li>
<li><span class="pt">Choose Integration Models:</span> e.g., Cloud Bursting — dynamically scale workloads from private to public cloud during peak demand.</li>
<li><span class="pt">Implement Hybrid Cloud Management Platform (CMP):</span> Orchestrate and manage workloads across clouds from a unified interface. Examples: VMware Cloud Foundation, Red Hat OpenShift, Microsoft Azure Arc.</li>
<li><span class="pt">Optimize Workload Placement:</span> Policies based on performance, cost, data sensitivity and compliance.</li>
<li><span class="pt">Ensure Security and Compliance:</span> Consistent security policies, controls and encryption.</li>
<li><span class="pt">Disaster Recovery and Business Continuity:</span> DR/BC strategy spanning both environments.</li>
<li><span class="pt">Training and Documentation:</span> Train IT staff and users for hybrid operations.</li>
</ol>

<h3 class="sec">Challenges</h3>
<ul>
<li><strong>Complexity:</strong> Managing two separate environments adds complexity.</li>
<li><strong>Security Considerations:</strong> Data transfer needs robust security for privacy and compliance.</li>
<li><strong>Vendor Lock-in:</strong> Integration across providers can be challenging.</li>
</ul>

{remember([
'Public + Private integration = Hybrid cloud.',
'Key model: Cloud Bursting for peak demand.',
'Needs CMP, security consistency, DR/BC, and staff training.'
])}
{source('Unit-3 IaaS/PaaS Notes — Pages 20–24; Unit-1 E-Notes — Pages 13–15; Assignment_16190 Assignment 3')}
""")

a3q5 = q_block("a3q5","Q.5 — Assignment 3","Explain any three Tools and Technology used in Cloud Computing.",5,f"""
<p>Unit-3 notes list important technologies and tools for cloud computing. Any three are explained below.</p>

<h3 class="sec">1. Virtualization</h3>
<p>Virtualization technology uses specialized programming techniques to create a virtual version of a computer resource. This allows cloud service providers to bring multiple operating systems and computer systems under one virtual machine to efficiently distribute an application among multiple users within one organization or numerous organizations in a cost-efficient and convenient manner. It offers unparalleled hardware flexibility and significantly brings down IT maintenance and infrastructure costs. It is the first entry on the cloud computing technologies list in the notes.</p>

<h3 class="sec">2. Service-Oriented Architecture (SOA)</h3>
<p>SOA refers to an online architecture that supports a collection of services. There is an established communication protocol between components of various applications or services, and this communication occurs over a network to provide the user with certain services.</p>

<h3 class="sec">3. Grid Computing</h3>
<p>Grid computing allows multiple computer resources to combine and interact to achieve a common objective. It is particularly beneficial when large-scale computing tasks are too burdensome for one individual computing resource. Such a job is broken into smaller components and distributed among the grid. The computing resources communicate and work together to solve the problem.</p>

<p><em>Additional technology from the same notes (for revision):</em> <strong>Utility Computing</strong> — a software service provision business model with pay-per-use; users subscribe and pay only for preferred services without massive initial expenditure.</p>

{remember([
'Three core technologies in notes: Virtualization, SOA, Grid Computing (also Utility Computing).',
'Virtualization enables multi-OS sharing and lower infrastructure cost.',
'Grid splits large jobs across many resources.'
])}
{source('Unit-3 IaaS/PaaS Notes — Pages 25–28; Assignment_16190 Assignment 3')}
""")

pages.append(a3q3)
pages.append(a3q4)
pages.append(a3q5)

# ========== ADDITIONAL QUESTIONS ==========
pages.append("""
<h2 style="color:var(--navy);text-align:center;border-bottom:2px solid var(--navy);padding-bottom:.4rem">Additional Important Exam Questions</h2>
<p style="text-align:center;color:#4a5568;font-family:'Segoe UI',sans-serif;font-size:.9rem">Prepared only from Unit-1, SaaS, and IaaS/PaaS E-Notes</p>
""")

addq1 = q_block("addq1","Additional Q.1","Differentiate between Public Cloud and Private Cloud.",5,f"""
<table class="cmp">
<thead><tr><th>Basis</th><th>Public Cloud</th><th>Private Cloud</th></tr></thead>
<tbody>
<tr><td>Meaning</td><td>Open to all via Internet using pay-per-usage; managed by CSP</td><td>Internal/corporate cloud built and managed by organization or third party</td></tr>
<tr><td>Access</td><td>General public; no limit on number of users</td><td>Accessible within the organization; limited area of operations</td></tr>
<tr><td>Security</td><td>Less secure; resources shared publicly</td><td>High level of security and privacy</td></tr>
<tr><td>Control</td><td>Client has no control of data</td><td>Organization has full control</td></tr>
<tr><td>Cost / Maintenance</td><td>Lower cost; CSP maintains</td><td>Needs skilled people and infrastructure</td></tr>
<tr><td>Examples / Tools</td><td>Amazon EC2, Google App Engine, Windows Azure</td><td>OpenStack, Eucalyptus</td></tr>
</tbody>
</table>
{source('Unit-1 E-Notes — Pages 7–12')}
""")

addq2 = q_block("addq2","Additional Q.2","Explain Hybrid Cloud with its advantages and disadvantages.",5,f"""
<p>Hybrid Cloud is a combination of the public cloud and the private cloud: <strong>Hybrid Cloud = Public Cloud + Private Cloud</strong>. It is partially secure because public-cloud services can be accessed by anyone, while private-cloud services can be accessed only by the organization’s users.</p>
<p><strong>Examples:</strong> Google Application Suite (Gmail, Google Apps, Google Drive), Office 365, Amazon Web Services.</p>
<h3 class="sec">Advantages</h3>
<ol>
<li>Suitable for organizations needing more security than public cloud</li>
<li>Helps deliver new products and services more quickly</li>
<li>Excellent way to reduce risk</li>
<li>Flexible resources (public) + secure resources (private)</li>
</ol>
<h3 class="sec">Disadvantages</h3>
<ol>
<li>Security not as good as private cloud</li>
<li>Managing hybrid cloud is complex</li>
<li>Reliability depends on cloud service providers</li>
</ol>
{source('Unit-1 E-Notes — Pages 13–15')}
""")

addq3 = q_block("addq3","Additional Q.3","Explain Community Cloud.",5,f"""
<p>Community cloud allows systems and services to be accessible by a group of several organizations to share information between the organization and a specific community. It is owned, managed and operated by one or more organizations in the community, a third party, or a combination of them.</p>
<p><strong>Example:</strong> Health Care community cloud.</p>
<p><strong>Advantages:</strong> Cost-effective sharing; collaborative with more security than public cloud; distributive environment; share resources/infrastructure/capabilities.</p>
<p><strong>Disadvantages:</strong> Not good for every organization; security not as good as private cloud; not suitable without collaboration; fixed storage and bandwidth shared among members.</p>
{source('Unit-1 E-Notes — Pages 16–18')}
""")

addq4 = q_block("addq4","Additional Q.4","Differentiate between IaaS, PaaS and SaaS.",5,f"""
<table class="cmp">
<thead><tr><th>Basis</th><th>IaaS</th><th>PaaS</th><th>SaaS</th></tr></thead>
<tbody>
<tr><td>Meaning</td><td>Hardware/Infrastructure as a Service over Internet</td><td>Platform for develop, test, run, manage apps</td><td>On-demand software hosted by CSP</td></tr>
<tr><td>User focus</td><td>Rent VMs, storage, networking</td><td>Programmers/developers</td><td>End users via browser</td></tr>
<tr><td>Management</td><td>Avoid buying/managing physical servers</td><td>Provider manages platform/runtime; builds on virtualization</td><td>Provider manages app, updates automatically</td></tr>
<tr><td>Key traits</td><td>Scalable, dynamic, GUI/API access</td><td>Multi-language, auto-scale, web/DB integration</td><td>Central management, pay-as-per-use</td></tr>
<tr><td>Examples</td><td>AWS, Azure, GCE, Rackspace</td><td>Heroku, Google App Engine, OpenShift</td><td>Salesforce, Google Apps, Dropbox, Slack</td></tr>
</tbody>
</table>
{source('Unit-1 E-Notes — Pages 30–32; Unit-3 Notes — Pages 1–3')}
""")

pages.append(addq1)
pages.append(addq2)
pages.append(addq3)
pages.append(addq4)

addq5 = q_block("addq5","Additional Q.5","Explain Platform as a Service (PaaS).",5,f"""
<p>PaaS cloud computing platform is created for the programmer to develop, test, run, and manage the applications. It builds on virtualization technology so resources can easily be scaled up or down as per the organization’s need, and provides an ability to “Auto-scale.”</p>
<h3 class="sec">Characteristics</h3>
<ol>
<li>Accessible to various users via the same development application</li>
<li>Integrates with web services and databases</li>
<li>Builds on virtualization technology</li>
<li>Supports multiple languages and frameworks</li>
<li>Provides auto-scale ability</li>
</ol>
<p><strong>Examples:</strong> AWS Elastic Beanstalk, Windows Azure, Heroku, Force.com, Google App Engine, Apache Stratos, Magento Commerce Cloud, OpenShift.</p>
{source('Unit-1 E-Notes — Page 31')}
""")

addq6 = q_block("addq6","Additional Q.6","Explain Pre-Copy Migration and Post-Copy Migration.",5,f"""
<h3 class="sec">Pre-Copy Migration</h3>
<p>The hypervisor copies all memory pages from source to destination while the VM is running. Phases:</p>
<ol>
<li><strong>Warm-up Phase:</strong> While copying, some pages change (dirty pages) because source CPU is active; dirty pages must be recopied.</li>
<li><strong>Stop &amp; Copy Phase:</strong> Warm-up repeats until dirty pages are recopied; source CPU is deactivated; both CPUs suspended during downtime while remaining pages transfer.</li>
</ol>
<div class="diagram">
  <img src="assets/diagrams/pre-copy.png" alt="Pre-Copy">
  <div class="cap"><strong>Diagram Source:</strong> Unit-3 Notes — Page 16</div>
</div>

<h3 class="sec">Post-Copy Migration</h3>
<p>VM at source is suspended to start post-copy migration. Execution state (CPU state, registers, non-pageable memory) is transferred to the target. Remaining memory pages are sent in parallel (pre-paging). If the target accesses a not-yet-transferred page, a page/network fault occurs and is redirected to the source. Pre-paging pushes pages after the last fault to reduce faults.</p>
<div class="diagram">
  <img src="assets/diagrams/post-copy.png" alt="Post-Copy">
  <div class="cap"><strong>Diagram Source:</strong> Unit-3 Notes — Page 19</div>
</div>
{source('Unit-3 IaaS/PaaS Notes — Pages 12–19')}
""")

addq7 = q_block("addq7","Additional Q.7","Explain Resource Provisioning and its methods.",5,f"""
<p><strong>Resource Provisioning</strong> means the selection, deployment, and run-time management of software (e.g., database server management systems, load balancers) and hardware resources (e.g., CPU, storage, and network) for ensuring guaranteed performance for applications.</p>
<h3 class="sec">Methods</h3>
<ol>
<li><span class="pt">Static Provisioning:</span> Predictable and unchanging demands; advance preparation of resources; charges as flat fee or monthly basis.</li>
<li><span class="pt">Dynamic Provisioning:</span> Demand may change or vary; allocate more resources when needed and remove when not in use.</li>
<li><span class="pt">User-Self Provisioning:</span> Resources are purchased from the web; create user account.</li>
</ol>
{source('Unit-3 IaaS/PaaS Notes — Pages 29–30')}
""")

addq8 = q_block("addq8","Additional Q.8","Write a short note on Cloud Infrastructure and its management.",5,f"""
<p><strong>Cloud infrastructure</strong> consists of all hardware and software elements needed for cloud computing, including: Compute (server), Networking, Storage, and Virtualization resources.</p>
<p><strong>Cloud infrastructure management</strong> comprises the processes and tools needed to effectively allocate and deliver key resources when and where they are required. The UI/dashboard is a control panel for provisioning, configuring and managing cloud infrastructure.</p>
<p>It is useful in delivering cloud services to:</p>
<ul>
<li>Internal users (developers or other roles that consume cloud resources)</li>
<li>External users (customers and business partners)</li>
</ul>
{source('Unit-1 E-Notes — Pages 19–20')}
""")

pages.append(addq5)
pages.append(addq6)
pages.append(addq7)
pages.append(addq8)

addq9 = q_block("addq9","Additional Q.9","Explain the Characteristics of SaaS.",5,f"""
<p>From the SaaS E-Notes, important characteristics are:</p>
<ol>
<li><span class="pt">Multi-tenancy model:</span> Single instance serves multiple users.</li>
<li><span class="pt">Scalable usage</span> based on subscription model.</li>
<li><span class="pt">Automatic updates</span> and patch management.</li>
<li><span class="pt">Accessible from anywhere</span> with Internet connectivity.</li>
<li><span class="pt">Security, compliance, and SLAs.</span></li>
</ol>
<p>Unit-1 also lists: managed from a central location; hosted on a remote server; accessible over the Internet; users not responsible for hardware/software updates; pay-as-per-use purchase.</p>
{source('SaaS E-Notes — Page 3; Unit-1 E-Notes — Page 32')}
""")

addq10 = q_block("addq10","Additional Q.10","Explain Utility Computing and Grid Computing as cloud technologies.",5,f"""
<h3 class="sec">Grid Computing</h3>
<p>Grid computing allows multiple computer resources to combine and interact to achieve a common objective. It is beneficial for large-scale tasks too burdensome for one resource. The job is broken into smaller components and distributed among the grid; resources communicate and work together to solve the problem.</p>
<h3 class="sec">Utility Computing</h3>
<p>Utility computing is an enabling technology for cloud computing. It is a software service provision business model that employs a pay-per-use model. Users subscribe to preferred services and pay only for those services without a massive initial expenditure. This offers flexibility to change or discontinue usage of a cloud service.</p>
{source('Unit-3 IaaS/PaaS Notes — Pages 27–28')}
""")

pages.append(addq9)
pages.append(addq10)

# Quick revision + diagrams summary
revision = f"""
<section id="revision">
<h2 style="color:var(--navy);text-align:center">Quick Revision — Important Definitions</h2>
<ol>
<li><strong>Cloud Computing:</strong> Storing and accessing data and computing services over the Internet; on-demand servers, networking, databases, storage. <em>(Unit-1 p.3)</em></li>
<li><strong>Distributed Computing (pre-requisite):</strong> Multiple software components on multiple computers running as a single system. <em>(Unit-1 p.2)</em></li>
<li><strong>Virtualization:</strong> Creation of a virtual version of a server, desktop, storage, OS or network resource; share one physical instance among many. <em>(Unit-1 p.23)</em></li>
<li><strong>Public / Private / Hybrid / Community Cloud:</strong> Four deployment models. <em>(Unit-1 p.6–18)</em></li>
<li><strong>IaaS / PaaS / SaaS:</strong> Three service layers/models. <em>(Unit-1 p.29–32)</em></li>
<li><strong>SaaS:</strong> Software distribution model; apps hosted by provider; browser access. <em>(SaaS notes p.2)</em></li>
<li><strong>Virtual Provisioning:</strong> Present LUN with more capacity than physically allotted; allocate from shared pool on demand. <em>(Unit-3 p.7)</em></li>
<li><strong>VM Migration:</strong> Moving a VM from one physical hardware environment to another. <em>(Unit-3 p.11)</em></li>
<li><strong>Resource Provisioning:</strong> Selection, deployment and run-time management of software/hardware for guaranteed performance. <em>(Unit-3 p.29)</em></li>
<li><strong>iPaaS:</strong> Cloud-based integration for connecting SaaS/on-premise/cloud apps and orchestrating workflows. <em>(SaaS notes p.19)</em></li>
</ol>
{source('Compiled from Unit-1, SaaS, and Unit-3 E-Notes as cited above')}
</section>
"""
pages.append(revision)

diagrams = """
<section id="diagrams">
<h2 style="color:var(--navy);text-align:center">Important Diagrams (from Study Material)</h2>
<div class="diagram">
  <img src="assets/diagrams/types-of-cloud.png" alt="Types of Cloud">
  <div class="cap"><strong>Diagram Source:</strong> Unit-1 E-Notes — Page 6</div>
</div>
<div class="diagram">
  <img src="assets/diagrams/challenges.png" alt="Challenges">
  <div class="cap"><strong>Diagram Source:</strong> Unit-1 E-Notes — Page 21</div>
</div>
<div class="diagram">
  <img src="assets/diagrams/applications.png" alt="Applications">
  <div class="cap"><strong>Diagram Source:</strong> Unit-1 E-Notes — Page 22</div>
</div>
<div class="diagram">
  <img src="assets/diagrams/pre-copy.png" alt="Pre-Copy">
  <div class="cap"><strong>Diagram Source:</strong> Unit-3 Notes — Page 16</div>
</div>
<div class="diagram">
  <img src="assets/diagrams/post-copy.png" alt="Post-Copy">
  <div class="cap"><strong>Diagram Source:</strong> Unit-3 Notes — Page 19</div>
</div>
</section>
"""
pages.append(diagrams)

# Assemble with page numbers
TOTAL = len(pages)
parts = []
for i, body in enumerate(pages, 1):
    title_map = {
        1: "Cover Page",
        2: "Table of Contents",
    }
    title = title_map.get(i, f"Study Notes · Sheet {i}")
    parts.append(page_open(title, i, TOTAL) + body + page_close(i, TOTAL))

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cloud Computing — Exam Preparation Q&amp;A (A4)</title>
<style>{CSS}</style>
</head>
<body>
<nav class="toolbar" aria-label="Study navigation">
  <a href="#top">Home</a>
  <a href="#a1q1">Assignment Qs</a>
  <a href="#addq1">Additional Qs</a>
  <a href="#toc">TOC</a>
  <button type="button" id="btnPrev">Previous</button>
  <button type="button" id="btnNext">Next</button>
  <button type="button" id="btnPrint">Print / Save as PDF</button>
  <button type="button" id="btnDl">Download HTML</button>
  <div class="search-wrap">
    <label for="searchBox" style="font-size:.8rem">Search</label>
    <input type="search" id="searchBox" placeholder="Question, keyword, topic...">
  </div>
</nav>
<main class="site" id="top">
{''.join(parts)}
</main>
<script>{JS}</script>
</body>
</html>
"""

OUT.write_text(html, encoding="utf-8")
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes), pages={TOTAL}")
