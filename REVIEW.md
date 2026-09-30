# Review of work/ (Unani, TCM, Ayurveda) — 30 Sept 2026

## Bottom line

The corpus is structurally ready for synthesis, but the verification behind it is uneven and the word "unverifiable" in `final.yml` is misleading. I checked the highest-value claims against primary sources, found two real errors and one regression, and closed two gaps with a better source than the reports had. Patched files are in this folder; nothing was deleted.

## 1. State of the corpus

| | Unani | TCM | Ayurveda |
|---|---|---|---|
| Leaves (schema 1.6, identical set) | 82 | 82 | 82 |
| filled / partial | 58 / 13 | 57 / 13 | 63 / 9 |
| incidental | 3 | 7 | 3 |
| not_requested | 5 | 4 | 4 |
| absent | 2 | 0 | 2 |
| Leaves from v2 / v1 / gap / verify | 63 / 2 / 2 / 15 | 63 / 5 / 3 / 11 | 45 / 3 / 5 / 29 |
| Verify outcomes: confirmed / corrected / unverifiable | 2 / 13 / 41 | 5 / 6 / 45 | 14 / 15 / 29 |
| Filled leaves still on indirect or uncited sources | 39 | 41 | 31 |

Schema errors 0, rejected fragments 0, same leaf set across all three. The mapping and merge are sound.

**Asymmetry to carry into the synthesis.** Ayurveda has 29 of its ~58 verify targets resolved, Unani 15, TCM 11. TCM is the least verified system, so any comparative claim leaning on a TCM leaf is the most exposed.

**Absent leaves.** Unani: `diagnostics.sign_vs_synthesis`, `disruption.abolition_attempts`. Ayurveda: `disruption.post_colonial_disruption`, `literature_state.publication_bias_findings`. TCM has none. These are real gaps that survived a search pass and belong in the synthesis's "cannot be compared" list.

## 2. What "unverifiable" means here

The pipeline recorded 115 unverifiable outcomes. They are not 115 doubtful claims:

| Class | Count | Example |
|---|---|---|
| Definitional labels | 5 | `identification.system_name` |
| The report's own text, not a claim | 6 | `self_reported_gaps`, `report_conclusions` |
| Emic description of the tradition's theory | 16 | `theoretical_primitives.balance_logic` |
| **Checkable factual claims, still unresolved** | **88** | statutes, dated events, counts, scholar positions |

The first three classes were flagged because "no citation" was treated as a verification target. They cannot be verified externally by design. Only the last 88 matter. Suggested fix: give classes 1–3 a `verify_outcome: not_applicable`, and tell the synthesis agent that unverifiable on the 88 means "unchecked", never "false".

## 3. What I verified (21 ledger entries, ~25 claims)

Full detail and URLs in `work/review-ledger.yml`. Results: 6 confirmed, 8 confirmed with a nuance, 2 corrected, 4 updated with a newer primary source, 1 unresolved.

**Corrections that matter**

1. **TCM, 1929 (T04).** The extraction says Chinese medicine was "outlawed under the 1929 proposals" and records the abolition outcome as unstated. In fact Yu Yan's proposal (Feb 1929) was met by the 17 March Shanghai protest and rescinded in December 1929 on Chiang Kai-shek's order. It was never enacted. A 2026 paper warns this is a common misreading. This matters for the "rupture and survival" chapter, where TCM's abolition attempt sits beside Ayurveda's 1835 and Unani's colonial marginalisation.
2. **TCM, Australia (T02).** The National Law took effect 1 July 2010; Chinese medicine joined on 1 July 2012. The single year "2012" conflated them. Before 2012 only Victoria regulated it.
3. **Unani, Mojahedi kappa range (U09), unresolved and probably a regression.** The paper's abstract says 0.40–0.82. The verify pass "corrected" it to 0.83. I could not read the full text (blocked), so I flagged it rather than changed it. Revert to 0.82 unless the results table says otherwise.

**Better sources than the reports had**

