'''
Create Python REST client program which queries http://api.open-notify.org/astros.json [api.open-notify.org]
and list the user name in sorted order. Convert the REST JSON object to list<String> with JSON names in sorted order.
'''
import urllib.request, json
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
#print(type(data))
#print(data)
data_list = data.items()
#print(data.keys())
#print(data.values())
my_list_values = (list(data.values()))
abc = my_list_values[0]
#print(abc)
sort_based_on = "name"
pattern = [(dict_[sort_based_on], dict_) for dict_ in abc]
pattern.sort()
result = [dict_ for (key, dict_) in pattern]
print(result)
#print(type(result))
