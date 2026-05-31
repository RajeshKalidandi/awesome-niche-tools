## Pattern: Secure Agent Execution with Policy Gateway

**Problem:** AI agents executing autonomously pose significant security risks when they have unrestricted access to external systems, APIs, and credentials. A compromised or misbehaving agent can exfiltrate sensitive data, make unauthorized changes, or cause financial harm.

**Solution:** Deploy a policy-enforcing gateway (like Claw Patrol) between the agent and external systems. The gateway evaluates every outbound request against declarative policies (HCL), injects credentials just-in-time, and logs/block requests that violate policies.

**When to Use:**
- Agents that need to access external APIs (GitHub, Slack, databases, etc.)
- Environments where agents handle sensitive credentials or PII
- Production agent deployments requiring audit trails and compliance
- Multi-agent systems where agents have different privilege levels

**When NOT to Use:**
- Agents operating in fully sandboxed, air-gapped environments
- Prototypes or experimental agents where security is not a concern
- Simple agents that only make local file system operations
- Cases where latency is critical and gateway overhead is unacceptable

**Discovered From:** Analysis of Claw Patrol (518★) curated by Beta shift on 2026-05-31, combined with agent security challenges observed in AI agent frameworks.

**Execution Pattern:**
1. Deploy Claw Patrol as a sidecar container or reverse proxy in your agent infrastructure
2. Define HCL policies for each agent or agent group (e.g., "research-agent can call arxiv.org and github.com/api but not internal services")
3. Configure your agent framework to route external traffic through the Claw Patrol proxy
4. Store credentials in Claw Patrol's secure vault; agents request them by reference at runtime
5. Monitor the gateway's audit logs for blocked requests and policy violations
6. Integrate with alerting systems to notify on security events
