# Deep Dive: Maigret

## [Maigret](https://github.com/soxoj/maigret)

> OSINT username reconnaissance tool that collects dossiers on people from 3000+ sites using only a username

- **Stars:** 31,993 (↑~200/week) | **Language:** Python | **License:** MIT
- **Last commit:** 2026-06-10
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 84/100 (after multipliers)
- **Deep Dive Date:** 2026-06-11
- **Analyst:** vibe

### What It Does

Maigret is an OSINT (Open Source Intelligence) tool that collects a comprehensive dossier on a person using only their username. It checks for accounts on 3000+ websites, gathers all available public information from those profiles, and can generate AI-powered analysis of the collected data. No API keys are required — it works by checking HTTP responses and parsing public profile pages.

The tool supports multiple output formats (JSON, CSV, HTML), can generate visual relationship graphs, and includes an AI profiling feature that analyzes the raw data to produce human-readable insights about a person's online presence, interests, and behavior patterns.

### Why Now

The OSINT tooling landscape is maturing rapidly as AI makes automated intelligence gathering more accessible. Maigret fills a specific niche: fast, no-API-key username enumeration at scale. Several factors make it relevant now:

1. **AI-powered analysis**: The new AI profiling feature transforms raw data into actionable intelligence
2. **Active maintenance**: Last commit June 10, 2026 — the project is actively developed
3. **Growing ecosystem**: OSINT is becoming a standard skill for security professionals
4. **No API keys**: In an era of API paywalls, Maigret's approach is refreshingly accessible

### Why It Matters

Maigret turns a single username into a comprehensive digital footprint in seconds. For security researchers, this means:
- **Threat hunting**: Quickly map a threat actor's online presence
- **Background checks**: Automated due diligence for hiring or partnerships
- **Incident response**: Identify compromised accounts and attack surfaces
- **Brand monitoring**: Track mentions and impersonation across platforms

The no-API-key approach is particularly valuable. Most OSINT tools require paid API access to major platforms. Maigret bypasses this by checking HTTP responses directly, making it accessible to individual researchers and small teams.

### Who Should Care

- **Security researchers**: Core OSINT tool for username-based reconnaissance
- **Penetration testers**: Reconnaissance phase automation
- **Threat intelligence analysts**: Building profiles on persons of interest
- **Journalists**: Researching individuals for stories
- **Corporate security**: Background checks and threat assessment

### Execution Pattern

1. **Single investigation**: `maigret username john_doe` — generates a complete dossier
2. **Batch processing**: Feed a list of usernames from a CSV for bulk analysis
3. **AI profiling**: Enable the AI analysis feature for human-readable summaries
4. **Integration**: Use the Python API to embed in custom security workflows
5. **Visualization**: Generate relationship graphs showing connected accounts

The CLI interface makes it scriptable. Pipe results to other OSINT tools for correlation. The HTML report format is shareable with non-technical stakeholders.

### Skill Potential

Yes — this is a prime candidate for a Hermes SKILL.md:
- Automated username investigation workflows
- Integration with security pipelines
- Batch processing patterns
- AI analysis configuration

### Deep Dive Analysis

**Architecture**: Maigret is built in Python with a clean CLI interface. It uses asynchronous HTTP requests to check thousands of sites concurrently, making it fast despite the scale. The site database is community-maintained and regularly updated. The AI profiling uses LLM APIs to analyze collected data.

**Comparison to alternatives**:
- ** Sherlock** (sherlock-project/sherlock): The original username OSINT tool. Maigret is faster (async), has more sites (3000+ vs ~400), and includes AI analysis.
- **WhatsMyName** (WebBreacher/WhatsMyName): More focused on web accounts. Maigret has broader coverage.
- **Namechk**: Commercial service with API. Maigret is free and open source.

**Trade-offs**:
- Strength: No API keys required — works out of the box
- Strength: 3000+ sites — comprehensive coverage
- Strength: AI profiling for automated analysis
- Strength: Active maintenance and community
- Weakness: HTTP-based checking can be blocked by rate limiting
- Weakness: Some sites may have changed their URL patterns
- Weakness: AI profiling requires an LLM API key (separate from the tool itself)

**Operational considerations**:
- Run with `--timeout` adjustments for slow networks
- Use proxy support for avoiding rate limits
- The site database needs regular updates (`maigret --update`)
- AI profiling costs vary by LLM provider

### Composable Stack Potential

**Maigret + Crawl4AI + Telegram Bot**: Automate OSINT investigations via Telegram. User sends a username, Maigret collects data, Crawl4AI scrapes additional context, and a Telegram bot delivers the report.

**Maigret + Jina Reader + AI Analysis**: Use Jina Reader to fetch additional context from discovered profiles, then pipe everything through an LLM for deeper analysis.

**Maigret + GitHub Actions + Scheduled Reports**: Run daily username checks on a watchlist, generate HTML reports, and commit them to a private repo for team review.

### Limitations & Trade-offs

1. **Rate limiting**: Checking 3000+ sites quickly can trigger rate limits. The async approach helps but doesn't eliminate this.
2. **Site database staleness**: URLs and profile structures change. The community database needs regular updates.
3. **False positives**: Some sites may return 200 for non-existent users. Manual verification is sometimes needed.
4. **Legal considerations**: OSINT collection may have legal implications depending on jurisdiction and use case.
5. **AI profiling dependency**: The AI analysis feature requires a separate LLM API key and costs money.
6. **Not real-time**: Results reflect the state at query time. Profiles may change or be deleted.

---

- **Discovered:** 2026-06-11 via GitHub Trending (credibility: 1.00)
- **Deep dived:** 2026-06-11 via vibe shift
