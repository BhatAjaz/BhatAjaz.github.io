#!/usr/bin/env python3
import glob
import re
import os


def parse_simple_yaml_block(yaml_text):
    data = {}
    lines = yaml_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith('#'):
            i += 1
            continue
        if ':' not in line:
            i += 1
            continue
        key, rest = line.split(':', 1)
        key = key.strip()
        value = rest.strip()
        # Handle multiline folded/scalar (| or >)
        if value in ('|', '>'):
            i += 1
            collected = []
            # collect indented lines
            while i < len(lines) and (lines[i].startswith(' ') or lines[i].startswith('\t')):
                collected.append(lines[i].lstrip())
                i += 1
            data[key] = '\n'.join(collected).rstrip()
            continue
        # remove surrounding quotes if present
        if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
            value = value[1:-1]
        data[key] = value
        i += 1
    return data


def remove_yaml_blocks(text):
    return re.sub(r'(?sm)^---\s*\n.*?\n---\s*\n', '', text)


def remove_section(text, section_title):
    pattern = rf'(?sm)^##\s*{re.escape(section_title)}.*?(?=(\n##\s)|$)'
    return re.sub(pattern, '', text)


def quote_value(v):
    if v is None:
        return '""'
    if isinstance(v, list):
        # simple list formatting
        return '[' + ', '.join('"{}"'.format(x.replace('"', '\\"')) for x in v) + ']'  # type: ignore
    if any(c in v for c in [':', '\n', '"']):
        return '"' + v.replace('"', '\\"') + '"'
    return v


def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # find all yaml front matter blocks
    yaml_blocks = list(re.finditer(r'(?sm)^---\s*\n(.*?)\n---\s*\n', text))
    if not yaml_blocks:
        print(f'No front matter found: {path}')
        return False

    first = yaml_blocks[0]
    fm_text = first.group(1)
    fm = parse_simple_yaml_block(fm_text)

    # collect abstract/methodology present in other blocks too
    abstract = fm.get('abstract')
    methodology = fm.get('methodology')

    for m in yaml_blocks[1:]:
        other = parse_simple_yaml_block(m.group(1))
        if not abstract and 'abstract' in other:
            abstract = other.get('abstract')
        if not methodology and 'methodology' in other:
            methodology = other.get('methodology')

    # Remove all yaml blocks from text to get a clean body
    body = remove_yaml_blocks(text).lstrip('\n')

    # If body already contains explicit ## Abstract or ## Methodology, extract if needed
    # Prefer front-matter values, otherwise try to extract from body
    if not abstract:
        m = re.search(r'(?sm)^##\s*Abstract\s*\n(.*?)(?=(\n##\s)|$)', body)
        if m:
            abstract = m.group(1).strip()

    if not methodology:
        m = re.search(r'(?sm)^##\s*Methodology\s*\n(.*?)(?=(\n##\s)|$)', body)
        if m:
            methodology = m.group(1).strip()

    # Remove any existing ## Abstract or ## Methodology sections to avoid duplicates
    body = remove_section(body, 'Abstract')
    body = remove_section(body, 'Methodology')

    # Trim leading/trailing whitespace
    body = body.strip() + '\n'

    # Build new body
    parts = []
    if abstract:
        parts.append('## Abstract\n\n' + abstract.strip() + '\n')
    if methodology:
        parts.append('## Methodology\n\n' + methodology.strip() + '\n')
    parts.append(body)
    new_body = '\n'.join(p.rstrip() for p in parts).rstrip() + '\n'

    # Rebuild front matter without abstract/methodology
    fm_keys = [k for k in fm.keys() if k not in ('abstract', 'methodology')]
    fm_lines = []
    for k in fm_keys:
        v = fm[k]
        if isinstance(v, str) and v.startswith('[') and v.endswith(']'):
            fm_lines.append(f"{k}: {v}")
        else:
            fm_lines.append(f"{k}: {quote_value(str(v))}")

    new_fm = '---\n' + '\n'.join(fm_lines) + '\n---\n\n'

    new_text = new_fm + new_body

    # Write back
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)

    print(f'Updated: {path}')
    return True


def main():
    base = os.path.join(os.getcwd(), '_publications')
    pattern = os.path.join(base, '*.md')
    files = glob.glob(pattern)
    if not files:
        print('No files found in _publications')
        return 1
    changed = 0
    for p in sorted(files):
        ok = process_file(p)
        if ok:
            changed += 1
    print(f'Processed {changed} files.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
