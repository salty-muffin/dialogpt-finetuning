from typing import List, Optional, Union
import os
import json
import click


def error(s: str) -> None:
    print(s)
    raise SystemExit


def parse_roles(s: Union[List, str]) -> List[str]:
    if isinstance(s, list):
        return s

    return [role.strip() for role in s.split(',')]


# yapf: disable
@click.command()
@click.argument('in_file',  nargs=1, type=click.Path(exists=True, dir_okay=False))
@click.argument('out_file', nargs=1, type=click.Path(dir_okay=False))

@click.option('-f', '--format', type=str,        help='string that determines formatting (e.g. [{{role}}:] {{text}}). must include {{role}}/{{ROLE}} (puts role in capital letters) & {{text}}.', required=True)
@click.option('-r', '--roles', type=parse_roles, help='will throw error, if roles different from these are found', required=False)
# yapf: enable
def parse(
        in_file: str, out_file: str, format: str, roles: Optional[List[str]]
    ) -> None:

    # if file is json
    if os.path.splitext(in_file)[1] == '.json':
        # read json and parse lines for textfile
        with open(in_file) as file:
            json_object = json.load(file)

        messages = [{
            'role': element['roleName'], 'text': element['message']
            } for element in json_object]

    # if file is txt
    elif os.path.splitext(in_file)[1] == '.txt':
        # read textfile
        with open(in_file) as file:
            in_lines = [
                line for line in file.readlines() if line
                ]  # discard empty lines

        messages = [{
            'role': line.split('>', 1)[0].strip(),
            'text': line.split('>', 1)[1].strip()
            } for line in in_lines]

    else:
        error('file must be either .txt or .json')

    # check roles
    if roles:
        for line_number, message in enumerate(messages, start=1):
            if (role := message['role']) not in roles:
                print(f'non matching role found in line {line_number}: {role}')

    # format message to lines
    lines = []
    for message in messages:
        line = format.replace(r'{ROLE}', message['role'].upper())
        line = line.replace(r'{role}', message['role'])
        line = line.replace(r'{text}', message['text'])
        lines.append(f'{line}\n')

    # write textfile
    with open(out_file, 'w') as file:
        file.writelines(lines)


if __name__ == '__main__':
    parse()