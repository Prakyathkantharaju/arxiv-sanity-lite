import json as json
import time
import os

os.chdir('/home/prakyath/gitfolder/arxiv-sanity-lite')
from aslite.db import get_papers_db, get_metas_db

# loading ieee json
f = open('ieee.json', 'r')
data = json.load(f)

print(data.keys())

print(data['papers'][0].keys())


print(''.join(data['papers'][0]['doi'].split('.')[-2:]))
print(data['papers'][0].keys())
print(data['papers'][0]['urls'])
print(data['papers'][0]['publication_date'])
pdb = get_papers_db(flag='c')
mdb = get_metas_db(flag='c')
prevn = len(pdb)

def store(p):
    pdb[p['_id']] = p
    mdb[p['_id']] = {'_time': p['_time']}

for paper in data['papers']:
    j = {}
    j['_id'] = j['id'] = ''.join(paper['doi'].split('.')[-2:])
    j['guidslink'] = False
    j['links'] = paper['urls']
    j['updated'] = paper['publication_date']
    j['title'] = paper['title']
    j['abstract'] = paper['abstract']
    j['authors'] = paper['authors']
    j['title'] = paper['title']
    j['tags'] = []
    j['_version'] = 1
    j['_time'] = paper['publication_date']
    store(p)

print(f'previous paper length {prevn}, new length {len(pdb)}')






# ['id', 'guidislink', 'link', 'updated', 'updated_parsed', 'published',
# 'published_parsed', 'title', 'title_detail', 'summary', 'summary_detail',
# 'authors', 'author_detail', 'author', 'arxiv_comment', 'links',
# 'arxiv_primary_category', 'tags', '_idv', '_id', '_version', '_time', '_time_str'
