import json

# get information from followers file
with open('followers.json') as f:  
    follower = json.load(f) 

# get information from following file
with open('following.json') as g:  
    following = json.load(g) 

followers_list = []
following_list = []

for i in follower['relationships_followers']:
  followers_list.append(i['string_list_data'][0]['value'])

for i in following['relationships_following']:
  following_list.append(i['string_list_data'][0]['value'])

followers_list.sort()
following_list.sort()


print(len(followers_list), len(following_list))

please_unfollow = []

for _ in range(len(following_list)):
    if following_list[_] not in followers_list:
        please_unfollow.append(following_list[_])

for _ in range(len(please_unfollow)):
  print(please_unfollow[_])
exit()
for _ in range(len(please_unfollow)):
  curr = check(please_unfollow[_])
  print(curr)
  if ',' in curr:
    curr = curr.replace(',', '')
  elif 'K' in curr:
    please_unfollow[_] = 'official_account'
    continue
  elif 'M' in curr:
    please_unfollow[_] = 'official_account'
    continue

# Check if user is "official" aka a professional account adjust if needed.
  if int(curr) >= 2000:
    please_unfollow[_] = 'official_account'
  print(curr)

# remove all occurences of 'official_account' in please_unfollow
while 'official_account' in please_unfollow:
  please_unfollow.remove('official_account')

print(please_unfollow)

