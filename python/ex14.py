from sys import argv

script, user_name, user_from = argv
prompt = '> '

print "Hi %s from %s, I'm the %s script" % (user_name, user_from, script)
print "I'd like to ask you a few questions."
print "Do you like me %s from %s?" % (user_name, user_from)
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
