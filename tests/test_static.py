from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
PUBLIC = [SITE / "index.html", SITE / "business-plan.html", SITE / "noema.html"]

class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.forms=[]; self.text=[]; self.ids=set()
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=="a" and a.get("href"): self.links.append(a["href"])
        if tag=="form": self.forms.append(a)
        if a.get("id"): self.ids.add(a["id"])
    def handle_data(self,data): self.text.append(data)

def fail(msg): raise AssertionError(msg)

def main():
    for p in PUBLIC:
        if not p.exists(): fail(f"missing public page: {p}")
        src=p.read_text(encoding="utf-8")
        parser=AuditParser(); parser.feed(src)
        visible=" ".join(parser.text).lower()
        if "demo" not in visible or "fict" not in visible: fail(f"missing demo disclosure: {p.name}")
        for f in parser.forms:
            if f.get("action") not in (None,"", "#"): fail(f"form endpoint found: {p.name}")
        for href in parser.links:
            if href.startswith(("http://","https://","mailto:","tel:")): continue
            base,_,anchor=href.partition("#")
            target=(p.parent/(base or p.name)).resolve()
            if not target.exists(): fail(f"broken link {href} in {p.name}")
            if anchor:
                q=AuditParser(); q.feed(target.read_text(encoding="utf-8"))
                if anchor not in q.ids: fail(f"broken anchor {href} in {p.name}")
    js=(SITE/"app.js").read_text(encoding="utf-8")
    forbidden=["fetch(","XMLHttpRequest","localStorage","sessionStorage","document.cookie","navigator.sendBeacon","WebSocket("]
    for token in forbidden:
        if token in js: fail(f"forbidden runtime capability: {token}")
    public_text=" ".join(p.read_text(encoding="utf-8").lower() for p in PUBLIC)
    banned=[r"resultados garantizados",r"100% seguro",r"sin riesgos",r"mejor cirujano",r"resultados? perfectos?"]
    for pattern in banned:
        if re.search(pattern,public_text): fail(f"prohibited claim pattern: {pattern}")
    agents=(ROOT/"AGENTS.md").read_text(encoding="utf-8")
    if len(agents.split())>320: fail("AGENTS.md exceeded lightweight entrypoint budget")
    manifest=(ROOT/"noema.project.yaml").read_text(encoding="utf-8")
    if "default_mode: build" not in manifest or "build:" not in manifest: fail("Noema default mode missing")
    print("PASS static quality gate")
    print(f"public_pages={len(PUBLIC)}")
    print(f"agent_entrypoint_words={len(agents.split())}")
    print("network_or_persistence_apis=0")

if __name__=="__main__": main()
