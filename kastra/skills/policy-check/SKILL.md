---
description: Review the active Kastra governance policy for an environment — its deny rules, which rules are actually firing, and recent governance changes. Use when the user asks "what's my policy", "show prod policy", "which rules are active/firing", "what changed in governance recently", or wants to audit their Kastra policy configuration.
---

# Kastra policy check

Summarize the active Kastra governance policy for an environment using the
read-only `kastra` MCP tools (Kastra OAuth connector, provided by this plugin).
The first `kastra` tool call triggers a one-time browser authorization.

## Steps

1. Determine the environment. Use an environment name (e.g. "prod"), never a UUID in `environment`. Resolve a supplied ID with `list_environments` first.
   Otherwise call `list_policies` first to see what exists and ask which
   environment they mean, or explicitly use the host default. A scoped OAuth grant cannot inspect another environment.
2. Call `get_active_policy` for that environment → the full active policy document
   (deny rules, scoping, lifecycle metadata) and its revision number.
3. Call `get_rule_stats` for the same environment → per-rule decision and denial
   counts, so you can show which rules are actually firing vs. dormant.
4. For revision history, obtain `policy_id` from `list_policies`, then call `list_policy_revisions`.
5. Call `list_audit_events` (default limit) → recent governance changes (policy
   promotions, kill-switch toggles, config changes), newest first.

## Output

- **Active policy** — name + revision, environment, and a readable list of deny
  rules (what each blocks/holds, effect, priority). Don't dump raw JSON; describe
  the rules.
- **Firing rules** — rank rules by denial count; call out rules with zero hits as
  candidates to review.
- **Recent changes** — a few most-recent audit events with who/what/when.

Close with one takeaway about the policy's health (e.g. "3 of 8 rules account for
all denials; 2 rules haven't fired in the window.").

## Notes

Read-only: this never edits a policy — authoring happens in the Kastra console. If
the tools error on auth, tell the user to approve the browser authorization (or
sign up via `kastra_start_signup` if they have no account). Never fabricate rules.
