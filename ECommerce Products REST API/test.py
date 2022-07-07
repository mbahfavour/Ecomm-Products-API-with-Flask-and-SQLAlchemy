import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name": "Rayban Glasses", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
         "image": "https://images.unsplash.com/photo-1619089662078-7fda3fdec77a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8c3BlY3RhY2xlc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60", 
         "category": "Designers","price": 2500},
    {"name": "Gucci", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "image": "https://images.unsplash.com/photo-1486670082170-b54a98edda89?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fHNwZWN0YWNsZXN8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60", 
        "category": "Designers","price": 3000},
    {"name": "Louis Vuitton", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "image": "https://images.unsplash.com/photo-1488203602058-8db2ce840718?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OXx8c3BlY3RhY2xlc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "category": "Designers","price": 3500},
    {"name": "YSL250",  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
         "image": "https://images.unsplash.com/photo-1610308932928-27697fde87de?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fHNwZWN0YWNsZXN8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
         "category": "Designers", "price": 20000},
    {"name": "SL20",  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
         "image": "https://images.unsplash.com/photo-1619089662706-11b2f8542913?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTd8fHNwZWN0YWNsZXN8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
         "category": "Optical", "price": 2100},
    {"name": "BAando35",  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
         "image": "https://images.unsplash.com/photo-1456081101716-74e616ab23d8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8c3BlY3RhY2xlc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
         "category": "Designers", "price": 25000},
    {"name": "SL50",  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
         "image": "https://images.unsplash.com/photo-1517948430535-1e2469d314fe?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8c3BlY3RhY2xlc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "category": "Optical Frames", "price": 30000},
    {"name": "BAando50",  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
         "image": "https://images.unsplash.com/photo-1603578119639-798b8413d8d7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8c3BlY3RhY2xlc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "category": "Optical Frames", "price": 2860},
    {"name": "SL25",  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
         "image": "https://images.unsplash.com/photo-1577400983943-874919eca6ce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8c3BlY3RhY2xlc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "category": "Regular", "price": 5000},
    {"name": "SL250",  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
         "image": "https://images.unsplash.com/photo-1483412468200-72182dbbc544?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8c3BlY3RhY2xlc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
         "category": "Regular", "price": 270000}
        ]

# for i in range(len(data)):
#     response = requests.post(BASE + "products/" + str(i), data[i])
#     print(response.json())
# input()


response = requests.delete(BASE + "products/2")
print(response)
