import requests


def request(user):
	repos = {}
	page_num = 1
	stargazers_counter = 0
	repos_number = 0

	while True:
		response = requests.get(f'https://api.github.com/users/{user}/repos?page={page_num}&per_page=100')
		# print(response.json())

		try:
			if not response.json():
				break
			i = 0
			for i in range(len(response.json())):
				repos[response.json()[i]['name']] = {'stargazers_count': response.json()[i]['stargazers_count']}
				stargazers_counter += response.json()[i]['stargazers_count']
			repos_number += i + 1
			if i < 99:
				break

		except KeyError:
			if response.json()['message'] == 'Not Found':
				return {'user': user, 'message': 'User Not Found'}
			if response.json()['message'][:23] == 'API rate limit exceeded':
				return {'user': user, 'message': 'API rate limit exceeded'}

		page_num += 1

	print(f"Pages number:   {page_num}")
	print(f"Repos number:   {repos_number}")
	print(f"Stargazers sum: {stargazers_counter}")

	return {'user': user, 'repositories': repos, 'stargazers_sum': stargazers_counter}


print(request("sniochup"))
