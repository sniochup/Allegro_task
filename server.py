from http.server import HTTPServer, BaseHTTPRequestHandler
from sys import argv
import requests
import json


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


class Handler(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header("Content-type", "application/json")
		self.end_headers()

	def do_HEAD(self):
		self._set_headers()

	def do_GET(self):
		self._set_headers()
		user = self.path[1:]
		print(f"User: {user}")
		api_req = request(user)
		# print(api_req)
		self.wfile.write(json.dumps(api_req, indent=4).encode("utf-8"))

	def do_POST(self):
		self._set_headers()
		user = self.rfile.read(int(self.headers['Content-Length'])).decode()
		print(f"User: {user}")
		api_req = request(user)
		# print(api_req)
		self.wfile.write(json.dumps(api_req, indent=4).encode("utf-8"))


def main(PORT=9000):
	HOST = "localhost"
	server_address = (HOST, PORT)
	httpd = HTTPServer(server_address, Handler)
	print(f"Server Starts - {HOST}:{PORT}")
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print(f"Server Stoped - {HOST}:{PORT}")


if __name__ == '__main__':
	if len(argv) == 2:
		main(PORT=int(argv[1]))
	else:
		main()
