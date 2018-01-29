import configparser

# The main process for maeve.  Does the listening loop to give you something like "Hey Siri" or "Ok Google"
# then subs out to a child process to record the actual command, tries to figure out what to do, calls
# another subfunction to execute that command, and provide contextual feedback to the user

# THIS IS VERY DIY.  No warranty expressed or implied per the license.  

# Get the configuration
config = configparser.ConfigParser()
config.sections()
[]
config.read('maeve.ini')
