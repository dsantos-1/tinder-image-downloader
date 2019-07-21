# Copyright 2019 Danilo Santos

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse, json, os, requests

headers={
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
	'X-Auth-Token': '',
	'app-version': '1020358',
	'platform': 'web'
}

teasers_url='https://api.gotinder.com/v2/fast-match/teasers'
photos_dir_name='Unblurred Tinder Photos'

parser=argparse.ArgumentParser(description='Downloads the unblurred photos of the users that liked your Tinder profile.')
parser.add_argument('X_Auth_Token', help='Your X-Auth-Token. To learn how to get your X-Auth-Token, follow the instructions detailed at the README.md file')
args=parser.parse_args()

headers['X-Auth-Token']=args.X_Auth_Token
get_r=requests.get(teasers_url, headers=headers)

# Check if the request has succeeded
if(get_r.status_code!=200):
	exit('[!] GET failed. The status code is not 200 [%d].\nYour X-Auth-Token is invalid or may have expired.' % get_r.status_code)
else:
	print('[+] Successfully logged in.')

# Parse the page response as JSON
try:
	print('[+] Parsing the page response as JSON... ', end='')
	jr=json.loads(get_r.text)
	print('ok.\n')
except:
	exit('failed.')

# Create the directory in which the photos will be stored
if(not os.path.exists(photos_dir_name)):
	print('[+] Creating "%s" directory... ' % photos_dir_name, end='')
	os.makedirs(photos_dir_name)
	print('ok.')

print('[+] Entering "%s" directory... ' % photos_dir_name, end='')
os.chdir(photos_dir_name)
print('ok.')

# Iterate over the users that liked your profile
for r in jr['data']['results']:
	if(not os.path.exists(r['user']['_id'])):
		print('  [+] Creating "%s" directory... ' % r['user']['_id'], end='')
		os.makedirs(r['user']['_id'])
		print('ok.')
	
	print('  [+] Entering "%s" directory... ' % r['user']['_id'], end='')
	os.chdir(r['user']['_id'])
	print('ok.')
	
	# Iterate over the photos of each user
	for p in r['user']['photos']:
		fname=p['url'].split('/')[-1]
	
		# Download the photos of a user
		if(not os.path.exists(fname)):
			print('    [+] Downloading "%s"... ' % fname, end='', flush=True)
			photo_url=requests.get(p['url'])
			photo_url.raise_for_status()
			open(fname, 'wb').write(photo_url.content)
			print('ok.')
	
	print('  [+] Exiting "%s" directory... ' % r['user']['_id'], end='')
	os.chdir('..')
	print('ok.\n')