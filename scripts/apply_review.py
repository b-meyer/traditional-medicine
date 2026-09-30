"""Apply the review ledger to work/<system>/final.yml.

Usage: python scripts/apply_review.py   (run from repo root)

Reads   work/review-ledger.yml
Writes  work/<system>/final.yml   (original kept as final.pre-review.yml)

Never changes a leaf's `status` or the pipeline's `verify_outcome`. Adds a
`review` list to every leaf a ledger entry touches, and makes the small value
edits listed in EDITS below. Anything else stays as the pipeline left it.
"""
import copy, os, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from tradmed_lib import load, dump, get_path, set_path, leaves

DATE = "2026-09-30"

def direct(url, title):
    return {"source": title, "url": url, "type": "institutional", "citation_strength": "direct"}

def find(lst, key, val):
    for x in lst:
        if isinstance(x, dict) and x.get(key) == val:
            return x
    raise KeyError(f"{key}={val!r} not found")

def sub(text, old, new):
    assert old in text, f"expected text not found: {old[:60]!r}"
    return text.replace(old, new, 1)

def edit_unani(f):
    pe = get_path(f, "identification.practitioner_estimate")
    for e in pe["value"]:
        if e.get("region") == "India":
            e["superseded_by_review"] = True
    pe["value"].append({
        "region": "India", "count": 50053, "year": 2022, "as_on": "2022-01-01",
        "source": "Lok Sabha USQ 1240 (9 Feb 2024) and USQ 1858 (2 Aug 2024), Annexure I, from State/UT Boards/Councils",
        "concentration": "UP 15,730; Maharashtra 7,882; Bihar 5,423; West Bengal 5,325; Telangana 5,187 (79% of total)"})
    pe["citations"] = (pe.get("citations") or []) + [
        direct("https://eparlib.nic.in/bitstream/123456789/2974061/1/AU1240.pdf", "Lok Sabha Unstarred Question 1240, 9 Feb 2024"),
        direct("https://eparlib.nic.in/bitstream/123456789/2979017/1/AU1858_XBNSfn.pdf", "Lok Sabha Unstarred Question 1858, 2 Aug 2024")]
    dp = get_path(f, "education_and_licensure.degree_programs")
    dp["value"] = sub(dp["value"],
        "55 Unani colleges (of 733 AYUSH institutes: 414 Ayurveda, 248 Homeopathy, 55 Unani, 13 Siddha, 3 Sowa Rigpa)",
        "57 Unani colleges as on 01.04.2022 (of 847 AYUSH colleges; Lok Sabha USQ 1858, 2 Aug 2024; an older undated snapshot gave 55 of 733)")
    dp["citations"] = (dp.get("citations") or []) + [
        direct("https://eparlib.nic.in/bitstream/123456789/2979017/1/AU1858_XBNSfn.pdf", "Lok Sabha Unstarred Question 1858, 2 Aug 2024, Annexure II")]
    j = get_path(f, "legal_status.jurisdictions")
    pk = find(j["value"], "jurisdiction", "Pakistan")
    pk["integration_with_public_health_system"] = (pk.get("integration_with_public_health_system") or "") + \
        ". Status at Feb 2026: merger with the homoeopathy council still pending as a draft NTCAM Act 2025; colleges told not to admit new students (Dawn, 16 Feb 2026)."
    sa = find(j["value"], "jurisdiction", "South Africa")
    sa["year_note"] = "Allied Health Professions Act is 1982; the 2001 date could not be sourced. Registration route: 3-year basic medical sciences plus 2-year Unani-Tibb specialisation (UWC)."
    j["citations"] = (j.get("citations") or []) + [
        direct("http://nasirlawsite.com/laws/uahpa.htm", "Unani, Ayurvedic and Homoeopathic Practitioners Act 1965 (Act No. II of 1965)"),
        direct("https://ahpcsa.co.za/faqs/", "AHPCSA FAQ: Unani-Tibb under Act 63 of 1982"),
        direct("https://www.dawn.com/news/1967850/uncertainty-clouds-future-of-tibb-colleges-and-hakeems-in-pakistan", "Dawn, 16 Feb 2026 (news, current status)")]
    de = get_path(f, "revival_and_institutionalization.dated_events")
    for ev in de["value"]:
        if ev.get("label", "").startswith("Ajmal Khan as President"):
            ev["label"] = "Ajmal Khan presides over the Indian National Congress (acting president for C. R. Das)"
            ev["description"] = "Ahmedabad session, December 1921."
        if ev.get("label") == "Tibbia College foundation stone":
            ev["date"] = "1916-03-29"
        if ev.get("label", "").startswith("Inauguration of Ayurvedic and Unani Tibbia"):
            ev["date"] = "1921-02-13"
    de["citations"] = (de.get("citations") or []) + [
        direct("https://autch.delhi.gov.in/autch/about-us", "Ayurvedic and Unani Tibbia College and Hospital, About Us"),
        direct("https://inc.in/leadership/past-party-presidents/hakim-ajmal-khan-acting-president-for-c-r-das", "Indian National Congress: Hakim Ajmal Khan (Acting President)")]
    rel = get_path(f, "diagnostics.reliability_evidence")
    rel["review_flag"] = ("Mojahedi 2014 weighted kappa range: the abstract says 0.40-0.82 (PMC4005447); the verify pass changed it to 0.83. "
                          "Revert to 0.82 unless the full-text results table shows 0.83.")

