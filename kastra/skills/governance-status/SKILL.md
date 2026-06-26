---
description: Show a read-only snapshot of the user's Kastra AI-governance state — decision volume, deny rate, latency, active kill-switch incidents, and per-environment enforcement/shadow status. Use when the user asks "how is my Kastra doing", "governance status", "any incidents", "is enforcement on", or wants a quick health check of their AI governance.
---

# Kastra governance status

Give the user a concise, read-only dashboard of their Kastra governance state by
calling the read-only `kastra` MCP tools (provided by this plugin via the Kastra
OAuth connector). The first time a `kastra` tool runs, Claude Code will ask the
user to authorize in their browser — that is expected and one-time.

## Steps

1. Call `get_activity_stats` (omit `include_trends` unless the user asks for a
   time series). Pull: total decisions, last-24h and last-7d counts, denies, allow
   rate, active incident count, and decision latency percentiles.
2. Call `list_incidents` (active only — do not pass `include_resolved`). Each
   active incident is a kill-switch currently blocking AI execution.
3. Call `list_environments` to show each environment and whether it is enforcing
   or in shadow mode, plus its kill-switch state.

## Output

Render a short summary, not raw JSON:

- **Activity** — decisions (total / 24h / 7d), allow rate, deny count, p50/p95 latency.
- **Incidents** — "No active kill-switch incidents" or a bullet per active one
  (environment + what it's blocking).
- **Environments** — one line each: name → enforcing | shadow, kill-switch on/off.

End with one plain-language takeaway (e.g. "Enforcement is live on prod with a
2.1% deny rate and no active incidents.").

## If the tools aren't available

If the `kastra` tools error with an auth/connection problem, the user likely
hasn't connected the Kastra connector or doesn't have an account yet. Tell them
to approve the browser authorization when prompted, and if they have no account,
point them at the `kastra_start_signup` onboarding tool. Never invent data.
