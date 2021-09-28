import pdfkit
pdfkit.from_file('readme.html', 'out.pdf', options={"--allow": "."})
