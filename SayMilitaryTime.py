import sys
from gtts import gTTS
from preferredsoundplayer import soundplay

def convert_hours(hours):
    if hours == 0:
        return "Zero"
    elif hours == 1:
        return "Zero One"
    elif hours == 2:
        return "Zero Two"
    elif hours == 3:
        return "Zero Three"
    elif hours == 4:
        return "Zero Four"
    elif hours == 5:
        return "Zero Five"
    elif hours == 6:
        return "Zero Six"
    elif hours == 7:
        return "Zero Seven"
    elif hours == 8:
        return "Zero Eight"
    elif hours == 9:
        return "Zero Nine"
    elif hours == 10:
        return "Ten"
    elif hours == 11:
        return "Eleven"
    elif hours == 12:
        return "Twelve"
    elif hours == 13:
        return "Thirteen"
    elif hours == 14:
        return "Fourteen"
    elif hours == 15:
        return "Fifteen"
    elif hours == 16:
        return "Sixteen"
    elif hours == 17:
        return "Seventeen"
    elif hours == 18:
        return "Eighteen"
    elif hours == 19:
        return "Nineteen"
    elif hours == 20:
        return "Twenty"
    elif hours == 21:
        return "Twenty One"
    elif hours == 22:
        return "Twenty Two"
    elif hours == 23:
        return "Twenty Three"

def convert_minutes(minutes):
    if minutes == 0:
        return "Zero"
    elif minutes == 1:
        return "One"
    elif minutes == 2:
        return "Two"
    elif minutes == 3:
        return "Three"
    elif minutes == 4:
        return "Four"
    elif minutes == 5:
        return "Five"
    elif minutes == 6:
        return "Six"
    elif minutes == 7:
        return "Seven"
    elif minutes == 8:
        return "Eight"
    elif minutes == 9:
        return "Nine"
    elif minutes == 10:
        return "Ten"
    elif minutes == 11:
        return "Eleven"
    elif minutes == 12:
        return "Twelve"
    elif minutes == 13:
        return "Thirteen"
    elif minutes == 14:
        return "Fourteen"
    elif minutes == 15:
        return "Fifteen"
    elif minutes == 16:
        return "Sixteen"
    elif minutes == 17:
        return "Seventeen"
    elif minutes == 18:
        return "Eighteen"
    elif minutes == 19:
        return "Nineteen"
    elif minutes == 20:
        return "Twenty"
    elif minutes == 21:
        return "Twenty One"
    elif minutes == 22:
        return "Twenty Two"
    elif minutes == 23:
        return "Twenty Three"
    elif minutes == 24:
        return "Twenty Four"
    elif minutes == 25:
        return "Twenty Five"
    elif minutes == 26:
        return "Twenty Six"
    elif minutes == 27:
        return "Twenty Seven"
    elif minutes == 28:
        return "Twenty Eight"
    elif minutes == 29:
        return "Twenty Nine"
    elif minutes == 30:
        return "Thirty"
    elif minutes == 31:
        return "Thirty One"
    elif minutes == 32:
        return "Thirty Two"
    elif minutes == 33:
        return "Thirty Three"
    elif minutes == 34:
        return "Thirty Four"
    elif minutes == 35:
        return "Thirty Five"
    elif minutes == 36:
        return "Thirty Six"
    elif minutes == 37:
        return "Thirty Seven"
    elif minutes == 38:
        return "Thirty Eight"
    elif minutes == 39:
        return "Thirty Nine"
    elif minutes == 40:
        return "Forty"
    elif minutes == 41:
        return "Forty One"
    elif minutes == 42:
        return "Forty Two"
    elif minutes == 43:
        return "Forty Three"
    elif minutes == 44:
        return "Forty Four"
    elif minutes == 45:
        return "Forty Five"
    elif minutes == 46:
        return "Forty Six"
    elif minutes == 47:
        return "Forty Seven"
    elif minutes == 48:
        return "Forty Eight"
    elif minutes == 49:
        return "Forty Nine"
    elif minutes == 50:
        return "Fifty"
    elif minutes == 51:
        return "Fifty One"
    elif minutes == 52:
        return "Fifty Two"
    elif minutes == 53:
        return "Fifty Three"
    elif minutes == 54:
        return "Fifty Four"
    elif minutes == 55:
        return "Fifty Five"
    elif minutes == 56:
        return "Fifty Six"
    elif minutes == 57:
        return "Fifty Seven"
    elif minutes == 58:
        return "Fifty Eight"
    elif minutes == 59:
        return "Fifty Nine"

def main():
    #Check for proper number of command line inputs (should be 1 or 2)
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print("Please provide appropriate number of inputs")
        sys.exit()
        
        military_time = sys.argv[1]

    #Check for "integer" military time by converting String to Integer using int() function
    try:
        mtime = int(military_time)
    except:
        print("Invalid 1st command line argument. Should contain only digits.")
        sys.exit()

    #Check for positive or zero military time
    if mtime < 0:
        print("Invalid 1st command line argument. Should be a zero or positive value.")
        sys.exit()

    #Convert military time to hours and minutes
    hours = mtime//100
    minutes = mtime%100

    #Check for hours between 0 and 23
    if hours > 23:
        print("Invalid 1st command line argument. Hours should be between 0 and 23.")
        sys.exit()

    #Check for minutes between 0 and 59
    if minutes > 59:
        print("Invalid 1st command line argument. Minutes should be between 0 and 59.")
        sys.exit()

    if len(sys.argv) == 3:
        accent = sys.argv[2].upper()
    else:  
        accent = "USA"

    #Check for valid "accent" if provide
    if accent not in ["IND", "AUS", "USA"]:
        print("Invalid 2nd command line argument. Should be IND, AUS, or USA.")
        sys.exit()

    hour_words = convert_hours(hours)
    minute_words = convert_minutes(minutes)
    final_words = hour_words + " Hundred " + minute_words + " Hours"
    print(final_words)

    #Produce audio file using gTTS function
    if accent == "AUS":
        audio = gTTS(final_words, lang='en', tld="com.au")
        audio.save("f.mp3")
    elif accent == "IND":
        audio = gTTS(final_words, lang='en', tld="com.in")
        audio.save("f.mp3")
    else:
        audio = gTTS(final_words, lang='en')
        audio.save("f.mp3")

    #Play file
    soundplay("./f.mp3")

main()