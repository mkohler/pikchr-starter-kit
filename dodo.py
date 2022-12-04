from pathlib import Path
import subprocess

PNG_HEIGHT = 1000


def show_cmd(task):
    return f'executing... {task.actions[0]}'


def task_markdown_to_pdf():
    for md in Path('.').glob('*.md'):
        Path('pdf').mkdir(exist_ok=True)
        pdf = (Path('pdf') / md.stem).with_suffix('.pdf')
        yield {
            'name': pdf.name,
            'actions': [[
                'pandoc',
                '--self-contained',
                '--lua-filter', 'pikchr.lua',
                '-f', 'markdown',
                '-t', 'pdf',
                md,
                '-o', pdf
            ]],
            'file_dep': [md],
            'targets': [pdf],
            'title': show_cmd,
        }


def pikchr_to_svg(pikchr_in, svg_out):
    '''We need to use subprocess because pikchr writes the svg to stdout.'''
    with open(svg_out, 'w', encoding='utf-8') as svg_f:
        subprocess.run(
            ['pikchr', '--svg-only', pikchr_in],
            check=True,
            stdout=svg_f)


def task_pikchr_to_png():
    for pikchr in Path('.').glob('*.pikchr'):
        Path('png').mkdir(exist_ok=True)
        Path('svg').mkdir(exist_ok=True)
        svg = Path('svg') / pikchr.with_suffix('.svg')
        png = (Path('png') / svg.stem).with_suffix('.png')
        yield {
            'name': pikchr.name,
            'actions': [
                (pikchr_to_svg, [pikchr, svg]),
                [
                    'inkscape',
                    f'--export-filename={png}',
                    f'--export-height={PNG_HEIGHT}',
                    '--export-background=white',
                    svg,
                ],
            ],
            'file_dep': [pikchr],
            'targets': [png],
            'title': show_cmd,
        }
