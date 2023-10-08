import speech_recognition
import pyttsx3
from datetime import date, datetime
import python_weather
import asyncio
import os
import string

hear = speech_recognition.Recognizer()
KKZ_think = ""
user = "User"
zodiac = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
Zodiac = "Unknown"

Aries = "Element: Fire\nPolarity: Positive\nQuality: Cardinal\nRuling Planet: Mars\nRuling House: First\nSpirit Color: Red\nLucky Gem: Diamond\nFlower: Thistle & honeysuckle\nTop Love Matches: Sagittarius"
Taurus = "Element: Earth\nPolarity: Negative\nQuality: Fixed\nRuling Planet: Venus\nRuling House: Second\nSpirit Color: Pink\nLucky Gem: Emerald\nFlower: Rose, Poppy, & Foxglove\nTop Love Matches: Cancer & Virgo"
Gemini = "Element: Air\nPolarity: Positive\nQuality: Mutable\nRuling Planet: Mercury\nRuling House: Third\nSpirit Color: Yellow\nLucky Gem: Tiger's Eye & Emerald\nFlower: Lavender & Lily of the Valley\nTop Love Matches: Aries & Leo"
Cancer = "Element: Water\nPolarity: Negative\nQuality: Cardinal\nRuling Planet: Moon\nRuling House: Fourth\nSpirit Color: Violet\nLucky Gem: Ruby, pearl\nFlower: Orchid and white rose\nTop Love Matches: Taurus & Pisces"
Leo = "Element: Fire\nPolarity: Positive\nQuality: Fixed\nRuling Planet: Sun\nRuling House: Fifth\nSpirit Color: Gold\nLucky Gem: Carnelian\nFlower: Sunflower & marigold\nTop Love Matches: Libra"
Virgo = "Element: Earth\nPolarity: Negative\nQuality: Mutable\nRuling Planet: Mercury\nRuling House: Sixth\nSpirit Color: Silver\nLucky Gem: Peridot\nFlower: Sunflower & marigold\nTop Love Matches: Cancer"
Libra = "Element: Air\nPolarity: Positive\nQuality: Cardinal\nRuling Planet: Venus\n\nRuling House: Seventh\nSpirit Color: Blue\nLucky Gem: Sapphire\nFlower: Rose\nTop Love Matches: Gemini"
Scorpio = "Element: Water\nPolarity: Negative\nQuality: Fixed\nRuling Planet: Pluto, Mars\nRuling House: Eighth\nSpirit Color: Black\nLucky Gem: Topaz & opal\nFlower: Hibiscus & geraniums\nTop Love Matches: Cancer"
Sagittarius = "Element: Fire\nPolarity: Positive\nQuality: Mutable\nRuling Planet: Jupiter\n\nRuling House: Ninth\nSpirit Color: Light Blue\nLucky Gem: Topaz\nFlower: Carnations & crocuses\nTop Love Matches: Aries"
Capricorn = "Element: Earth\nPolarity: Negative\nQuality: Cardinal\nRuling Planet: Saturn\nRuling House: Tenth\nSpirit Color: Dark blue\nLucky Gem: Lapis lazuli\nFlower: Pansy\nTop Love Matches: Virgo"
Aquarius = "Element: Air\nPolarity: Positive\nQuality: Fixed\nRuling Planet: Uranus\nRuling House: Eleventh\nSpirit Color: Sky blue\nLucky Gem: Amethyst\nFlower: Orchid\nTop Love Matches: Sagittarius"
Pisces = "Element: Water\nPolarity: Negative\nQuality: Mutable\nRuling Planet: Neptune\nRuling House: Twelfth\nSpirit Color: Sea green\nLucky Gem: Moonstone\nFlower: Water lily\nTop Love Matches: Virgo"

Z = [Aries,Taurus,Gemini,Cancer,Leo,Virgo,Libra,Scorpio,Sagittarius,Capricorn,Aquarius,Pisces]






