
# from resume_content import *
# from boiler_plate import *

import boiler_plate
import resume_info


def append_text(indent_level, additions):

    if type(additions) == str:
        text = indent_level*'\t' + additions + '\n'
    elif type(additions) == list:
        text=''
        for addition in additions:
            text += indent_level*'\t' + addition + '\n'
    else:
        raise ValueError('additions should be a strings or list of strings')

    return text


innards = ''

indent_level = 3


innards += append_text(indent_level, ["<h1> Skills Summary </h1>", "<p>"])
indent_level += 1

for skill in resume_info.skills:
    innards += append_text(indent_level, skill + ' <br/>')

indent_level -= 1
innards += append_text(indent_level, '</p>')
innards += append_text(indent_level, '<h1> Experience </h1>')

for title, info in resume_info.experience.items():
    innards += append_text(indent_level, '<h2> ' + title + ' </h2>')
    innards += append_text(indent_level, '<h3> ' + info[0] + ' </h3>')
    innards += append_text(indent_level, '<p> ' + info[1] + ' </p>')

innards += append_text(indent_level, '<h1> Publications </h1>')

for publication in resume_info.publications:
    innards += append_text(indent_level, '<p> ' + publication + ' </p>')

innards += append_text(indent_level, '<h1> Code </h1>')

for some_code in resume_info.code:
    innards += append_text(indent_level, '<p> ' + some_code + ' </p>')

innards += append_text(indent_level, '<h1> Eduction </h1>')

for some_education in resume_info.education:
    innards += append_text(indent_level, '<h3> ' + some_education + ' </h3>')

content_svg_text = boiler_plate.content_svg_start + innards + boiler_plate.end

with open('content.svg', 'w') as f:
    f.write(content_svg_text)

html_text = boiler_plate.html_start + innards + boiler_plate.end

with open('resume.html', 'w') as f:
    f.write(html_text)
