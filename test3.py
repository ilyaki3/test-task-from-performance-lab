import json


with open('values.json', 'r', encoding='utf-8') as v:
	values = json.load(v)

with open('tests.json', 'r', encoding='utf-8') as t:
	tests = json.load(t)


def exchange(value_id):
	for value in values['values']:
		if value['id'] == value_id:
			return value['value']


def entry(some_list):
	if isinstance(some_list, list):
		for i in range(len(some_list)):
			entry(some_list[i])
	else:
		if 'value' in some_list:
			value_id = some_list['id']
			some_list['value'] = exchange(value_id)

		if 'values' in some_list:
			entry(some_list['values'])
	return tests


report = entry(tests['tests'])


with open('report.json', 'w', encoding='utf-8') as r:
	json.dump(report, r, sort_keys=True, indent=4, ensure_ascii=False)
