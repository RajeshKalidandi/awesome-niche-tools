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
