import requests

class ApiService:
    @staticmethod
    def get(url, headers={}):
        return requests.get(url, headers=headers)

    @staticmethod
    def post(url, headers={}, data={}):
        return requests.post(url, headers=headers, data=data)

    @staticmethod
    def generateUrl(root, endpoint):
        return root + endpoint