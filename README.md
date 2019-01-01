# DeepGamingAI_FIFAVA
A voice-assistant for the game of FIFA (windows platform) to control game actions with your voice.

Click the image below to see the project video on YouTube.
<a href="https://www.youtube.com/watch?v=QhDnMHmoadQ" target="_blank"><img src="https://github.com/ChintanTrivedi/DeepGamingAI_FIFAVA/blob/master/fifa_voice_assistant.png" 
alt="YOUTUBE VIDEO" width="800" height="480"  /></a>

# Dependencies
1. Install porcupine keyword detection engine from [this github repo](https://github.com/Picovoice/Porcupine).
2. PyAudio

# How to run
This implementation supports three types of actions:-
1. Game tactics (team mentality)
2. Skill moves
3. Goal celebrations

Run the respective python scripts to enable keyword detection for these actions. Make sure the key combinations in the code match with those within the game.

The commands supported for each are under the `porcupine_res/commands` directory.

# Create custom commands for any game other than FIFA
- Use the porcupine tutorial [here](https://www.youtube.com/watch?v=3z7LBW_Rl9c) to create your own wake words, or use the tutorial [here](https://www.youtube.com/watch?v=YQQ5Bq5HqpQ) to create your custom commands. Place the resultant `.ppn` files under the `porcupine_res/commands` directory and map the key controls in the python scripts with that within the game you are making the voice assistant for.
