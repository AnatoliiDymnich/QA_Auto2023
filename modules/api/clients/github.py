import requests


class Github:
    def get_user_defunkt(self):
        r = requests.get("https://api.github.com/users/defunkt")
        body = r.json()

        return body
