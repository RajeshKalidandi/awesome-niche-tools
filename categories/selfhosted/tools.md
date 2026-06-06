# 🏠 Selfhosted

> Tools you can host yourself — mail gateways, encrypted storage, and privacy-respecting alternatives.

---

## [Posthorn](https://github.com/craigmccaskill/posthorn)

> Self-hosted email gateway between your apps and transactional mail providers. One Docker container, one TOML config.

- **Stars:** 168 (↑~10/day) | **Language:** Go | **License:** Apache-2.0
- **Last commit:** 2026-05-27
- **Source credibility weight:** 0.85 (Hacker News Show HN)
- **Relevance score:** 70/100

### What It Does
Posthorn is a self-hosted email gateway that sits between your applications and transactional mail providers (Postmark, Resend, Mailgun, AWS SES, or outbound SMTP). It's a single Docker container with a TOML config file — no database, no complex setup. Your apps send email to Posthorn, and it routes to the right provider.

### Why Now
Transactional email is a solved problem, but the integration layer between your apps and mail providers is messy. Posthorn simplifies this by providing a single endpoint that handles provider switching, retry logic, and logging. The Show HN launch on Hacker News signals growing interest in self-hosted email infrastructure.

### Why It Matters
Instead of hardcoding mail provider credentials in every app, Posthorn provides a central gateway. Switch providers by editing one TOML file. Get unified logging across all email. Retry failed deliveries automatically. It's the "reverse proxy for email" that every self-hosted setup needs.

### Who Should Care
- Self-hosters who send transactional email
- Developers tired of managing mail provider SDKs in every app
- Teams that want to switch mail providers without code changes
- Anyone running multiple apps that need email

### Execution Pattern
Run Posthorn as a Docker container: `docker run -p 2525:2525 -v ./config.toml:/app/config.toml craigmccaskill/posthorn`. Configure your apps to send email to localhost:2525 instead of directly to your mail provider. The TOML config defines your mail providers, routing rules, and retry policies. Monitor logs via `docker logs` or integrate with your logging stack.

### Skill Potential
Yes — SKILL.md would cover: Docker deployment, TOML configuration, provider setup, monitoring integration, and high-availability patterns.

- **Discovered:** 2026-05-29 via Hacker News (credibility: 0.85)

## [Feloxi](https://github.com/thesaadmirza/feloxi)

> Real-time Celery task queue monitoring — Rust/Axum backend, Next.js dashboard, ClickHouse analytics. Self-hosted monitoring tool with Prometheus endpoints, beat scheduler support, and failure group tracking.

- **Stars:** 29 (↑~5/day) | **Language:** Rust | **License:** Apache-2.0
- **Last commit:** 2026-05-24
- **Source credibility weight:** 0.85 (Lobsters)
- **Relevance score:** 72/100

### What It Does
Feloxi is a self-hosted monitoring tool for Celery task queues. It provides a real-time dashboard showing task status, worker health, queue depths, and processing times. Built with a Rust/Axum backend for performance, a Next.js dashboard for the UI, and ClickHouse for analytics storage. Features include Prometheus metrics endpoint, Celery beat scheduler visibility, failure group tracking, and task inspection with args/kwargs/viewable results.

### Why Now
As more Python applications adopt Celery for background job processing, the need for real-time monitoring grows. Existing tools like Flower are functional but lack modern UIs and deep analytics. Feloxi addresses this with a performance-focused stack (Rust+ClickHouse) and a React-based dashboard. Released in May 2026, it's gaining traction in the self-hosted Python ecosystem.

### Why It Matters
Monitoring background job queues is critical for system reliability — stuck queues, failing workers, or processing delays can cascade into user-impacting issues. Feloxi gives teams visibility into their Celery infrastructure with low overhead. The self-hosted nature means no data leaves your infrastructure, important for teams processing sensitive data in background jobs.

### Who Should Care
- Teams using Celery for background job processing in Python applications
- DevOps engineers responsible for monitoring job queue health
- Anyone needing real-time visibility into task processing times and failure patterns
- Organizations with compliance requirements that prevent using SaaS monitoring tools

### Execution Pattern
Deploy via Docker Compose: run the feloxi service (backend) and optionally the dashboard. Point your Celery app to use Feloxi as a monitor via configuration. Access the dashboard at http://localhost:3000. Configure Prometheus scraping if you want metrics in your existing monitoring stack. The ClickHouse instance stores historical analytics for trend analysis.

### Skill Potential
Yes — SKILL.md would cover: Docker deployment, Celery integration, dashboard usage, Prometheus metric configuration, failure alerting setup, and ClickHouse backup procedures.

