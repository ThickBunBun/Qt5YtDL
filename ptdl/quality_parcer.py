import re


# quality filter for videodl funtion
def ql_filter(yt):
    ql_list = []
    dict_list = []
    dictionary = {}
    linkfilter = re.compile(r'itag=["\w]+ mime_type="video/mp4" res=["\w]+')
    stream_ls = yt.streams.filter(adaptive=True)
    quality = linkfilter.findall(f'{stream_ls}')
    for ql in quality:
        ql_list.append(str(ql).replace('mime_type="video/mp4"', ''))
    for pair in ql_list:
        dict_list.append(pair.split(' '))
    for pair in dict_list[::-1]:
        dictionary[pair[2].replace('res=', '').replace('"', '')] = pair[0].replace(
            'itag=', '').replace('"', '')

    return dictionary


# workaround to have resolution tags in the Video name
def ql_dict(yt):
    ql_list = []
    dict_list = []
    dictionary = {}
    linkfilter = re.compile(r'itag=["\w]+ mime_type="video/mp4" res=["\w]+')
    stream_ls = yt.streams.filter(adaptive=True)
    quality = linkfilter.findall(f'{stream_ls}')
    for ql in quality:
        ql_list.append(str(ql).replace('mime_type="video/mp4"', ''))
    for pair in ql_list:
        dict_list.append(pair.split(' '))
    for pair in dict_list[::-1]:
        dictionary[pair[0].replace('itag=', '').replace('"', '')] = pair[2].replace(
            'res=', '').replace('"', '')

    return dictionary
