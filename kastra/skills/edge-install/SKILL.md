---
description: Install Kastra Edge so policies enforce locally on this machine, after the user has a Kastra account. Use when the user has signed up and wants their Claude Code / Codex actions actually governed.
---

# Install Kastra Edge

Use this AFTER the user has a Kastra account (see the `kastra_start_signup` MCP
tool if they don't). This wires local enforcement so their agent's tool calls are
checked against their Kastra policies.

## Steps

1. Confirm the platform. These instructions target macOS (Homebrew). For other
   platforms point the user to https://kastra.ai/docs/install.

2. Install the CLI:

   ```bash
   brew install kastra-labs/tap/kastra-edge
   ```

3. Log in (opens a browser to authorize this device):

   ```bash
   kastra-edge login
   ```

4. Wire the agent hooks + MCP:

   ```bash
   kastra-edge install-claude   # Claude Code hooks + read-only MCP
   kastra-edge install-codex    # Codex hooks (restart Codex after)
   ```

5. Verify enforcement is live:

   ```bash
   kastra-edge status
   ```

Always show the user each command before running it and get their go-ahead —
these modify shell config and install software.