- **Discovered:** 2026-05-31 via Lobsters (credibility: 0.85)

---

## [Secluso](https://github.com/secluso/core)

> Private DIY home security camera for Raspberry Pi — end-to-end encrypted, no cloud surveillance.

- **Stars:** 1,505 (↑~376/day) | **Language:** Rust | **License:** GPL-3.0
- **Last commit:** 2026-05-31
- **Source credibility weight:** 0.85 (Hacker News)
- **Relevance score:** 71/100

### What It Does
Secluso is a self-hosted home security camera system built for Raspberry Pi with end-to-end encryption. It provides encrypted remote access to live video, alerts, and recordings from your phone — all without cloud surveillance. Setup takes 5 minutes via Secluso Deploy. Requires a Pi Zero 2W, compatible camera modules, and a relay (your own VPS or free beta hosting).

### Why Now
Home security cameras from Ring, Nest, and Arlo send your video to the cloud — creating privacy risks and ongoing subscription costs. Secluso solves this with a fully self-hosted, E2E encrypted alternative. Created May 29, 2026, it is already at 1,505 stars with 42 forks. The Rust implementation ensures performance and security. The GPL-3.0 license guarantees it stays open.

### Why It Matters
Privacy-focused home security without cloud dependency. Your video never leaves your network (except through E2E encrypted relay). No monthly fees, no data harvesting, no third-party access. For privacy-conscious households, this is the security camera system that Ring should have been.

### Who Should Care
- Privacy-conscious households wanting home security
- Raspberry Pi enthusiasts looking for projects
- Anyone frustrated by cloud-dependent security cameras
- Self-hosters who want encrypted remote access

### Execution Pattern
```bash
# Flash SD card with Secluso image
# Or install on existing Pi
curl -sL https://secluso.com/install | bash

# Configure via web interface
# Access at http://secluso.local

# Connect from phone
# Download Secluso app (iOS/Android)
# Scan QR code to pair
```

### Skill Potential
Yes — SKILL.md should cover: Pi setup, camera module compatibility, relay configuration, phone app pairing, encryption setup, and troubleshooting.

- **Discovered:** 2026-06-01 via Hacker News (credibility: 0.85)


---

## [Odysseus](https://github.com/pewdiepie-archdaemon/odysseus)

> Self-hosted AI workspace — local-first ChatGPT/Claude alternative with agents, deep research, and email triage

- **Stars:** 7877 (↑rapid growth, created 2026-05-31) | **Language:** JavaScript | **License:** MIT
- **Last commit:** 2026-05-31
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 85/100

### What It Does
A full-featured self-hosted AI workspace that replicates the ChatGPT/Claude UI experience on your own hardware. Includes chat with any local model (vLLM, llama.cpp, Ollama), agent mode with tools (MCP, web, files, shell), deep research with multi-step synthesis, model comparison with blind testing, document editing with AI assistance, persistent memory/skills via ChromaDB, IMAP/SMTP email with AI triage, notes/tasks with reminders, and CalDAV calendar sync. Docker compose deployment with PWA mobile support.

### Why Now
Self-hosted AI tooling is maturing rapidly. Odysseus bundles the best patterns (local model serving, agent frameworks, memory systems) into a single polished package. Created 2026-05-31, it represents the current state of the art for self-hosted AI workspaces. The cookbook feature that scans hardware and recommends models is particularly novel.

### Why It Matters
This is the most complete self-hosted AI workspace available. Instead of stitching together Open WebUI + separate agent tools + separate email tools, you get everything in one deployment. For teams running on-prem AI or privacy-conscious users, this eliminates the need for multiple SaaS subscriptions.

### Who Should Care
Privacy-conscious developers, teams running on-prem AI infrastructure, self-hosters building local AI stacks, anyone wanting ChatGPT-like experience without sending data to OpenAI/Anthropic.

### Execution Pattern
Deploy via Docker Compose, point at your existing LLM server (Ollama/vLLM), configure email accounts in Settings. Use the Cookbook to auto-discover and serve optimal models for your hardware. The agent mode integrates with MCP servers for tool use. Memory and skills persist across sessions via ChromaDB.

### Skill Potential
Yes — SKILL.md would cover: Docker deployment, model selection via Cookbook, agent tool configuration, email triage setup, memory/skills persistence.

- **Discovered:** 2026-06-01 via GitHub Trending (credibility: 1.00)


---

## [OpenLogi](https://github.com/AprilNEA/OpenLogi)

