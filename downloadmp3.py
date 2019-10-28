import urllib.request

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

def downloadMp3(name, note):
	url='https://virtualpiano.net/wp-content/themes/twentyfourteen-child/newnotes/' + name + '.mp3'
	print(url)
	local='notes/' + note + '.mp3'
	urllib.request.urlretrieve(url,local)

fopen = open('blacks')
notesWhite = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
notesBlack = ['C#', 'D#', 'F#', 'G#', 'A#']
s = fopen.readline();
s = s.split()
octave = 1
curNotes = notesBlack
note = 0
for i in s:
	#print(i)
	if i[:5] == 'id="b':
		print(i)
		downloadMp3(i[4:-2], str(octave) + 'o' + curNotes[note])
		note += 1
		if note == len(curNotes):
			note = 0
			octave += 1