# Plugin compatibility checks

Run `python3 contracts/check.py` to validate plugin metadata, hosted MCP server
URLs, and command/tool references in the README and skills. `producers.json` lists
the public interfaces used by this plugin; each has exactly one name.

The check validates references without installing the plugin, running skill
instructions, or accessing an account.

The upcoming request-view contract adds read-only `get_request_stages`. It keeps
linked admission and final audit records available while presenting one logical
request when `search_decisions` explicitly selects `view: requests`. Omitted
`view` preserves individual audit records. This producer inventory is not a deployment or plugin release claim;
use only names and arguments advertised by the connected server.
