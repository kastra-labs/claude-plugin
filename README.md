# Kastra Claude plugin

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

Gives your agent two onboarding tools (`kastra_start_signup`,
`kastra_signup_status`) backed by the hosted MCP at https://api.kastra.ai/mcp,
plus the `/kastra:edge-install` skill to set up local enforcement.

The onboarding MCP creates no account and sends no email itself — it returns a
link you open to finish a normal, email-confirmed signup.
