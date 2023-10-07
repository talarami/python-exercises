"""

Here is a snippet of Lionel Richie’s song “All Night Long (All Night)”

"Well, my friends, the time has come
To raise the roof and have some fun
Throw away the work to be done
Let the music play on (play on, play on, play on...)
Everybody sing, everybody dance
Lose yourself in wild romance
We're going to Party, Karamu, Fiesta, forever
Come on and sing along!
All night long (all night), All night (all night)
All night long (all night), All night (all night)
All night long (all night), All night (all night)
All night long! (all night), Ooh, yeah (all night)
People dancing all in the street
See the rhythm all in their feet
Life is good, wild and sweet
Let the music play on...(Play on, play on, play on...)
Feel it in your heart and feel it in your soul
Let the music take control
We're going to Party, Liming, Fiesta, forever
Come on and sing along
We're going to Party, Liming, Fiesta, forever
Come on and sing my song!"

Tasks:
1. Write the lyrics to a new file called song.txt
2. Read in the file and print out ONLY lines that have the word ‘sing’ in them.

"""
from datetime import datetime


fileName = datetime.now().strftime("%d-%m-%Y-%H-%M-%S") +".txt"

lyrics = """
"Well, my friends, the time has come
To raise the roof and have some fun
Throw away the work to be done
Let the music play on (play on, play on, play on...)
Everybody sing, everybody dance
Lose yourself in wild romance
We're going to Party, Karamu, Fiesta, forever
Come on and sing along!
All night long (all night), All night (all night)
All night long (all night), All night (all night)
All night long (all night), All night (all night)
All night long! (all night), Ooh, yeah (all night)
People dancing all in the street
See the rhythm all in their feet
Life is good, wild and sweet
Let the music play on...(Play on, play on, play on...)
Feel it in your heart and feel it in your soul
Let the music take control
We're going to Party, Liming, Fiesta, forever
Come on and sing along
We're going to Party, Liming, Fiesta, forever
Come on and sing my song!"
"""
file = open(fileName, "a")
file.writelines("\n")
file.writelines(lyrics)

with open (fileName, "r") as file:
    for line in file:
        if "sing" in line:
            print(line.strip())

file.close()

