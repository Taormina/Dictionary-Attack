import urllib, sys, os, string

# sys.argv[1] is the domain
# sys.argv[2] is the relative path name of cewl.rb
# sys.argv[3...] previously existing password list(s) -- preferably unmutated
# if sys.argv[-1] is -m, perform mutations on the password list

# diggity the website's name
page = urllib.urlopen(sys.argv[1]) # for verification
print "Site verified."
if sys.argv[-1] == "-m":
	m = True
	sys.argv = sys.argv[:-1]
	print "Mutations enabled."
else:
	m = False
	print "Mutations disabled."
print "cewl beginning."
os.system("./" + sys.argv[2] + " " + sys.argv[1] + " -d 1 -w tmp.txt") # fires off the cewl
print "cewl finished."
cmd = "cat tmp.txt "
for x in range(4,len(sys.argv)):
	cmd += sys.argv[x] + " "
os.system(cmd + "> pass.txt")
print "cat finished."
if m: # perform mutations
	print "Mutations started."
	f = open("pass.txt","r") 
	words = f.readlines()
	f.close()
	print "File read."
	print str(len(words)) + " words from scrapping."
	out = words[:]
	"Numbers appended."
	for word in words:
		for num in (range(0,100) + range(1900,2015)):
			out += [word[:-1] + str(num) + "\n"]
	words = out[:]
	print str(len(words)) + " words from first round mutations."
	for word in out:
		words += [string.upper(word)]
		words += [string.capitalize(word)]
	print str(len(words)) + " words from second round mutations."
	print "Writing to file."
	f = open("pass.txt","w")
	for x in words:
		f.write(x)
print "Done."