def edit_tcm(f):
    j = get_path(f, "legal_status.jurisdictions")
    au = find(j["value"], "jurisdiction", "Australia")
    au["year"] = "2010 (National Law in force); 2012 (Chinese medicine joined the scheme, 1 July)"
    au["scope_of_practice"] = (au.get("scope_of_practice") or "") + \
        ". Before 2012 only Victoria regulated Chinese medicine. Registered: 3,804 (2012), 4,795 (March 2022)."
    my = find(j["value"], "jurisdiction", "Malaysia")
    my["regulator"] = "Traditional and Complementary Medicine Council (T&CM Council), Ministry of Health"
    my["year_note"] = "Act 775 gazetted 10 Mar 2016, partly in force 1 Aug 2016; practitioner registration opened 15 Mar 2021."
    prc = find(j["value"], "jurisdiction", "People's Republic of China")
    prc["statute"] = "Law on Traditional Chinese Medicine, adopted 25 Dec 2016 by the NPC Standing Committee, effective 1 July 2017 (63 articles)"
    j["citations"] = (j.get("citations") or []) + [
        direct("https://en.nhc.gov.cn/2016-12/26/c_70933.htm", "National Health Commission: TCM law passed 25 Dec, effective 1 July"),
        direct("https://chinesemedicineboard.gov.au/registration", "Chinese Medicine Board of Australia: registration from 1 July 2012"),
        direct("https://hq.moh.gov.my/tcm/en/index.php/faqregistration", "Malaysia MOH T&CM Division FAQ")]
    sm = get_path(f, "disruption.suppression_or_marginalization")
    sm["value"] = [
        ("Marginalized further in the Republican era. A 1929 proposal to abolish 'old medicine' was rescinded that December; "
         "it was not enacted (earlier text said 'outlawed under the 1929 proposals', which overstates it)") if "1929" in str(x) else x
        for x in sm["value"]]
    sm["citations"] = (sm.get("citations") or []) + [
        direct("https://en.apu.ac.jp/rcaps/uploads/fckeditor/publications/journal/RJAPS_V27_Fan.pdf", "Fan, Ritsumeikan J. Asia Pacific Studies 27: abolition proposal rescinded Dec 1929")]
    ab = get_path(f, "disruption.abolition_attempts")
    ab["value"] = ("1929: Yu Yunxiu (Yu Yan) proposed at the Nanjing government's National Public Health Conference (Feb 1929) to abolish 'old medicine'; "
                   "practitioners protested in Shanghai on 17 March 1929; the Nanjing government rescinded the proposal in December 1929 under Chiang Kai-shek's order.")
    ab["status"] = ab.get("status")  # unchanged
    ab["citations"] = (ab.get("citations") or []) + [
        direct("https://en.apu.ac.jp/rcaps/uploads/fckeditor/publications/journal/RJAPS_V27_Fan.pdf", "Fan, Ritsumeikan J. Asia Pacific Studies 27"),
        direct("https://gera.fr/wp-content/uploads/2026/04/nguyen-100231.pdf", "Nguyen 2026: the 1929 episode is often misread as an effective ban")]
    de = get_path(f, "disruption.dated_events")
    if not any("rescind" in str(e.get("label", "")).lower() for e in de["value"]):
        de["value"].append({"label": "Abolition proposal rescinded", "date": "1929-12",
                            "description": "Nanjing government rescinded the proposal to abolish Chinese medicine (Chiang Kai-shek's order)."})
    ra = get_path(f, "safety.regulatory_actions_taken")
    ra["value"] = [
        ("Aristolochia: Belgian cluster identified 1992; FDA warnings 2000-2001 plus import alert; Canada removal order 2001 and re-warning 2004; "
         "UK ban 2001; Netherlands prohibition 2001; Hong Kong brand list; China removed Guan mu tong in 2003 (weakly sourced)") if "Aristolochia" in str(x) else x
        for x in ra["value"]]
    ra["citations"] = (ra.get("citations") or []) + [
        direct("https://www.cmaj.ca/content/cmaj/171/5/449.full.pdf", "CMAJ 2004;171(5):449"),
        direct("https://link.springer.com/article/10.1007/s00216-007-1310-3", "Anal Bioanal Chem, aristolochic acid in herbal preparations")]

