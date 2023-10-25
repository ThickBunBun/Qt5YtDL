import re


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
    for pair in dict_list:
        dictionary[pair[0].replace('itag=', '').replace('"', '')] = pair[2].replace(
            'res=', '').replace('"', '')

    return dictionary
