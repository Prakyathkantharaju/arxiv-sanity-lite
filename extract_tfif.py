import json as json
import time
import os
import sys
import urllib

os.chdir('/home/prakyath/gitfolder/arxiv-sanity-lite')
from aslite.db import get_papers_db, get_metas_db
from aslite.arxiv import parse_arxiv_url


pdb = get_papers_db(flag='c')
mdb = get_metas_db(flag='c')
prevn = len(pdb)

def store(p):
    pdb[p['_id']] = p
    mdb[p['_id']] = {'_time': p['_time']}


for file_ in ['ieee.json', 'test.json']:
    f = open(file_, 'r')
    data = json.load(f)
    for paper in data['papers']:
        j = {}
        if paper['doi'] is not None:
            j['_id'] = j['id'] = ''.join(paper['doi'].split('.')[-2:])
        elif paper['publication'] is not None and 'issn' in paper['publication'].keys():
            j['_id'] = j['id'] = paper['publication']['issn']
        elif'arXiv' in paper['databases']:
            idv, rawid, version = parse_arxiv_url(paper['urls'][-1])
            j['_id'] = j['id'] = rawid
        else:
            print(paper.keys())
            print(paper)
            sys.exit()
        j['guidslink'] = False
        j['links'] = paper['urls']
        j['updated'] = paper['publication_date']
        j['title'] = paper['title']
        j['abstract'] = paper['abstract']
        j['authors'] = paper['authors']
        j['title'] = paper['title']
        j['publication'] = paper['publication']
        j['databases'] = paper['databases']
        j['tags'] = []
        if paper['databases'] == 'arxiv':
            idv, rawid, version = parse_arxiv_url(paper['urls'][-1])
            j['_version'] = rawid
        else:
            j['_version'] = 1
        time_temp = tuple([int(c) for c in paper['publication_date'].split('-')] + [0 , 0, 0, 0, 0, 0])
        # print(j['_time'])
        j['_time'] = time.mktime(time_temp)
        j['summary'] = paper['abstract']
        j['_time_str'] = time.strftime('%b %d %Y',time_temp)
        if len(paper['urls']) == 0:
            url = urllib.parse.quote_plus(paper['title'])
            j['urls'] = 'https://www.google.com/?q=' + url
        else:
            j['urls'] = paper['urls'][-1]
        store(j)

print(f'previous paper length {prevn}, new length {len(pdb)}')






# ['id', 'guidislink', 'link', 'updated', 'updated_parsed', 'published',
# 'published_parsed', 'title', 'title_detail', 'summary', 'summary_detail',
# 'authors', 'author_detail', 'author', 'arxiv_comment', 'links',
# 'arxiv_primary_category', 'tags', '_idv', '_id', '_version', '_time', '_time_str'
