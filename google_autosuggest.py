import xml.etree.ElementTree as ET
from collections import defaultdict
import requests
import time


def cal_exe_time(func, xml, want="all"):
    start_time = time.time()
    data = func(xml, want)
    print(data)
    print("time taken--- {} seconds ---".format(time.time() - start_time))
    return data


def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
                d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d


def find_sugg(myroot, w="all"):
    data = []
    count = 0
    for root in myroot:
        for x in root:
            if w != "all":
                if count >= w:
                    break
            data.append(x.attrib["data"])
            count += 1
    return data


def find_data(myroot, w="all"):
    response = etree_to_dict(myroot)
    data = []
    datalist = response["toplevel"]["CompleteSuggestion"]
    count = 0
    for x in datalist:
        if w != "all":
            if count >= w:
                break
        data.append(x["suggestion"]["@data"])
        count += 1

    return data


def fetch_suggestions(query):
    x = requests.get('https://www.google.com/complete/search?output=toolbar&q={}&hl=en'.format(query))
    data = x.text
    myroot = ET.fromstring(data)
    return myroot


xml = fetch_suggestions("github")

# extraction starts here
# method 1 by converting xml to dict
cal_exe_time(find_data, xml, "all")

# method 2 by direct putting data to list

cal_exe_time(find_sugg, xml, 3)
