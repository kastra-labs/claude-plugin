"""Validate plugin metadata and references; never execute skill instructions."""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
registry=json.loads((root/'contracts/producers.json').read_text())
for file in [root/'kastra/.mcp.json',root/'kastra/.claude-plugin/plugin.json',root/'.claude-plugin/marketplace.json']:
 json.loads(file.read_text())
servers=json.loads((root/'kastra/.mcp.json').read_text())['mcpServers']
assert servers['kastra']['url']=='https://api.kastra.ai/mcp/account'
assert servers['kastra-onboarding']['url']=='https://api.kastra.ai/mcp'
assert len(servers)==2, 'Do not silently duplicate or rename installed namespaces'
known=set(registry['shared_tools']+registry['onboarding_tools'])
for file in [root/'README.md',*sorted((root/'kastra/skills').glob('*/SKILL.md'))]:
 text=file.read_text()
 for tool in re.findall(r'`((?:get|list|search|verify|kastra_start|kastra_signup)[a-z_]*)`',text):
  assert tool in known, f'{file}: unknown tool {tool}'
 for cmd in re.findall(r'kastra-edge ([a-z]+(?:-[a-z]+)*)',text):
  assert cmd in registry['edge_commands'],f'{file}: unknown Edge command {cmd}'
assert 'max 200' in (root/'kastra/skills/decision-audit/SKILL.md').read_text()
print('Plugin metadata, namespaces, and public tool/command references passed.')
