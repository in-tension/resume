import resume_info

tabs = ['\t'*i for i in range(10)]

def skills_str(skill_list):
    skills_txt = ''
    for skill in skill_list:
        skills_txt += '{tabs[4]}{skill} <br/>\n'.format(tabs=tabs, skill=skill)

    return '{tabs[3]}<p>\n{skills_txt}{tabs[3]}</p>'.format(tabs=tabs, skills_txt=skills_txt)

# print(skills_str(resume_info.skills))
# print()


def experience_str(exp_dict):
    exp_txt = ''
    for title, info in exp_dict.items():
        exp_txt += '''{tabs[3]}<h2> {title} </h2>
        {tabs[3]}<h3> {info[0]} </h3>
        {tabs[3]}<p>
        {tabs[4]}{info[1]}
        {tabs[3]}</p>
        '''.format(tabs=tabs, title=title, info=info)

    return exp_txt

# print(experience_str(resume_info.experience))
# print()


def info_str(infos, tag):
    info_txt = ''
    for info in infos:
        info_txt = '{tabs[3]}<{tag}>\n{tabs[4]}{info}\n{tabs[3]}</{tag}>\n'.format(tabs=tabs, tag=tag, info=info)

    return info_txt

# print(info_str(resume_info.publications, 'p'))
# print()

# print(info_str(resume_info.code, 'p'))
# print()

# print(info_str(resume_info.education, 'h3'))
# print()
