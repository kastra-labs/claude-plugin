---
description: Search Kastra decision history and explain denials — e.g. "show me denials in the last 24h", "why was I blocked", "what did Kastra deny on prod today", "which rule stopped this action". Use when the user wants to inspect past ALLOW/DENY decisions or debug why an action was governed.
---

# Kastra decision audit

Search the user's Kastra decision history and explain outcomes using the
read-only `kastra` MCP tools (Kastra OAuth connector, provided by this plugin).
The first `kastra` tool call triggers a one-time browser authorization.

## Steps

1. Build filters for `search_decisions` from the user's request:
   - `decision`: `DENY` when they ask about blocks/denials; omit for both.
   - `environment`: the env they named (e.g. `prod`); omit for all.
   - `from` / `to`: RFC3339 bounds. Translate "last 24h", "today", "this week"
     into a concrete `from` (and `to` if needed).
   - `limit`: keep modest (e.g. 50) unless they ask for more (max 1000).
2. Call `search_decisions`. Results are newest-first; each carries the outcome,
   environment, matched rule, source, and latency.
3. When the user is debugging *why* something was denied, also call
   `get_rule_stats` for that environment to show how often the matched rule fires.

## Output

- A compact table or list: time, environment, decision, matched rule, source.
- For denials, lead with the matched rule and a plain-language reason
  ("Denied by rule 'block-prod-db-writes' — writes to prod DB require a HOLD.").
- If the user asked a yes/no ("was X allowed?"), answer it directly, then show
  the supporting decision.

## Notes

`source` and `actor_email` filters are currently informational (stored, not
filtered server-side) — note that if the user relies on them. Read-only; never
fabricate decisions. On an auth error, tell the user to approve the browser
authorization (or sign up via `kastra_start_signup` if they have no account).
