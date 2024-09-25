import requests
import beautifulsoup

url = "https://www.google.com/search?sca_esv=253929064fe52cf4&sca_upv=1&sxsrf=ADLYWIIpigKCQBrg3_cr2CT1kYELL3f2Kg:1727227687663&q=python&udm=2&fbs=AEQNm0AaBOazvTRM_Uafu9eNJJzCxsFAN9ghZeJg62vyKsfSNG5tuTU7rKoiWdpt4Wcr80sJ7RkUqfqCa3lF9LpI36rAO7M6OXoApbhEamWRfxDiS3mCsbtmKhJtXGycdio0jBA-YmakY6Wva1PjEUBJIpjRba2v6UJA0gUjU3NGjJk9Uru6KEqgX7fezOblGtG2pjmzd0RI&sa=X&ved=2ahUKEwiZy5PG-NyIAxWGi68BHRG3BlYQtKgLegQIERAB&biw=1478&bih=713&dpr=1.3"

headers = {
	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

print(response.text)