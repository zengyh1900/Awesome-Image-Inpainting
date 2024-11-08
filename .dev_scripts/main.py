import re
import os
import csv
from tqdm import tqdm
import argparse
import functools

parser = argparse.ArgumentParser(description = 'What the program does')
parser.add_argument('-f', choices=['csv', 'md'], default='md')
args = parser.parse_args()

DIR_ROOT= os.path.dirname(os.path.abspath(__file__))
COLLECTION_CSV = os.path.join(DIR_ROOT, 'collection.csv')
MD_FILE= os.path.join(DIR_ROOT, '../README.md')

HEAD = f"""# Awesome-Inpainting-Tech
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) ![visitors](https://visitor-badge.glitch.me/badge?page_id=1900zyh/Awesome-Image-Inpainting) ![GitHub stars](https://img.shields.io/github/stars/1900zyh/Awesome-Image-Inpainting?color=green)  ![GitHub forks](https://img.shields.io/github/forks/1900zyh/Awesome-Image-Inpainting?color=9cf)

A curated list of inpainting papers and resources, inspired by [awesome-computer-vision](https://github.com/jbhuang0604/awesome-computer-vision).

This `README.md` is automatically generated from [`.dev_scripts/collection.csv`](.dev_scripts/collection.csv).

We provide [scripts](.dev_scripts/main.py) to automatically generate `README.md` from CSV file or vice versa.

Welcome to pull request to update or correct this collection. 🥰
"""

def readme_to_csv():
    # save all data to csv file
    csvfile = open(COLLECTION_CSV, 'w')
    csv_writer = csv.writer(csvfile, delimiter=',')
    csv_writer.writerow(['Year', 'Conf', 'Type', 'Ttitle', 'URL', 'Code', 'Project'])

    # parse data from readme
    with open(MD_FILE, 'r', encoding='utf-8') as md:
        lines = md.readlines()

    type = None
    papers = []
    i = 0
    while i < len(lines):
        if '## Year' not in lines[i]:
            i += 1
        else:
            year = int(re.match(r'## Year (.*)', lines[i]).groups()[0])
            i += 1
            while i < len(lines) and (r'## Year' not in lines[i]):
                line = lines[i]
                conf, type, title, url = re.match(
                    r'- \*\*(.*)\*\* \((.*)\) \[(.*)\]\((.*)\)\..*', line).groups()

                project, code = None, None
                if '[code]' in line:
                    code = line.split('[[code]](')[-1].split(')')[0]
                if '[project]' in line:
                    project = line.split('[[project]](')[-1].split(')')[0]

                papers.append(dict(title=title, url=url, conf=conf, year=year, project=project, code=code, type=type))
                i += 1

    papers = sorted(papers, key=lambda x: (x['year'], x['conf'], x['type']), reverse=True)
    for p in papers:
        csv_writer.writerow([p['year'], p['conf'], p['type'], p['title'], p['url'], p['code'], p['project']])
    csvfile.close()


def csv_to_readme():
    # save all data to csv file
    csvfile = open(COLLECTION_CSV)
    csv_reader = csv.reader(csvfile, delimiter=',')

    papers = {}
    # parse data from csv file
    for idx, row in enumerate(csv_reader):
        if idx == 0:
            continue
        try:
            year, conf, type, title, url, code, project = row
        except:
            print(row)
        p = dict(title=title, url=url, conf=conf, year=year, project=project, code=code, type=type)
        if str(year) not in papers:
            papers[str(year)] = [p]
        else:
            papers[str(year)].append(p)

    for k, v in papers.items():
        papers[k].sort(key=lambda x: (x['year'], x['conf'], x['type']), reverse=True)

    message = {}
    # generate msg from parsed dict data
    years = sorted([y for y in list(papers.keys())], reverse=True)
    for k,v in papers.items():
        msg = f"## Year {k}\n"
        for p in v:
            msg += f"- **{p['conf']}** ({p['type']}) [{p['title']}]({p['url']})."
            if p['code']:
                msg += f" [[code]]({p['code']}) "
            if p['project']:
                msg += f" [[project]]({p['project']}) "
            msg += "\n"
        message[k] = msg

    # write to readme
    readme_content = HEAD
    for y in years:
        readme_content += message[y]
    with open(MD_FILE, 'w') as f:
        f.write(readme_content)





if __name__ == '__main__':
    if args.f == 'csv':
        readme_to_csv()
    elif args.f == 'md':
        csv_to_readme()
    else:
        raise ValueError('Invalid target format. Only support csv or md.')