import os;
import requests;

NAME = "saucerest"
VERSION = "0.0.1"

class SauceRestException(Exception):
    pass

class SauceRest:
    BASE_URL = "https://saucelabs.com/rest"
    USERS_ENDPOINT = "v1/users"

    def __init__(self, username=None, accessKey=None):
        self.set_credentials(username, accessKey)

    def set_credentials(self, username, accessKey):
        self.username = username or os.getenv("SAUCE_USERNAME")
        self.accessKey = accessKey or os.getenv("SAUCE_ACCESS_KEY")
        self.auth = (self.username, self.accessKey)
        if self.username is None:
            raise Exception("username is not set")
        if self.accessKey is None:
            raise Exception("accessKey is not set")
    
    def users_endpoint(self, username=None):
        return f"{self.BASE_URL}/{self.USERS_ENDPOINT}/{username or self.username}"

    def get_user(self, username=None):
        url = self.users_endpoint(username)
        return self.send(url)

    def list_subaccounts(self, username=None):
        url = self.users_endpoint(username) + "/list-subaccounts"
        return self.send(url)

    def get_subaccounts(self, username=None):
        url = self.users_endpoint(username) + "/subaccounts"
        return self.send(url)

    def get_sibling_accounts(self, username=None):
        url = self.users_endpoint(username) + "/siblings"
        return self.send(url)

    def get_concurrency(self, username=None):
        url = self.users_endpoint(username) + "/concurrency"
        return self.send(url)
            
    def change_access_key(self, username=None):
        url = self.users_endpoint(username) + "/accesskey/change"
        return self.send(url, "POST")

    # def create_subaccount(self, user, username=None):
    #     url = self.users_endpoint(username)
    #     print(user)
    #     print(url)
    #     return self.send(url, "POST", user)

    def send(self, url, method="GET", body=None):
        if method is "GET":
            response = requests.get(url, auth=self.auth)
        elif method is "POST":
            response = requests.post(url, json=body, auth=self.auth)
        elif method is "PUT":
            response = requests.put(url, json=body, auth=self.auth)
        elif method is "DELETE":
            response = requests.delete(url, auth=self.auth)
        else:
            raise SauceRestException("unknown request method: " + method)
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    print("sauce rest examples")
    sauce = SauceRest()
    alt_user = "team1-user2"
    print("\nGET USER", sauce.get_user())
    print("\nGET USER", sauce.get_user(alt_user))
    print("\nLIST SUBACCOUNTS", sauce.list_subaccounts())
    print("\nGET SUBACCOUNTS", sauce.get_subaccounts())
    print("\nGET SIBLING ACCOUNTS", sauce.get_sibling_accounts(alt_user))
    print("\nGET CONCURRENCY", sauce.get_concurrency())
    # print("\nCHANGE ACCESS KEY", sauce.change_access_key(alt_user))

    new_user = { 
        "username" : "new-test-username",
        "password" : "new-test-Password",
        "name" : "new-test-name",
        "email" : "new-test-email@saucelabs.com"
    }

    # print("\nCREATE SUBACCOUNT", sauce.create_subaccount(username="team2", user=new_user))
