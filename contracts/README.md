# Plugin compatibility checks

Run `python3 contracts/check.py` to validate plugin metadata, hosted MCP server
URLs, and command/tool references in the README and skills. `producers.json` lists
the public interfaces used by this plugin; each has exactly one name.

The check validates references without installing the plugin, running skill
instructions, or accessing an account.
