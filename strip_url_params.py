def strip_url_params(url, params_to_strip = []):
    if '?' in url:
        baseURL = url.split('?')[0]
        querystring = url.split('?')[1]
        wholeparams = querystring.split('&')
        paramnames = []
        for wholeparam in wholeparams:
            paramname = wholeparam.split('=')[0]
            paramnames.append(paramname)
        newparamnames = []
        newwholeparams = []
        for i in range(len(wholeparams)):
            if (paramnames[i] not in params_to_strip) and (paramnames[i] not in newparamnames):
                newparamnames.append(paramnames[i])
                newwholeparams.append(wholeparams[i])
        newquerystring='?'
        for x in newwholeparams:
            newquerystring += x
            newquerystring += "&"
        newquerystring = newquerystring[:-1]
        return baseURL + newquerystring
    else:
        return url

print(strip_url_params('www.google.com?a=1&b=2&b=2',['a']))
