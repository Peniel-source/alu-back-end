#!/usr/bin/python3
"""
Does nothinig
"""
import requests
import sys

if __name__ == "__main__":

	employeeId=sys.argv[1]


	url = f"https://jsonplaceholder.typicode.com/users/{employeeId}"

	response = requests.get(url)

	data= response.json()

	username = data['name']
	# print(username)


	todo_url = f'https://jsonplaceholder.typicode.com/todos'
	paramas = { "userId" : f"{employeeId}" }
	r = requests.get(todo_url,params=paramas)

	dta = r.json()


	total= len(dta)
	done_tasks = [task for task in dta if task.get('completed')]

	print(f'Employee {username} is done with tasks ({len(done_tasks)}/{total}):')

	for title in done_tasks:
    		print(f'\t{title.get("title")}')
