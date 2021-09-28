import resume_info
import info_formatting

with open('content_template.svg', 'r') as f:
    content_template = f.read()

skills = info_formatting.skills_str(resume_info.skills)
experience = info_formatting.experience_str(resume_info.experience)
publications = info_formatting.info_str(resume_info.publications, 'p')
code = info_formatting.info_str(resume_info.code, 'p')
education = info_formatting.info_str(resume_info.education, 'h3')


with open('content.svg', 'w') as f:
    f.write(content_template.format(skills=skills, experience=experience, publications=publications, code=code, education=education))

    
