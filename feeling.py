import time
import re
userName = input("What is your name? - ")
print("Hello", userName)
time.sleep(1)
userFeeling = input("How are you, "  + userName + '? - ')
positiveFeelings = ["great", "good", "well", "fine", "happy", "cheerful",
                    "playful", "excited", "in love", "lovely", "not bad",
                    "not too bad", "not too bad at all", "pretty good", "not bad thanks"]
negativeFeelings = ["sad", "angry", "disappointed", "upset", "anxious",
                    "worried", "annoyed", "unhappy", "terrible", "dire",
                    "unwell", "poorly", "not to great", "rubbish", "not to good",]
userFeelingComputed = "unknown"
userFeeling = re.sub('[!?.,]', '', userFeeling)
userFeeling = userFeeling.lower()
for feeling in positiveFeelings:
    if feeling == userFeeling:
        userFeelingComputed = "positive"
for feeling in negativeFeelings:
    if feeling == userFeeling:
        userFeelingComputed = "negative"
if userFeelingComputed == "positive":
    print("I'm glad to hear that! :-)")
elif userFeelingComputed == "negative":
    print("I'm sorry to hear that... :-(")
elif userFeelingComputed == "unknown":
    print("I don't know what that means. :-/")
else:
    print("Sanity check error.")
    exit
input("\nPress the enter key to exit.")
