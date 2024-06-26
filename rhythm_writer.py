import random

#major keys
a_key=["in the Key of A", "A", "Bm", "C#m", "D", "E", "F#m"]
c_key=["in the key of C", "C", "Dm", "Em", "F", "G", "Am"]
d_key=["in the Key of D", "D", "Em", "F#m", "G", "A", "Bm"]
g_key=["in the Key of G", "G", "Am", "Bm", "C", "D", "Em"]

#common progressions
prog1=[0,1,5,6,4]
prog2=[0,6,4,1,5]
prog3=[0,1,4,5,4]
prog4=[0,1,6,4,5]
prog5=[0,2,5,1,6]

strum_patterns=["DuDuDD", "DDu uDu", "DDDuDu", "DDuDDu", "DDDuD"]

key_list=[a_key, d_key, g_key]
prog_list=[prog1, prog2, prog3, prog4, prog5]

print("__________          __  .__               __      __        .__  __                 ")
print("\______   \___.__._/  |_|  |__   _____   /  \    /  \_______|__|/  |_  ___________  ")
print(" |       _<   |  |\   __\  |  \ /     \  \   \/\/   /\_  __ \  \   __\/ __ \_  __ \ ")
print(" |    |    \\___  | |  | |   Y  \  Y Y  \  \        /  |  | \/  ||  | \  ___/|  | \/ ")
print(" |____|_  // ____| |__| |___|  /__|_|  /   \__/\  /   |__|  |__||__|  \___  >__|    ")
print("        \/ \/                \/      \/         \/                        \/        ")


print("Welcome to Rythm Writer, made by Trish, 2021")

BPM = random.randint(75,140)

key =  random.choice(key_list)
progression = random.choice(prog_list)
strum = random.choice(strum_patterns)

print("Today's Chords are:")
print(key[progression[1]] + " " + key[progression[2]] + " " + key[progression[3]] + " " + key[progression[4]])
print("Try this strumming pattern: " + str(strum))    
print("Play this chord progression, which is " + str(key[0]) + ", at " + str(BPM) + " BPM using a metronome")