4. **India practitioner counts (U06, A01).** One Lok Sabha answer (USQ 1858, 2 Aug 2024) gives every system on the same basis, as on 01.01.2022: Ayurveda 346,240; homoeopathy 320,873; Unani 50,053; Siddha 9,164; naturopathy 3,933; Sowa-Rigpa 54; total 730,317. That is 47.4% / 43.9% / 6.9% / 1.3% / 0.5%. Five states hold 79% of Unani practitioners. Colleges (01.04.2022): Ayurveda 453, Unani 57. This replaces a 2015 press-relayed Unani figure, and fills the Ayurveda `practitioner_estimate`, which previously had only Sri Lankan numbers. TCM has no equivalent in the corpus.
5. **Pakistan (U02).** The 2024 merger of the Tibb and Homoeopathy councils is still unresolved in Feb 2026, now as a draft NTCAM Act 2025 with colleges told to stop admitting students (Dawn).

**Confirmed against primary or near-primary sources:** Kurande 2013 kappas 0.07 / 0.17 / 0.28 (with the design and the random-rating rejection counts); the 2026 Persian-medicine kappa study (0.512 max, 0.081 min, n=350); PRC TCM Law (25 Dec 2016, in force 1 July 2017, 63 articles); Malaysia Act 775 (gazetted 10 March 2016, registration opened only on 15 March 2021, so it covers TCM and Ayurveda but not Unani); Pakistan's 1965 Act; South Africa's Act 63 of 1982 (the year 2001 is unsourced); Tibbia College dates; WHO Unani benchmarks (11 Feb 2022); Saper 2004 and 2008; the aristolochic acid regulatory chronology; the Denmark ashwagandha ban.

**Weaker confirmations, flagged in the ledger:** Saper and the Denmark ban are confirmed through press releases and trade press, not the JAMA page or the Danish regulator. The Ajmal Khan "President of the Congress" claim is really acting president. DTU's stated concerns did not lead with liver toxicity, contrary to how the Ayurveda v2 report phrases it (the extraction's value does not mention it, and was left unchanged).

**Candidate addition, not applied (T06).** Jagwani et al. 2023 (pulse diagnosis, weighted κ 0.370, matched on 116 of 300). I quoted this earlier in the project from the first TCM v2 run; the clean re-run does not include it. It is real, but it used two Indian TCM practitioners and Cronbach α was 0.963, so it needs its design attached if added.

## 4. What I did not verify

I sampled; I did not clear the 88. Highest-value remainder, in order:

1. TCM `legal_status` beyond PRC, Australia and Malaysia: Hong Kong, Singapore, Ontario, Taiwan, Japan, Korea, Switzerland, Germany. Unani: Bangladesh, Sri Lanka, Iran.
2. `construct_debate.positions` for TCM and Ayurveda (scholar positions; Unani's was already corrected).
3. `contact_and_borrowing.relationships` for all three (Speziale, Mankah al-Hindi, the Yuan-era Muslim medical bureau).
4. Dated events: Ayurveda's 1835 institutional closure, TCM canon dates.
5. Specific unchecked items I saw: Iran's 2007 PhD, Hunayn's 129 titles, the Qanun manuscript dates, India's 2005 heavy-metal export rule, FDA import alerts 66-41 and 99-42, the ephedra ban date.
6. `politicized_episodes` and `integration_disputes` (fast-moving; use court and ministry primaries).
7. `economics` for TCM (market-size figures are likely to stay aggregator-sourced).

## 5. Before running the synthesis

1. Use the patched `final.yml` files (originals kept as `final.pre-review.yml`). Leaves I touched carry a `review` list; no `status` or `verify_outcome` was changed. `abolition_attempts` for TCM is still marked partial although its outcome is now stated.
2. Decide the Mojahedi value (U09).
3. Give the synthesis agent the class rule from section 2 and the verification asymmetry from section 1.
4. If you want the TCM column to carry as much weight as Ayurveda's, run a second verify pass on TCM's checkable leaves first.

## Method and limits

Sources were retrieved through web search and direct fetch. PubMed Central full text was blocked by a reCAPTCHA, so journal claims rest on abstracts. Where I relied on a secondary report, the ledger says so. Colleges' and councils' own websites are treated as authoritative for their own histories and rules, not for anything else.
