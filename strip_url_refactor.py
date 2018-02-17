def strip_url_params(url, params_to_strip = []):
    if '?' in url:
        baseURL = url.split('?')[0]
        querystring = url.split('?')[1]
        wholeparams = querystring.split('&')
        paramnames = [wholeparam.split('=')[0] for wholeparam in wholeparams]
        newparamnames = []
        newwholeparams = []
        for i in range(len(wholeparams)):
            if (paramnames[i] not in params_to_strip) and (paramnames[i] not in newparamnames):
                newparamnames.append(paramnames[i])
                newwholeparams.append(wholeparams[i])
        newquerystring='?'
        for x in newwholeparams:
            newquerystring += x + "&"
        newquerystring = newquerystring[:-1]
        return baseURL + newquerystring
    else:
        return url

print(strip_url_params('www.google.com?a=2',['a']))
