# `memory/feedback/` — External Signal Log

Logs signals from **outside the curation pipeline** that should re-trigger a scoring pass or change the priority of an existing entry. A maintainer DM, a GitHub issue, a Hacker News thread where the author participates, a Twitter mention — anything that gives us attribution, credibility data, or a "the maintainer is alive" signal.

## When to write a feedback entry

Write one when:

- A **maintainer of a borderline tool** (score 40-59) reaches out to ask why they weren't curated → log the conversation, capture handle + current metrics, queue for re-score
- A **maintainer of a rejected tool** asks for re-consideration → log, capture the new evidence, re-score from scratch
- A **credible third party** (HN front-page, conference talk, podcast mention) vouches for a tool → log as a corroboration signal
- A **GitHub issue is opened on a curated entry** about a bug, license change, or archival → log so the next shift can decide to de-curate or update

## Naming convention

`YYYY-MM-DD-<source>-<handle-or-alias>.md`

Examples:
- `2026-06-07-linkedin-ananay.md` (a LinkedIn DM from @ananay)
- `2026-06-08-github-issue-lowfat-42.md` (issue #42 on the lowfat repo)
- `2026-06-10-hn-thread-mnemo.md` (Ananay-style HN participation)

## Required sections

Every feedback entry should answer:

1. **Source** — where did the signal come from? (LinkedIn DM, GitHub issue, HN comment, X post, etc.)
2. **Handle / context** — who said it, and what's their relationship to the tool?
3. **What changed** — new evidence that should affect scoring
4. **Action** — what should the next shift do? (re-score, de-curate, attribute, escalate)
5. **Status** — `open` / `resolved` / `no-action`

## How agents should use it

**At the start of every shift**, before scoring:

1. Read all `memory/feedback/*.md` files with `status: open`
2. For each open entry, run a fresh score on the linked tool
3. Update the entry's status once actioned
4. Reference the entry ID in the shift log if it caused a curation or de-curation

This makes the curation engine **bidirectional**: it talks to maintainers, and maintainers can move entries across the 40/60 boundary with one message.