def edit_ayurveda(f):
    pe = get_path(f, "identification.practitioner_estimate")
    pe["value"].append({
        "region": "India", "count": 346240, "year": 2022, "as_on": "2022-01-01",
        "source": "Lok Sabha USQ 1858 (2 Aug 2024), Annexure I, from State/UT Boards/Councils",
        "colleges": "453 (01.04.2022)", "dispensaries": "25,280 (01.04.2022, incl. central)"})
    pe["notes"] = ((pe.get("notes") or "") + " Review pass added the India figure (same source and date as the Unani count).").strip()
    pe["citations"] = (pe.get("citations") or []) + [
        direct("https://eparlib.nic.in/bitstream/123456789/2979017/1/AU1858_XBNSfn.pdf", "Lok Sabha Unstarred Question 1858, 2 Aug 2024")]
    j = get_path(f, "legal_status.jurisdictions")
    my = find(j["value"], "jurisdiction", "Malaysia")
    my["year_note"] = "Practice area 'Traditional Indian Medicine'; practitioner registration opened 15 Mar 2021."

EDITS = {"unani": edit_unani, "tcm": edit_tcm, "ayurveda": edit_ayurveda}

def leaf_map(doc):
    return dict(leaves(doc["fields"]))

def main():
    ledger = load("work/review-ledger.yml")["entries"]
    patched, sources = {}, {}
    # Patch everything in memory first, so a mismatch in any system writes nothing.
    for system, fn in EDITS.items():
        path = f"work/{system}/final.yml"
        backup = f"work/{system}/final.pre-review.yml"
        src = backup if os.path.exists(backup) else path   # always patch from the untouched original
        sources[system] = (src, path, backup)
        doc = load(src)
        try:
            fn(doc["fields"])
            for e in [x for x in ledger if x["system"] == system]:
                leaf = get_path(doc["fields"], e["path"])
                if leaf is None:
                    raise KeyError(f"ledger path missing: {e['path']}")
                leaf.setdefault("review", []).append(
                    {"id": e["id"], "verdict": e["verdict"], "date": DATE, "sources": e["sources"]})
        except (AssertionError, KeyError) as err:
            sys.exit(f"{system}: {err}\nNothing was written. The repo's final.yml differs from the one "
                     f"this review was made against; send the error back for a re-fit.")
        patched[system] = doc

    # Self-check against the untouched originals before writing anything.
    report = []
    for system, doc in patched.items():
        src = sources[system][0]
        before, after = leaf_map(load(src)), leaf_map(doc)
        if before.keys() != after.keys():
            sys.exit(f"{system}: leaf set changed; aborting, nothing written")
        bad = [q for q in before if before[q].get("status") != after[q].get("status")
               or before[q].get("verify_outcome") != after[q].get("verify_outcome")]
        if bad:
            sys.exit(f"{system}: status/verify_outcome changed on {bad}; aborting, nothing written")
        report.append((system, len(after), sum(1 for q in before if before[q] != after[q])))

    for system, doc in patched.items():
        src, path, backup = sources[system]
        if not os.path.exists(backup):
            shutil.copy(path, backup)
        dump(doc, path)
    for system, n, changed in report:
        print(f"{system}: {n} leaves, {changed} leaves modified, statuses untouched")
    print("Expected: unani 6, tcm 6, ayurveda 5.")

main()
