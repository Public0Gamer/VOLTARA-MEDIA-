# Voltara Web Studio — Agent Authentication Protocol (auth.md)

> Specification compliant with [WorkOS auth.md](https://workos.com/auth-md) and [RFC 9728](https://www.rfc-editor.org/rfc/rfc9728).

---

## 1. Overview for Autonomous Agents

Voltara Web Studio provides automated API access for AI agents (OpenAI GPTs, Claude Artifacts/Projects, Cursor, AutoGPT, MCP Clients) to query agency package availability, calculate real-time pricing estimates, and submit client website inquiries.

Read-only endpoints (package catalog, cost calculations, public agency metadata) are accessible anonymously without authentication. Protected lead submission and booking endpoints require an Agent Bearer Token.

---

## 2. Discovery Endpoints

- **OAuth Protected Resource:** `/.well-known/oauth-protected-resource`
- **OAuth Authorization Server:** `/.well-known/oauth-authorization-server`
- **OpenID Connect Discovery:** `/.well-known/openid-configuration`
- **API Catalog (RFC 9727):** `/.well-known/api-catalog`

---

## 3. Dynamic Agent Registration

Agents can register dynamically or request a client credential via the registration endpoint:

- **Registration URI:** `https://voltara.studio/api/v1/agents/register`
- **Supported Identity Types:** `did:key`, `uri:https`, `email`
- **Supported Credential Types:** `api_key`, `oauth2_client_credentials`, `jwt_bearer`
- **Token Endpoint:** `https://voltara.studio/api/v1/oauth/token`
- **Revocation Endpoint:** `https://voltara.studio/api/v1/oauth/revoke`

### Registration Request Example
```http
POST /api/v1/agents/register HTTP/1.1
Host: voltara.studio
Content-Type: application/json

{
  "client_name": "Autonomous-Procurement-Agent",
  "identity_type": "uri:https",
  "identity_value": "https://agent.example.com/id",
  "redirect_uris": ["https://agent.example.com/oauth/callback"],
  "grant_types": ["client_credentials"],
  "scope": "voltara:estimate voltara:lead"
}
```

### Response
```json
{
  "client_id": "voltara_agent_live_994b72",
  "client_secret": "vsec_live_d8a1c4b2e88f407b",
  "token_endpoint": "https://voltara.studio/api/v1/oauth/token",
  "scopes": ["voltara:estimate", "voltara:lead"]
}
```

---

## 4. Scopes & Permissions

| Scope | Access Level | Description |
| :--- | :--- | :--- |
| `voltara:read` | Public | Read package details, FAQs, agency profiles, and case studies |
| `voltara:estimate` | Public | Programmatic execution of project cost estimator algorithms |
| `voltara:lead` | Protected | Submit client inquiry and receive instant WhatsApp dispatch payload |
| `voltara:admin` | Restricted | Internal agency operational endpoints |

---

## 5. Token Request (Client Credentials Flow)

```http
POST /api/v1/oauth/token HTTP/1.1
Host: voltara.studio
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials&client_id=voltara_agent_live_994b72&client_secret=vsec_live_d8a1c4b2e88f407b&scope=voltara:estimate%20voltara:lead
```

---

## 6. Rate Limits & Policy

- **Anonymous Agents:** 120 requests / minute
- **Authenticated Agents:** 600 requests / minute
- **CORS:** All agent discovery endpoints support `Access-Control-Allow-Origin: *`
- **User-Agent:** Please identify your agent platform in the `User-Agent` HTTP header.
