import json
import requests

def get_numeric_fbid(request):
    fbid=request['graphql']['user']['fbid']
    return fbid

def main():
    username=str(input('Enter Username:'))
    req=requests.get(f'https://www.instagram.com/{username}/?__a=1&__d=dis')
    request=req.json()
   # print(request,type(request))
   # formatted_json = json.dumps(request, indent=2)
    try:

        fbid=get_numeric_fbid(request)
        print(fbid)
    except KeyError:
        print(request['message'])

if __name__=="__main__":
    main()


