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

   **macOS / Linuxbrew:**

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

   Tell a Windows user two things up front: the binaries are **not
   code-signed**, so SmartScreen warns on first run; and there is **no desktop
   app on Windows**, so a HOLD is approved from the console rather than from a
   notification. Governance itself is identical — the hooks are the enforcement
   surface on both platforms.

   > **Linux:** there is no prebuilt Edge client. `release.yml` builds the edge
   > binaries for darwin and windows only, and the Homebrew formula's URL is a
   > darwin tarball — under Linuxbrew it fetches Mach-O binaries that cannot
   > run. Only the separate `kastra` control-plane CLI ships for Linux, and it
   > governs nothing on its own. Do not offer a Linux path here.

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
