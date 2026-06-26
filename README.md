# Kastra Claude plugin

Govern your AI agents with [Kastra](https://kastra.ai). This plugin lets your
assistant **inspect your Kastra governance state read-only** — policies,
decisions, the tamper-evident audit chain, kill-switch incidents, and
environments — plus create a free account and install local enforcement.

## Add Kastra to Claude in one click (claude.ai)

**[➕ Add Kastra to Claude](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Kastra&connectorUrl=https%3A%2F%2Fapi.kastra.ai%2Fmcp)**

Opens the "add custom connector" dialog in claude.ai pre-filled with Kastra's
hosted MCP (`https://api.kastra.ai/mcp`) — no copy-pasting a URL. It gives your
assistant the onboarding tools (`kastra_start_signup`, `kastra_signup_status`)
so you can spin up a free-tier account without leaving the chat.

## Claude Code plugin

```
/plugin marketplace add kastra-labs/claude-plugin
/plugin install kastra@kastra
```

### What you get

**Read-only governance inspection** via the Kastra OAuth connector
(`https://api.kastra.ai/mcp/account`). The first time a governance tool runs,
Claude Code opens your browser to authorize once (OAuth 2.1 + PKCE, scope
`kastra.account.read`) — it never sees a pasted API key. Then your assistant can
read your policies, decisions, audit chain, incidents, and activity stats.

**Governance slash commands** (composed from the read-only tools):

| Command | What it does |
|---|---|
| `/kastra:governance-status` | Snapshot: decision volume, deny rate, latency, active incidents, per-environment enforcement/shadow state |
| `/kastra:policy-check` | Active policy for an environment, which rules are firing, and recent governance changes |
| `/kastra:decision-audit` | Search decision history and explain denials ("why was I blocked?") |
| `/kastra:verify-audit` | Verify the tamper-evident decision audit chain is intact |

**Onboarding tools** (`kastra_start_signup`, `kastra_signup_status`) backed by
the hosted MCP — create a free-tier account without leaving the chat. They create
no account and send no email themselves; they return a link you open to finish a
normal, email-confirmed signup.

**`/kastra:edge-install` skill** — guides setup of the *local enforcement edge*
(`kastra-edge`) so your agent's tool calls are actually blocked/held against your
policies. See below.

### Inspect vs. enforce

This plugin is **read-only inspection**. To make Kastra actually *enforce* (block
or hold tool calls) on this machine, install the local edge — run
`/kastra:edge-install` or `brew install kastra-labs/tap/kastra-edge && kastra-edge
login && kastra-edge install-claude`. Local enforcement runs as a Claude Code
hook from the `kastra-edge` CLI; bundling it directly into this plugin is a
planned future version.

> Note: the governance connector registers as an MCP server named `kastra`, so
> its tools surface as `mcp__kastra__*`. If you also have the local
> `kastra-edge` MCP installed under the same name, expect a naming overlap.
