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
```bash
# Deploy with Docker
docker run -d \
  -p 8025:8025 \
  -v ./posthorn.toml:/etc/posthorn/config.toml \
  ghcr.io/craigmccaskill/posthorn:latest

# Configure providers in posthorn.toml
[providers.postmark]
api_token = "your-token"

[providers.resend]
api_key = "re_..."

# Point your apps at Posthorn
# SMTP: localhost:8025
# HTTP: http://localhost:8025/send
```

### Skill Potential
Yes — SKILL.md should cover: Docker deployment, TOML configuration, provider setup, retry configuration, and integration with Hermes email tools.

- **Discovered:** 2026-05-29 via Hacker News Show HN (credibility: 0.85)

---

## [LUKSbox](https://github.com/PentHertz/LUKSbox)

> Rust-based encrypted container tool with FIDO2, TPM 2.0, and hybrid post-quantum keyslots.

- **Stars:** 552 (↑~10/day) | **Language:** Rust | **License:** Apache-2.0
- **Last commit:** 2026-05-25
- **Source credibility weight:** 0.90 (GitHub search)
- **Relevance score:** 74/100

### What It Does
LUKSbox creates encrypted containers that mount as real drives on Linux, macOS, and Windows. It supports FIDO2 hardware keys, TPM 2.0 chip-based unlocking, and hybrid post-quantum cryptography (ML-KEM-768/1024) for future-proof security. Store sensitive files in the cloud or on shared media without trusting the host.

### Why Now
Post-quantum cryptography is moving from theory to practice. LUKSbox is one of the first tools to implement ML-KEM (formerly CRYSTALS-Kyber) for actual file encryption. Combined with FIDO2 and TPM 2.0, it provides defense against both current and future threats. The Rust implementation means memory safety and high performance.

### Why It Matters
This is "encrypt once, trust nothing" security. Your files are protected against:
- Cloud providers reading your data
- Shared computers logging your keystrokes
- Future quantum computers breaking current encryption
- Physical theft of storage media

The cross-platform support (Linux/macOS/Windows) means you can access your encrypted data anywhere.

### Who Should Care
- Security-conscious users storing sensitive files
- Developers working with proprietary code
- Journalists and activists protecting sources
- Anyone using cloud storage who wants zero-knowledge encryption

### Execution Pattern
```bash
# Install
cargo install luksbox

# Create encrypted container
luksbox create --size 10G --output secrets.luksbox

# Unlock with FIDO2 key
luksbox mount secrets.luksbox --fido2 /dev/hidraw0

# Unlock with TPM
luksbox mount secrets.luksbox --tpm

# Cross-platform access
# Linux: mounts as /dev/mapper/luksbox-*
# macOS: mounts as /Volumes/luksbox-*
# Windows: mounts as L:\ drive
```

### Skill Potential
Yes — SKILL.md should cover: installation, container creation, FIDO2/TPM setup, cross-platform mounting, and backup strategies.

- **Discovered:** 2026-05-29 via GitHub search (credibility: 0.90)

---

## [NetMap](https://github.com/xoriin/NetMap)

> Self-hosted tool for home lab / small network overview. Map devices, track IPs, monitor uptime.

- **Stars:** 87 (↑~2/day) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.90 (GitHub search)
- **Relevance score:** 65/100

### What It Does
NetMap is a self-hosted network monitoring tool designed for home labs and small networks. It discovers and maps devices, tracks IP assignments, monitors uptime, and provides firewall log analysis — all from a single web interface. Think "Ubiquiti controller" but open-source and vendor-agnostic.

### Why Now
Home labs are growing in complexity, but network monitoring tools are either enterprise-grade (overkill) or basic scripts (underpowered). NetMap fills the middle ground with a clean web UI that provides visibility without complexity. The self-hosted nature means your network data stays local.

### Why It Matters
For home lab enthusiasts and small business IT, NetMap provides the network visibility that's otherwise only available through expensive enterprise tools. Device discovery, IP tracking, and uptime monitoring in one place — no vendor lock-in, no subscription fees.

### Who Should Care
- Home lab enthusiasts with complex networks
- Small business IT managing 10-100 devices
- Network engineers wanting a simple monitoring dashboard
- Anyone tired of scanning networks with nmap manually

### Execution Pattern
```bash
# Deploy with Docker
docker run -d \
  -p 8080:8080 \
  -v ./netmap-data:/data \
  ghcr.io/xoriin/netmap:latest

# Access web UI
open http://localhost:8080

# Features:
# - Automatic device discovery
# - IP assignment tracking
# - Uptime monitoring
# - Firewall log analysis
```

### Skill Potential
No — too simple for automation. Best used as a standalone web app.

- **Discovered:** 2026-05-29 via GitHub search (credibility: 0.90)

---

## [A-Eye](https://github.com/SpaceinvaderOne/a-eye)

> Self-hosted AI photo intelligence tool. Uses local vision models via Ollama to describe, tag, rename, and search your photos.

- **Stars:** 81 (↑~2/day) | **Language:** Python | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.90 (GitHub search)
- **Relevance score:** 68/100

### What It Does
A-Eye uses local vision models (via Ollama) to analyze your photos — generating descriptions, tags, and enabling natural language search. All processing happens locally, so your photos never leave your machine. Rename files based on content, find photos by description, and build a searchable photo library without cloud services.