> Native, local-first alternative to Logitech Options+ written in Rust — remap buttons, DPI, SmartShift over HID++

- **Stars:** 1688 (↑growing) | **Language:** Rust | **License:** GPL-3.0
- **Last commit:** 2026-05-28
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 78/100

### What It Does
A native, local-first replacement for Logitech Options+ written in Rust. Remap mouse buttons, adjust DPI settings, and configure SmartShift (free-spin/tilt wheel) via HID++ protocol directly. No account required, no telemetry, no cloud dependency. Supports multiple Logitech devices through the HID++ protocol.

### Why Now
Logitech Options+ has become increasingly bloated with mandatory accounts, cloud sync, and telemetry. The privacy-conscious community has been demanding a local alternative. OpenLogi delivers this in Rust (fast, safe, single binary) with full HID++ protocol support.

### Why It Matters
This eliminates the need for Logitech's proprietary software stack. Users get full device customization without surrendering privacy. The Rust implementation means it's fast, lightweight, and cross-platform.

### Who Should Care
Logitech mouse/keyboard users who refuse to install Options+, privacy-conscious developers, Linux users without native Logitech support, anyone wanting local hardware control.

### Execution Pattern
Download the binary for your platform, run it, detect connected Logitech devices via HID++, remap buttons and adjust settings through the GUI or CLI. Settings persist locally without cloud sync.

### Skill Potential
No — this is a desktop GUI app, not a CLI/API tool with automation potential.

- **Discovered:** 2026-06-01 via GitHub Trending (credibility: 1.00)


---

## [sandboxes](https://github.com/tastyeffectco/sandboxes)

> Self-hosted dev sandboxes with preview URLs. One command. No Kubernetes, perfect for coding agents and SaaS factories.

- **Stars:** 395 | **Language:** Go | **License:** MIT
- **Last commit:** 2026-06-05
- **Source credibility weight:** 1.00 (GitHub trending discovery)
- **Relevance score:** 72/100

### What It Does
sandboxes gives you ephemeral dev environments with shareable preview URLs in a single command. It removes the infra layer (no Kubernetes) so coding agents or indie builders can spin up previews fast.

### Why Now
Coding agents increasingly need safe, throwaway execution environments and review links. sandboxes fits that exact gap with minimal config.

### Why It Matters
Preview environments reduce shipping friction. For agent-generated PRs, the reviewer can test the result immediately instead of reading diffs blindly.

### Who Should Care
- SaaS founders shipping quickly
- Coding agents executing task → preview → review loops
- Indie hackers who want production-like previews without infra
- QA/test automation teams

### Execution Pattern
```bash
# Spin up a sandboxed preview
sandboxes up ./my-app
# Share URL and iterate
sandboxes logs ./my-app
sandboxes down ./my-app
```

### Skill Potential
Yes — installation, project initialization, preview lifecycles, plus integration with agent run loops for PR review automation.

- **Discovered:** 2026-06-05 via GitHub trending discovery (credibility: 1.00)


---

## [papernews](https://github.com/marcj/papernews)

> Self-hosted daily newspaper PDF generator for e-ink readers, powered by Claude

- **Stars:** 95 (47/day velocity) | **Language:** Python | **License:** MIT
- **Last commit:** 2026-06-04
- **Source credibility weight:** 0.88 (Hacker News Show HN, 11 points)
- **Relevance score:** 64/100
- **Discovered:** 2026-06-06 via Hacker News

### What It Does
papernews pulls RSS feeds and Hacker News stories, uses Claude to clean up and rewrite full article bodies (not summaries), and renders everything into a consistently typeset LaTeX PDF. Designed for e-ink readers like the reMarkable, but works in any PDF viewer.

### Why Now
The proliferation of news sites with different layouts, ads, and visual noise makes reading painful. papernews solves this by creating a single,安静, offline-readable PDF each day. The Docker-based setup makes it trivial to run on any machine.

### Why It Matters
Instead of juggling 5 browser tabs refreshed throughout the day, you get one calm PDF. The Claude-powered rewriting produces clean, full-text articles without the visual noise of the original sites.

### Who Should Care
reMarkable owners, e-ink enthusiasts, and anyone who prefers reading news in a clean, offline-first format. Also useful for teams wanting a daily digest of industry news.

### Execution Pattern
Clone the repo, set your Anthropic API key in .env, configure sources in sources.toml, then run docker compose up. The PDF builds on demand and is cached. Background ingest runs every 4 hours.

### Skill Potential
Yes - could automate daily newspaper generation as a cron job, or integrate with specific RSS feeds for niche industry monitoring.
