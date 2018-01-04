import json
import re
import datetime
import urllib2

_FILE_NAME = "/Users/jane/rfc-analysis/parent_id_added.json"
with open(_FILE_NAME) as file:
    stored_rfcs = json.load(file)


# # https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=parentid&format=jsonfm&formatversion=2&revids=618183389|618183399
# first get the diff blob
# https://en.wikipedia.org/w/api.php?action=compare&fromrev=611979064&torev=611981981
tracked = []
for id,res in stored_rfcs.items():
    fromrev = res['parent_id']
    torev = str(id)
    from wikitools import wiki, api
    site = wiki.Wiki('https://en.wikipedia.org/w/api.php?')
    params = {'action': 'compare', 'fromrev':fromrev, 'torev':torev}

    request = api.APIRequest(site, params)
    try:
        result = request.query()['compare']
        diff = result['*']

        stored_rfcs[id]['diff'] = diff
        stored_rfcs[id]['id'] = id

        with open("/Users/jane/rfc-analysis/diff_added_" + str(id) + ".json", "w") as file:
            json.dump(stored_rfcs[id], file)
        tracked.append(id)

    except api.APIError:
        with open("/Users/jane/rfc-analysis/tracked_ids.json", "w") as file:
            json.dump(tracked, file)

