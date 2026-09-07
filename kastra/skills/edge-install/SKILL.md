---
description: Install Kastra Edge so policies enforce locally on this machine, after the user has a Kastra account. Use when the user has signed up and wants their Claude Code / Codex actions actually governed.
---

# Install Kastra Edge

Use this AFTER the user has a Kastra account (see the `kastra_start_signup` MCP
tool if they don't). This wires local enforcement so their agent's tool calls are
checked against their Kastra policies.

## Steps

1. **Confirm the platform first** — the install command differs, and Homebrew
   is not the Windows path.

2. Install the CLI.

   **macOS:**

   ```bash
   brew install kastra-labs/tap/kastra-edge
   ```

   **Windows (PowerShell)** — all three lines are required. Scoop has no
   inline-tap form, so `scoop install kastra-edge` on its own fails with
   *"couldn't find manifest"*:

   ```powershell
   scoop install git    # Scoop needs git to add a third-party bucket
   scoop bucket add kastra https://github.com/kastra-labs/scoop-bucket
   scoop install kastra-edge
   ```

   If `brew` or `scoop` is missing, point the user at https://brew.sh or
   https://scoop.sh first.

   Explain the distribution difference on Windows: the binaries are **not
   code-signed**, so SmartScreen warns on first run; the Windows desktop distribution and its bundled CLIs are signed as Kastra Labs Inc. A HOLD can be approved in the console. Governance itself is identical — the hooks are the enforcement
   surface on both platforms.

   > **Linux:** there is no prebuilt Edge client. The Homebrew and Scoop
   > instructions above are for macOS and Windows. Do not offer a Linux
   > installation path for local enforcement.

3. Log in (opens a browser to authorize this device):

   ```bash
   kastra-edge login
   ```

4. Run `kastra-edge help` to check the installed commands, then wire the agent
   hooks. Only offer the optional install/removal commands below when listed in help:

   ```bash
   kastra-edge install-claude   # Claude Code hooks
   kastra-edge install-codex    # Codex hooks (restart Codex after)
   ```

   Optional read-only local inspection is a separate install:

   ```bash
   kastra-edge install-mcp --target claude
   ```

   Preview owned configuration removal with `kastra-edge uninstall-claude --dry-run`
   or `kastra-edge uninstall-mcp --target claude --dry-run`. Omit `--dry-run` to
   remove only Kastra-owned configuration. Hosted inspection remains available.

5. Verify enforcement is live:

   ```bash
   kastra-edge status
   ```

Always show the user each command before running it and get their go-ahead —
these modify shell config and install software.
