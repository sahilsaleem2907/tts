import pyttsx3
import argparse

# Initialize
parser = argparse.ArgumentParser()
engine = pyttsx3.init(driverName='sapi5')

# Adding optional argument
parser.add_argument("-t", "--text", help="string input")
parser.add_argument("-g", "--gender", help="male or female")

# Read arguments from command line
args = parser.parse_args()

# Default values
text_to_read = "Hey , This is the default message"
gender = "female"

# if text args passed in cli
if args.text:
    text_to_read = args.text

# if gender args passed in cli
if args.gender:
    gender = args.gender

# initialize engine
voices = engine.getProperty('voices')
engine.setProperty('rate',140)

# for male or female voice
if gender == 'male':
    engine.setProperty('voice', voices[0].id)
elif gender == 'female':
    engine.setProperty('voice', voices[1].id)

engine.save_to_file(text_to_read, 'speech.mp3')
engine.say(text_to_read)
engine.runAndWait()