### Why Now
Photo management is a privacy minefield — Google Photos, Apple Photos, and iCloud all upload your photos to the cloud. A-Eye provides the same AI-powered features (smart search, auto-tagging, content-aware renaming) while keeping everything on your local machine. The Ollama integration means it runs on consumer hardware.

### Why It Matters
You get Google Photos-level intelligence without the privacy cost. Describe a photo ("sunset at the beach with the dog") and find it instantly. Auto-tag photos for organization. Rename cryptic camera filenames to descriptive ones. All running locally on your home server.

### Who Should Care
- Privacy-conscious photo collectors
- Home server enthusiasts with large photo libraries
- Anyone migrating away from cloud photo services
- Photographers who want AI-powered organization

### Execution Pattern
```bash
# Prerequisites: Ollama with vision model
ollama pull llava

# Deploy A-Eye
docker run -d \
  -p 8090:8090 \
  -v /path/to/photos:/photos \
  -v ./a-eye-data:/data \
  ghcr.io/spaceinvaderone/a-eye:latest

# Access web UI
open http://localhost:8090

# Features:
# - Auto-generate descriptions for all photos
# - Natural language search
# - Content-aware file renaming
# - Tag generation
```

### Skill Potential
No — better used as a standalone web app.

- **Discovered:** 2026-05-29 via GitHub search (credibility: 0.90)
## [Compartment](https://github.com/compartmentdev/compartment)

> Self-hosted application deployment system for teams — ship and share internal, private, or public web apps without building your own platform.

- **Stars:** 76 (↑~10/day) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.75 (GitHub Search)
- **Relevance score:** 72/100

### What It Does
Compartment is a self-hosted platform that lets teams deploy and share internal web applications. It provides SSO, RBAC, audit logging, and automated deployment — the features you'd expect from Heroku or Vercel, but running on your own infrastructure. Deploy a web app with `compartment deploy`, and it handles routing, authentication, and access control automatically.

### Why Now
Every team has internal tools — dashboards, admin panels, data viewers — that need to be shared securely. The current options are: deploy to a cloud platform (privacy concerns), build auth from scratch (time waste), or use enterprise PaaS (expensive). Compartment provides the middle ground: self-hosted deployment with built-in auth and access control. Created May 2026, actively developed.

### Why It Matters
Internal tool deployment is a solved problem at the infrastructure level (Docker, Kubernetes) but not at the access control level. Compartment adds SSO, RBAC, and audit logging on top of simple deployment — meaning your team can share tools without exposing them to the internet or building custom auth. This is the missing "internal Heroku" that every team needs.

### Who Should Care
- Teams building internal tools that need secure sharing
- DevOps engineers deploying internal dashboards
- Startups without enterprise PaaS budgets
- Anyone who has built custom auth for internal apps

### Execution Pattern
```bash
# Install
npm install -g compartment

# Initialize a project
compartment init

# Deploy
compartment deploy --name my-dashboard

# Configure access
compartment auth add-group --group eng --role admin
compartment auth add-group --group product --role viewer

# Manage deployments
compartment list
compartment logs my-dashboard
compartment rollback my-dashboard
```

### Skill Potential
Yes — SKILL.md should cover: installation, SSO configuration, RBAC setup, deployment workflows, and audit log integration.

- **Discovered:** 2026-05-30 via GitHub Search (credibility: 0.75)

---

## [Singulary](https://github.com/sammwyy/singulary)

> Self-host your own AI app builder — FOSS alternative to v0 and Lovable.

- **Stars:** 39 (↑~5/day) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-05-25
- **Source credibility weight:** 0.75 (GitHub Search)
- **Relevance score:** 70/100

### What It Does
Singulary is a self-hosted AI app builder that generates full-stack web applications from natural language descriptions. Think v0 or Lovable, but running on your own infrastructure with your own LLM keys. Describe what you want, and Singulary generates the UI, API routes, database schema, and deployment configuration — all locally.

### Why Now
AI app builders (v0, Lovable, Bolt) are popular but expensive ($20-100/month) and lock your code into their platforms. Singulary provides the same capability as open source — generate apps from descriptions while keeping full control of your code and data. The self-hosted nature means no per-generation costs and no platform lock-in.

### Why It Matters
For teams that prototype frequently, AI app builders save hours of boilerplate. Singulary makes this accessible without SaaS costs or vendor lock-in. Generate a dashboard, admin panel, or landing page in minutes — then own the code completely. The FOSS nature means you can customize the generation pipeline for your specific needs.

### Who Should Care
- Solo devs and small teams prototyping web apps
- Anyone tired of v0/Lovable subscription costs
- Developers who want AI-generated code they fully own
- Teams building internal tools rapidly

### Execution Pattern
```bash
# Install
npm install -g singulary

# Start the server
singulary serve

# Access web UI
open http://localhost:3000

# Describe what you want
# "Build a task management app with user auth, 
#  drag-and-drop boards, and real-time updates"

# Singulary generates:
# - Next.js frontend with Tailwind CSS
# - API routes with authentication
# - Database schema (Prisma)
# - Docker deployment config
```

### Skill Potential
Yes — SKILL.md should cover: installation, LLM provider configuration, customization of generation templates, and integration with deployment pipelines.

- **Discovered:** 2026-05-30 via GitHub Search (credibility: 0.75)

---