def speak(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def first_split(forcast):
    return forcast.split(" ")
def second_split(A):
    return A.split("=")
def extra_split(A):
    return A.split(".")
def remove_symbol1(kind):
    for char in string.punctuation:
        kind = kind.replace('>','')
    return kind
def remove_symbol2(overal):
    for char in string.punctuation:
        overal = overal.replace(char,'')
    return overal
 
while True:
    
    print("I am listening")
    try:

        with speech_recognition.Microphone() as UserVoiceInputSource:

            hear.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)

            # The Program listens to the user voice input.
            UserVoiceInput = hear.listen(UserVoiceInputSource)

            KKZ_think = hear.recognize_google(UserVoiceInput)
            KKZ_think = KKZ_think.lower()
            
    
    except KeyboardInterrupt:
        print("Interupt by keyboard")
        break
    
    except speech_recognition.UnknownValueError:
        KKZ_think = ""
    
    print(user,":",KKZ_think)
    print("KKZ:...")
    
    if "hello" in KKZ_think:
        command = "Hi, How are you today"        
        print("KKZ: Hi!!!\nKKZ: How are you today?")
    
    elif "your name" in KKZ_think:
        command = ("Hi, I am K K Z")
        print("Hi, I am KKZ")
    
    elif "fine" in KKZ_think or "good" in KKZ_think:
        command = "Me too. what can I help you. I can tell your zodiac, would you like to hear "
        print("Me, too. What can I help you?\nKKZ: I can tell your zodiac, would you like to hear")
        speak(command)
        
        print("I am listening")
        try:

            with speech_recognition.Microphone() as UserVoiceInputSource:

                hear.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)

                # The Program listens to the user voice input.
                UserVoiceInput = hear.listen(UserVoiceInputSource)

                KKZ_think = hear.recognize_google(UserVoiceInput)
                KKZ_think = KKZ_think.lower()
                
        
        except KeyboardInterrupt:
            print("Interupt by keyboard")
            break
        
        except speech_recognition.UnknownValueError:
            KKZ_think = ""
        
        print(user,":",KKZ_think)
        print("KKZ:...")
        
        if "yes" in KKZ_think:
            command = "First, I need to know some of your information"
            speak(command)
            command = "Please type your name here"
            speak(command)
            user = str(input("Please type your name here:\nuser: "))
            command = "Thank you, now please type your date of birth"
            speak(command)
            date_of_birth = input("Please enter your date of birth here(MM/DD/YY)\nuser: ")
            date_of_birth = date_of_birth.split('/')
            date_of_birth[0] = int(date_of_birth[1])
            date_of_birth[1] = int(date_of_birth[0])
            command = "thank you, please wait for a second for processing"
            print("KKZ: Thank you\nKKZ: Processing...")
            speak(command)
            if date_of_birth[1] == 3:
                if date_of_birth[0] >= 21:
                    Zodiac = zodiac[0]
                else: 
                    Zodiac = zodiac[11]
            elif date_of_birth[1] == 4:
                if date_of_birth[0] >= 21:
                    Zodiac = zodiac[1]
                else:
                    Zodiac = zodiac[0]
            elif date_of_birth[1] == 5:
                if date_of_birth[0] >= 21:
                    Zodiac = zodiac[2]
                else:
                    Zodiac = zodiac[1]
            elif date_of_birth[1] == 6:
                if date_of_birth[0] >= 22:
                    Zodiac = zodiac[3]
                else:
                    Zodiac = zodiac[2]
            elif date_of_birth[1] == 7:
                if date_of_birth[0] >= 23:
                    Zodiac = zodiac[4]
                else:
                    Zodiac = zodiac[3]
            elif date_of_birth[1] == 8:
                if date_of_birth[0] >= 23:
                    Zodiac = zodiac[5]
                else:
                    Zodiac = zodiac[4]
            elif date_of_birth[1] == 9:
                if date_of_birth[0] >= 23:
                    Zodiac = zodiac[6]
                else:
                    Zodiac = zodiac[5]
            elif date_of_birth[1] == 10:
                if date_of_birth[0] >= 24:
                    Zodiac = zodiac[7]
                else:
                    Zodiac = zodiac[6]
            elif date_of_birth[1] == 11:
                if date_of_birth[0] >= 23:
                    Zodiac = zodiac[8]
                else:
                    Zodiac =zodiac[7]
            elif date_of_birth[1] == 12:
                if date_of_birth[0] >= 22:
                    Zodiac = zodiac[9]
                else:
                    Zodiac = zodiac[8]
            elif date_of_birth[1] == 1:
                if date_of_birth[0] >= 20:
                    Zodiac = zodiac[10]
                else:
                    Zodiac = zodiac[9]
            elif date_of_birth[1] == 2:
                if date_of_birth[0] >= 19:
                    Zodiac = zodiac[11]
                else:
                    Zodiac = zodiac[10]
            command = "Your zodiac sign is:" + Zodiac
            print("KKZ: Your zodiac sign is",Zodiac)
            speak(command) 
            command = "Say More information for more information about your Zodiac"
            speak(command)
        elif KKZ_think == "no":
            command = "Okey, then feel free to ask me if there is anything else I can help you"
            print("KKZ: OK")
            command = "I can tell you today's date, weather and time"
            print("KKZ: Date?\n     Time?\n     Weather?")
            speak(command)
        
    elif "more" in KKZ_think and "information" in KKZ_think:
        for i in range(11):
            if i == zodiac.index(Zodiac):
                print(Z[i])
    
    elif "what" in KKZ_think and "date" in KKZ_think and "today" in KKZ_think:
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        command = "today is"+ d2
        speak(command)
        print("KKZ: Today is: ",d2)
        
    elif "what" in KKZ_think and "time" in KKZ_think:
        now = datetime.now()
        current_time = now.strftime("%H hour(s), %M minute(s), %S second(s)")
        command = "current time is" + current_time
        speak(command)
        print("KKZ: Current time is: ",current_time)
        
    elif "what" in KKZ_think and "weather" in KKZ_think:
        async def getweather():
            async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
                weather = await client.get('New York')
                
                for forecast in weather.forecasts:
                    for hourly in forecast.hourly:
                        A = f' --> {hourly!r}'
                        A = first_split(A)
                        for i in range(-1,-4,-1):
                            A[i] = second_split(A[i])
                        kind = A[-1]
                        kind = kind[-1]
                        kind = extra_split(kind)
                        kind = kind[-1]
                        kind = remove_symbol1(kind)
                        overal = A[-2]
                        overal = overal[-1]
                        overal = remove_symbol2(overal)
                        temperature = A[-3]
                        temperature = temperature[-1]    
                        break
                    break
                command = "for the next hour, the weather will be"+overal+"it will be"+overal+"and the temperature is going to be"+temperature
                speak(command)
                print("KKZ: +Overal:",overal,"\n     +Kind:",kind,"\n     +Temperature:",temperature)

        if __name__ == '__main__':
            if os.name == 'nt':
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
            asyncio.run(getweather())
                            
    elif KKZ_think == "":
        command = "Sorry I don't understand"
        print("KKZ: Sorry, I don't understand")
        
    elif "bye" in KKZ_think:
        command = "Have a nice day"
        print("KKZ: Have a nice day!")
        speak(command)
        break
    if "fine" in KKZ_think or "good" in KKZ_think:
        continue
    else:
        speak(command)