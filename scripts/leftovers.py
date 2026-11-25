"""List worktrees, containers, dev servers and test browsers that may be left over.

Read-only: it stops and removes nothing. Usage: leftovers.py REPO [REPO ...]
"""
import json
import subprocess
import sys


def run(*argv, cwd=None):
    """Return (ok, stdout); a missing tool or failed command is reported, not raised."""
    try:
        done = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return False, ''
    return done.returncode == 0, done.stdout


def section(title, ok, rows):
    print(f'\n{title}')
    if not ok:
        print('  unavailable: could not be checked')
    elif not rows:
        print('  none')
    for row in rows:
        print(f'  {row}')


def pull_request(repo, branch):
    if not branch:
        return 'detached'
    ok, out = run('gh', 'pr', 'list', '--head', branch, '--state', 'all',
                  '--json', 'number,state', cwd=repo)
    if not ok:
        return 'PR unknown'
    found = json.loads(out)
    return f"PR {found[0]['number']} {found[0]['state']}" if found else 'no PR'


def worktrees(repo):
    ok, out = run('git', 'worktree', 'list', '--porcelain', cwd=repo)
    rows = []
    for block in out.strip().split('\n\n') if ok else []:
        fields = dict(line.partition(' ')[::2] for line in block.splitlines())
        path = fields['worktree']
        branch = fields.get('branch', '').removeprefix('refs/heads/')
        clean, status = run('git', 'status', '--porcelain', cwd=path)
        changes = f'{len(status.splitlines())} uncommitted' if clean else 'status unknown'
        rows.append(f"{path} | {branch or '-'} | {pull_request(repo, branch)} | {changes}")
    return ok, rows


def working_directory(pid):
    ok, out = run('lsof', '-a', '-p', pid, '-d', 'cwd', '-Fn')
    return next((line[1:] for line in out.splitlines() if line.startswith('n')), '?')


def servers():
    ok, out = run('lsof', '-nP', '-iTCP', '-sTCP:LISTEN')
    rows = set()
    for line in out.splitlines()[1:]:
        parts = line.split()
        if parts[0].lower().startswith(('node', 'python', 'bun', 'deno', 'workerd')):
            rows.add(f'{parts[8]} | {parts[0]} {parts[1]} | {working_directory(parts[1])}')
    return ok, sorted(rows)


def browsers():
    ok, out = run('ps', '-axo', 'pid=,ppid=,etime=,command=')
    rows = []
    for line in out.splitlines():
        pid, parent, age, command = line.split(None, 3)
        if '--headless' in command and '--type=' not in command and 'hrom' in command:
            rows.append(f'pid {pid} | parent {parent} | running {age}')
    return ok, rows


def containers():
    label = '{{.Label "com.docker.compose.project.working_dir"}}'
    ok, out = run('docker', 'ps', '-a', '--format', '{{.Names}} | {{.Status}} | ' + label)
    return ok, out.splitlines()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for repository in sys.argv[1:]:
        section(f'Worktrees of {repository}', *worktrees(repository))
    section('Containers (name | status | Compose directory)', *containers())
    section('Listening servers (address | process | directory)', *servers())
    section('Headless browsers', *browsers())
