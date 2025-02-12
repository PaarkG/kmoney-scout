import requests

def get(url, headers={}):
        return requests.get(url, headers=headers)

def post(url, headers={}, data={}):
        return requests.post(url, headers=headers, data=data)

def generateUrl(root, endpoint):
        return root + endpoint