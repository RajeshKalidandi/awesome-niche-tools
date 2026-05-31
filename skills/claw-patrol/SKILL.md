name: claw-patrol
description: "Security firewall for AI agents that routes traffic through a gateway with HCL-based policy rules and credential injection."
tags: [security, ai-agents, self-hosted, gateway, credentials]
platforms: [linux]
related_skills: []
version: 1.0.0
author: Hermes Agent
license: MIT

# Claw Patrol Skill

This skill provides automation for deploying and configuring Claw Patrol, the open-source security firewall for AI agents.

## Prerequisites

- Docker or Podman installed
- Basic understanding of HCL (HashiCorp Configuration Language)
- AI agent framework that supports HTTP proxy configuration
- Access to the credentials/services you want to protect

## Installation

Pull the Claw Patrol Docker image:

```bash
docker pull denoland/clawpatrol:latest
```

Or build from source:

```bash
git clone https://github.com/denoland/clawpatrol.git
cd clawpatrol
docker build -t clawpatrol .
```

## Configuration

Create an HCL policy file (`policy.hcl`) defining what your agent can access:

```hcl
# Allow GitHub API access
http {
  method = "GET"
  host   = "api.github.com"
  path   = "/user/*"
  
  # Inject GitHub token at request time
  header "Authorization" = "token {{ env.GITHUB_TOKEN }}"
}

# Allow database access (read-only)
sql {
  query = "SELECT * FROM users WHERE id = $1"
  
  # Inject database credentials
  username = "{{ env.DB_USERNAME }}"
  password = "{{ env.DB_PASSWORD }}"
}

# Block everything else by default
default {
  action = "deny"
}
```

## Usage

Run Claw Patrol as a sidecar proxy:

```bash
docker run -d \
  --name clawpatrol \
  -p 8080:8080 \
  -v ./policy.hcl:/etc/clawpatrol/policy.hcl \
  -e GITHUB_TOKEN=${GITHUB_TOKEN} \
  -e DB_USERNAME=${DB_USERNAME} \
  -e DB_PASSWORD=${DB_PASSWORD} \
  denoland/clawpatrol:latest
```

Configure your AI agent to use `localhost:8080` as its HTTP/HTTPS proxy.

## Examples

### Basic HTTP filtering

```hcl
http {
  host = "api.example.com"
  path = "/data/*"
  
  header "Authorization" = "Bearer {{ env.API_TOKEN }}"
}
```

### Kubernetes access control

```hcl
kubernetes {
  resource = "pods"
  verb     = "get"
  
  # Inject kubeconfig or token
  bearer_token = "{{ env.KUBE_TOKEN }}"
}
```

### Blocking dangerous operations

```hcl
# Block all AWS metadata access
http {
  host = "169.254.169.254"
  action = "deny"
}

# Block database drops
sql {
  query = "DROP TABLE *"
  action = "deny"
}
```

## Environment Variables

- `CLAW_PATROL_LOG_LEVEL`: Debug, Info, Warn, Error (default: Info)
- `CLAW_PATROL_LISTEN_ADDR`: Address to listen on (default: ":8080")
- `CLAW_PATROL_POLICY_FILE`: Path to policy file (default: "/etc/clawpatrol/policy.hcl")

## Monitoring

Claw Patrol exposes metrics at `/metrics` in Prometheus format:
- `clawpatrol_requests_total`: Total requests processed
- `clawpatrol_requests_allowed`: Requests allowed by policy
- `clawpatrol_requests_denied`: Requests denied by policy
- `clawpatrol_active_connections`: Currently active connections

## Common Pitfalls

- **Overly permissive policies**: Start with deny-all and explicitly allow what's needed
- **Credential leakage**: Ensure credentials are only injected into allowed requests
- **Performance impact**: Add caching for frequently used credentials if needed
- **Protocol mismatches**: Verify your agent's traffic matches the protocol rules (HTTP/SQL/K8s)

## Verification

Test that your policy works:

1. Make a request that should be allowed: `curl -x localhost:8080 https://api.github.com/user`
2. Make a request that should be blocked: `curl -x localhost:8080 http://169.254.169.254/latest/meta-data/`
3. Check the logs: `docker logs clawpatrol`
4. Verify metrics: `curl http://localhost:8080/metrics`

## References

- GitHub Repository: https://github.com/denoland/clawpatrol
- HCL Language Docs: https://developer.hashicorp.com/language/hcl
- Docker Hub: https://hub.docker.com/r/denoland/clawpatrol