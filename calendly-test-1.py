import requests
uri = "https://api.calendly.com/users/me"
access_token = "eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzgzMzQyMTE5LCJqdGkiOiI4NzMyZWMyOC1mNzIzLTQ1ZWMtYmU3ZC01ZmEyY2EwYTZhMGYiLCJ1c2VyX3V1aWQiOiI0NjgyMmJiMi03NDEwLTQ1ODYtYjA3YS1lNzIzNjNkMDI2NmQiLCJzY29wZSI6ImF2YWlsYWJpbGl0eTpyZWFkIGF2YWlsYWJpbGl0eTp3cml0ZSBldmVudF90eXBlczpyZWFkIGV2ZW50X3R5cGVzOndyaXRlIGxvY2F0aW9uczpyZWFkIHJvdXRpbmdfZm9ybXM6cmVhZCBzaGFyZXM6d3JpdGUgc2NoZWR1bGVkX2V2ZW50czpyZWFkIHNjaGVkdWxlZF9ldmVudHM6d3JpdGUgc2NoZWR1bGluZ19saW5rczp3cml0ZSBncm91cHM6cmVhZCBvcmdhbml6YXRpb25zOnJlYWQgb3JnYW5pemF0aW9uczp3cml0ZSB1c2VyczpyZWFkIGNvbnRhY3RzOnJlYWQgY29udGFjdHM6d3JpdGUgYWN0aXZpdHlfbG9nOnJlYWQgZGF0YV9jb21wbGlhbmNlOndyaXRlIG91dGdvaW5nX2NvbW11bmljYXRpb25zOnJlYWQgd2ViaG9va3M6cmVhZCB3ZWJob29rczp3cml0ZSJ9.wHFvgXnTFOI7MUAOILib_VYsJxScF60fnN57ET6_zuFH-iBkp6PKnpv63aR-fg4wR-OXSBbNJioYJl_ZWcYRng"
header = {"authorization": f"Bearer {access_token}"}
response = requests.get(url=uri,headers=header)

json_response = response.json()
#print(json_response.get("resource").get("current_organization"))
# user_name = json_response.get("resource").get("name")
org_id = json_response.get("resource").get("current_organization")
# print(org_id)
##print(response.json().get("resource").get("current_organization"))

#new_uri = "https://api.calendly.com/event_types?organization={org_id}"
new_uri = f"https://api.calendly.com/event_types?organization={org_id}"

response = requests.get(url=new_uri,headers=header)
print(response.json())
