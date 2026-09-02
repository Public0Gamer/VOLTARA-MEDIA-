# DNS for AI Discovery (DNS-AID) — Deployment Guide

> Compliant with **draft-mozleywilliams-dnsop-dnsaid** and **RFC 9460 (SVCB / HTTPS Resource Records)**.

DNS-AID enables autonomous AI agents (such as OpenAI Operator, Anthropic Claude Agents, Google Gemini Autonomous Agents) to discover API capabilities, MCP servers, and agent skills directly through the domain name system (DNS) before initiating any HTTP requests.

---

## 1. Required DNS Records

Add the following records to your domain's DNS provider (Cloudflare, AWS Route 53, Vercel DNS, or Google Cloud DNS):

### Entrypoint 1: AI Discovery Index (`_index._agents`)
- **Record Type:** `HTTPS` (or `SVCB`)
- **Name / Host:** `_index._agents`
- **Priority / SvcPriority:** `1`
- **Target:** `voltara.studio` (or your root domain)
- **Parameters / Value:** `alpn="h2,h3" port="443" key65301="/.well-known/ai-catalog.json"`

### Entrypoint 2: Agent-to-Agent Endpoint (`_a2a._agents`)
- **Record Type:** `HTTPS` (or `SVCB`)
- **Name / Host:** `_a2a._agents`
- **Priority / SvcPriority:** `1`
- **Target:** `voltara.studio`
- **Parameters / Value:** `alpn="h2,h3" port="443" key65301="/api/v1/agents"`

### Entrypoint 3: MCP Server Discovery (`_mcp._agents`)
- **Record Type:** `HTTPS` (or `SVCB`)
- **Name / Host:** `_mcp._agents`
- **Priority / SvcPriority:** `1`
- **Target:** `voltara.studio`
- **Parameters / Value:** `alpn="h2,h3" port="443" key65301="/.well-known/mcp/server-card.json"`

### Entrypoint 4: Compatibility TXT Record
- **Record Type:** `TXT`
- **Name / Host:** `_agents`
- **Content:** `"v=aid1; card=/.well-known/mcp/server-card.json; ard=/.well-known/ai-catalog.json; skills=/.well-known/agent-skills/index.json"`

---

## 2. DNSSEC Validation Requirement

Per DNS-AID specification, all agent discovery records MUST be signed with **DNSSEC** (Domain Name System Security Extensions).
- If using **Cloudflare**: Navigate to **DNS** → **Settings** → **Enable DNSSEC** (1-click).
- Copy the generated DS record to your domain registrar (GoDaddy, Namecheap, Google Domains).
