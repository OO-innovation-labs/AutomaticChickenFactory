"""Check specification links and illustrative configuration consistency."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
errors = []
for document in root.rglob('*.md'):
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', document.read_text()):
        if '://' in target or target.startswith('#'):
            continue
        if not (document.parent / target.split('#')[0]).exists():
            errors.append(f'{document.relative_to(root)}: missing link {target}')
for example in sorted((root / 'examples').glob('*.json')):
    data = json.loads(example.read_text())
    required = {'schemaVersion', 'projectId', 'repository', 'base', 'factory',
                'toolchain', 'areas', 'roles', 'checks', 'knowledge', 'adapters'}
    if set(data) != required or data['schemaVersion'] != 1:
        errors.append(f'{example.name}: unexpected top-level contract')
    for name, area in data['areas'].items():
        if area['owner'] not in data['roles']:
            errors.append(f'{example.name}: unknown owner for {name}')
    names = [check['name'] for check in data['checks']]
    if len(names) != len(set(names)):
        errors.append(f'{example.name}: duplicate check names')
    for check in data['checks']:
        if not check['argv'] or not all(isinstance(arg, str) and arg for arg in check['argv']):
            errors.append(f'{example.name}: invalid check argv')
    if not re.fullmatch(r'[0-9a-f]{40}', data['factory']['revision']):
        errors.append(f'{example.name}: invalid illustrative revision')
if errors:
    raise SystemExit('\n'.join(errors))
print('Specification links and illustrative configuration consistency passed.')
print('Runtime schema validation and factory behavior remain planned work.')
