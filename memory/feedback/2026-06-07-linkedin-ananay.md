# Feedback — 2026-06-07 — LinkedIn DM from @ananay

## Source

LinkedIn DM (off-platform, but verified the LinkedIn profile matches the GitHub org owner of `openhackai/openhack` — every commit on the repo is authored by `ananay` / `Ananay Arora`).

## Handle / context

- **GitHub handle:** `@ananay` (the real one)
- **Reserved handle:** `@ananayarora` — just a username reservation, not active
- **LinkedIn:** "Ananay Arora — Building OpenHack"
- **Relationship to tool:** solo maintainer / creator of `openhackai/openhack`

## What changed

- Maintainer surfaced. `openhackai/openhack` is not a dead repo with a stolen name — there's a real person behind it who is reading the curation output.
- The maintainer read `memory/rejected/2026-06-06.md`, saw their tool listed with score 56 and reason "too new", and interpreted "rejected" as a hard pass. They reached out to ask how to "fix" it.
- This is a **directory-naming bug** (the entry was in `roundup/` semantics, not `rejected/` semantics) — the tool was never actually rejected. A clarification was sent and accepted; maintainer reacted with 👍 "Perfect".

## Action

- [x] Maintainer identity confirmed (`@ananay` owns every commit on `openhackai/openhack`)
- [x] Directory-split PR opened in `awesome-niche-tools` to clarify the naming (`memory/rejected/` → `memory/roundup/` for borderline, `memory/rejected/` reserved for true rejects)
- [x] `memory/feedback/` convention introduced so future maintainer DMs land in a queryable, agent-readable log
- [ ] **Next shift:** re-score `openhackai/openhack` with attribution credit (`maintainer_signal = HIGH` because they responded within 38 minutes). Re-evaluate the "too new" 14-day half-life penalty — if the repo has crossed 100★ or 1+ stars/day, bump into the curated set under `categories/ai-agents/`.

## Status

`resolved` (clarification sent, maintainer satisfied with the explanation; re-score queued for next shift)

## Conversation excerpt

> **Ananay Arora (9:29 PM):** Hi Rajesh! Great work on the memory repo. Saw that OpenHack landed up in the rejected md file due to being too new. Would love to know how we can fix that!
>
> **Rajesh Kalidandi (9:59 PM):** Hey Ananay — quick clarification: OpenHack wasn't actually rejected. It scored 56 in the curation pass, which puts it in our "logged for weekly roundup" bucket. The directory name is on us — `memory/rejected/` holds both roundup logs and true rejects, which is confusing. The "too new" reason was the agent being conservative on a 2-week-old project. We're happy to bump it to the main list on the next curation run — what would help is any signal on stars/usage since 2026-05-23 and your GitHub handle (looks like `ananayarora`?) so the re-score has attribution. Solid work on the subcommand CLI + checkpoint system, by the way.
>
> **Ananay Arora (10:07 PM):** Thanks for the clarification. Github handle is `@ananay`. `@ananayarora` is just to reserve the username haha
