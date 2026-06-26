---
description: Verify the integrity of the Kastra tamper-evident decision audit chain. Use when the user asks "verify my audit chain", "is the audit log tamper-evident", "check audit integrity", or needs compliance assurance that the decision log hasn't been altered.
---

# Kastra verify audit chain

Confirm that the user's Kastra decision history is tamper-evident by calling the
read-only `verify_audit_chain` tool on the `kastra` MCP connector (provided by
this plugin). The first `kastra` tool call triggers a one-time browser
authorization.

## Steps

1. Call `verify_audit_chain` (no arguments). It returns `ok`, `state`
   (e.g. intact), the chain length, the head hash, and how many entries were
   checked.

## Output

State the result clearly for a compliance reader:

- ✅ **Intact** — "Audit chain verified: N entries, state intact, head hash
  `<short>`. The decision log is cryptographically tamper-evident."
- ❌ **Not intact** — surface the reported `state` verbatim and flag it as
  requiring investigation; do not soften it.

Keep it short and unambiguous — this is an attestation, not a dashboard.

## Notes

Read-only. On an auth/connection error, tell the user to approve the browser
authorization (or sign up via `kastra_start_signup` if they have no account).
Never claim the chain is intact without a successful tool result.
