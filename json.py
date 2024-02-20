import json

data = '{"name": "Andryan Zulfi"},"Age":17, "Hobby": ["NgeBokep"],\
    "FavSong": {"NF": "Happy","Keenan Te": "Mne","The Weeknd": "StarBoy", "Sawn Mendes": "Imagination"},'

json_data = json.loads(data)
print(type(json_data))