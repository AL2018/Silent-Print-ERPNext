# AGENTS.md — Silent-Print-ERPNext

Entry file for any AI agent or person working in this repository. It is tool-neutral. `CLAUDE.md` imports it, so
edit this file, not that one.

## What this repository is
Frappe app `silent_print`: prints documents straight to a printer without the browser's print dialog, through
the Webapp Hardware Bridge (a Java program on the computer with the printers). Covers POS printing and printing from
any document by client script. Upstream author Roque Vera (`hooks.py`); the README's install line still points at
`roquegv/Silent-Print-ERPNext`.

**Legacy, lightly maintained.** Uploaded on 5 Feb 2024; one fix since (28 Jul 2026, the uv dependency below). Where
it runs, if anywhere, is not recorded in this repo (unverified).

## Read first
The estate's rules live in `AL2018/littlecocoa-docs`. Read them in this order before working here:
1. `docs/cc-briefs/METHOD-02-how-we-work.md`: how Alan, the architect and the coder work. Always first.
2. `docs/cc-briefs/PRODUCTION-INTEGRITY-RULE.md`: what may touch production, and how.
3. `docs/cc-briefs/ACCEPTANCE-CRITERIA-RULE.md` and `docs/cc-briefs/OPERATING-STANDARDS-v1.0.md`.
4. `docs/cc-briefs/CC_STANDING_RULES_v0.9.md` (v0.9 governs; earlier versions are superseded).
5. `docs/architecture/GOTCHAS.md`: the single register of known traps.
Then this file, then the repo's own docs.

## Rules that bite here
A short digest; the documents above are the source, and this list is a cache.
- Production is changed only through the application or its API, never by direct SQL. Staging first.
- The default branch is protected: feature branch, then PR. Deploys name both the branch and the commit.
- No secrets in the repo. AI never sends a message to anyone outside the team.
- Australian English in copy and comments.
- Never declare `frappe` (or `erpnext`) as a pip dependency. uv cannot resolve it, because frappe's own metadata carries `PyPika @ git+https://...` and uv rejects transitive URL dependencies (fixed in dieline and Silent-Print-ERPNext, 28–29 Jul 2026). Bench provides frappe. `setup.py` sets `install_requires=[]`; `requirements.txt` is kept but no longer read, and must not simply be emptied, as `"".strip().split("\n")` yields `[""]`, an invalid requirement.

## Structure
- `silent_print/silent_print_core/doctype/`: Silent Print Format and Silent Print Settings.
- `silent_print/public/js/silent_print.js`: the browser side that talks to the hardware bridge.
- `silent_print/utils/print_format.py`: renders the print format for sending.
- `README.md` and the two `.png` files: upstream's usage guide.

## Conventions
- Default branch `main`. Install from this repo, not the upstream URL in the README.
- Whether this app is installed on any site is not recorded in this repo (unverified). Any deploy is Alan's, on Frappe Cloud, by branch and SHA, after staging.

## Current state
Not kept here: entry files describe the repo, not the week. See `AL2018/littlecocoa-docs`
`docs/handoffs/STATUS-LEDGER.md` and the workstream folder under `docs/` for this repo.
