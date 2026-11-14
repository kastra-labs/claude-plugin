# Kastra Claude plugin

Govern your AI agents with [Kastra](https://kastra.ai). This plugin lets your
assistant **inspect your Kastra governance state read-only** — policies,
decisions, the tamper-evident audit chain, kill-switch incidents, and
environments. Agent Builder support is coming soon (see below). The plugin also
provides account signup and local enforcement setup.

## Add Kastra to Claude (claude.ai)

**[➕ Add Kastra to Claude](https://claude.ai/customize/connectors)**

Open the connectors page and add Kastra with OAuth and the hosted account URL
`https://api.kastra.ai/mcp/account`. Sign into Kastra and
choose a workspace for read-only governance. Upcoming Agent Builder support uses
the same connection, with a separate opt-in when available.

## Claude Code plugin

```
/plugin marketplace add kastra-labs/claude-plugin
/plugin install kastra@kastra
```

### What you get

**Read-only governance inspection** via the Kastra OAuth connector
(`https://api.kastra.ai/mcp/account`) — 13 read-only governance tools covering
policies, decisions, environments, the tamper-evident audit chain, kill-switch
incidents, API keys, and activity/rule stats. The first time a governance tool
runs, Claude Code opens your browser to authorize once (OAuth 2.1 + PKCE, scope
`kastra.account.read`) — it never sees a pasted API key.

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

### Improve agents you choose

**Coming soon:** Builder is disabled by default and has not yet been qualified
for production host use. In enabled workspaces, owners and administrators check
**Allow Agent Builder access** during consent (off by default),
then choose agents in **Connections → AI assistants**. Leaving it unchecked keeps
governance-only access, including on reconnect. Every agent starts hidden.
Preview the exact shared fields and choose read, proposal and simulation access.
Credentials stay private. Selected run evidence and detailed simulation results
require explicit release in Kastra.

| Tool | Purpose |
|---|---|
| `list_authoring_agents` | List agents enabled for this connection |
| `get_agent_authoring_context` | Read the latest permitted saved draft |
| `create_agent_proposal` | Propose changes for review in Kastra |
| `get_agent_proposal` | Read proposal status and its review link |
| `compare_agent_proposal` | Run permitted paid simulations within configured limits |
| `get_agent_comparison` | Read simulation status and released results |

After accepting or editing a draft, ask Claude to read its latest context again.
The simulation allowance starts at zero and never resets on reconnect. Simulations
never execute connected tools. Agent creation, MCP setup, permissions, acceptance,
publication and live actions remain in Kastra. Disable Builder access to retain
governance reads; disconnect Kastra to revoke both. Restoring an administrator role
does not restore a revoked Builder delegation.

### Inspect vs. enforce

Governance tools remain **read-only**. Upcoming Builder support can propose changes
and run permitted simulations. To make Kastra actually *enforce* (block
or hold tool calls) on this machine, install the local edge — run
`/kastra:edge-install`, which picks the right command for your platform, or do it
by hand:

```bash
# macOS
brew install kastra-labs/tap/kastra-edge
```

```powershell
# Windows — all three lines; scoop has no inline-tap form, so
# `scoop install kastra-edge` alone fails with "couldn't find manifest"
scoop install git
scoop bucket add kastra https://github.com/kastra-labs/scoop-bucket
scoop install kastra-edge
```

Then `kastra-edge login && kastra-edge install-claude` on either platform. Local
enforcement runs as a Claude Code hook from the `kastra-edge` CLI. There is no
prebuilt Edge client for Linux.

### Companion release and MCP coexistence

Command availability depends on your installed Edge version. Run `kastra-edge help`
to see supported commands, and only use the removal commands below when they
appear in that help output. Each MCP operation has exactly one tool name
(`get_active_policy`, `list_policy_revisions`); a saved permission that still
names a pre-release tool must be updated.

This plugin keeps the hosted server name `kastra` and its `mcp__kastra__*` permissions. Onboarding stays `kastra-onboarding` at `/mcp`; governance and Builder use `/mcp/account`. New local wiring uses `kastra-edge`, so both can coexist. Hook governance and read-only MCP installation are separate:

```sh
kastra-edge install-mcp --target claude
kastra-edge uninstall-mcp --target claude --dry-run
kastra-edge uninstall-claude --dry-run
```

`install-mcp --target claude` moves a pre-release local entry named `kastra` to `kastra-edge` and tells you to update saved permissions for the local tools from `mcp__kastra__*` to `mcp__kastra-edge__*`; hosted permissions stay under `mcp__kastra__*`. Removal preserves hosted and unrelated entries. The two inspection surfaces overlap in capabilities; select the intended server rather than invoking both for the same operation.

`kastrahook` remains a supported executable name in release archives, Homebrew, Scoop, and desktop bundles. The plugin ID `kastra@kastra` is unchanged.

## Version & docs

**v0.2.2** — Read-only governance inspection, plus hosted
onboarding MCP + 4 governance skills (`governance-status`, `policy-check`,
`decision-audit`, `verify-audit`) and the `edge-install` skill.

The plugin listing stays governance-only. A Builder version bump and listing
claims wait for server enablement and host qualification.

For platform guides, see [Kastra documentation](https://kastra.ai/docs).
