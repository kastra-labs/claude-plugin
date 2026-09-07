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
(`https://api.kastra.ai/mcp/account`) — 13 read-only governance operations (15 tool names with compatibility aliases) covering
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

### Inspect vs. enforce

This plugin is **read-only inspection**. To make Kastra actually *enforce* (block
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
to see supported commands. If `install-claude` is unavailable, use `install-hooks`.
Only use the removal commands below when they appear in that help output.
For policy inspection, the skills use the tool names advertised by the connected
server and support the older policy tool names.

This plugin keeps the hosted server name `kastra` and its `mcp__kastra__*` permissions. Onboarding stays `kastra-onboarding` at `/mcp`; inspection uses `/mcp/account`. New local wiring uses `kastra-edge`, so both can coexist. Hook governance and read-only MCP installation are separate:

```sh
kastra-edge install-mcp --target claude
kastra-edge uninstall-mcp --target claude --dry-run
kastra-edge uninstall-claude --dry-run
```

Existing local entries named `kastra` are preserved by an ordinary reinstall. To migrate one explicitly, preview `uninstall-mcp --target claude --dry-run`, remove the owned local entry with `uninstall-mcp --target claude`, then reinstall. Update any local permissions from `mcp__kastra__*` to `mcp__kastra-edge__*` when migrating; retain hosted permissions under `mcp__kastra__*`. Removal preserves hosted and unrelated entries. The two inspection surfaces overlap in capabilities; select the intended server rather than invoking both for the same operation.

`kastrahook` remains a supported executable name in release archives, Homebrew, Scoop, and desktop bundles. The plugin ID `kastra@kastra` is unchanged.

## Version & docs

**v0.2.2** — OAuth governance MCP connector (13 read-only tools) + hosted
onboarding MCP + 4 governance skills (`governance-status`, `policy-check`,
`decision-audit`, `verify-audit`) and the `edge-install` skill.

For platform guides, see [Kastra documentation](https://kastra.ai/docs).
