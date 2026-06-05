# Kastra Claude plugin

Install:

```
/plugin marketplace add kastra-labs/claude-plugin
/plugin install kastra@kastra
```

Gives your agent two onboarding tools (`kastra_start_signup`,
`kastra_signup_status`) backed by the hosted MCP at https://api.kastra.ai/mcp,
plus the `/kastra:edge-install` skill to set up local enforcement.

The onboarding MCP creates no account and sends no email itself — it returns a
link you open to finish a normal, email-confirmed signup.
