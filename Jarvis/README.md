
# Jarvis AI

**Jarvis AI** is a voice-activated virtual assistant built using Python. It can perform a variety of tasks, including fetching information, playing music, telling jokes, opening applications, and more. Inspired by the fictional AI assistant from Iron Man, this project showcases the capabilities of integrating voice recognition, natural language processing, and automation.
## Features

- Voice Commands: Responds to user input through voice recognition.
- Music Playback: Plays specific songs based on user requests from predefined links.
- Web Search: Opens websites or searches the web using voice commands.
- Wikipedia Integration: Fetches summaries of topics from Wikipedia.
- Jokes: Tells random jokes for entertainment.
- System Automation: Includes features like shutting down the system, checking battery status, and more.
- Date and Time: Tells the current date and time.
## Requirements 

- Python 3.x
 
- Required libraries:
  ```bash
   pip install speechrecognition pyttsx3 wikipedia pyjokes pyautogui psutil pyaudio
## How it works:

 1. Voice Input: Jarvis listens to your voice command using the speech_recognition library.
2. Task Execution: Based on the input, Jarvis performs tasks like opening a browser, playing a song, or fetching information.
3. Response: Provides audio feedback using pyttsx3 to confirm or interact with the user.
## Installation

1. Clone this repository:
  ```bash
git clone <repository-link>
cd jarvis-ai
 ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the training script:
   ```bash
   python jarvis.py

## Music Commands
Here are some predefined music commands and their corresponding songs:
  
- **stealth**: [Listen on YouTube](https://www.youtube.com/watch?v=U47Tr9BB_wE)  
- **march**: [Listen on YouTube](https://www.youtube.com/watch?v=Xqeq4b5u_Xw)  
- **skyfall**: [Listen on YouTube](https://www.youtube.com/watch?v=DeumyOzKqgI&pp=ygUHc2t5ZmFsbA%3D%3D)  
- **wolf**: [Listen on YouTube](https://www.youtube.com/watch?v=ThCH0U6aJpU&list=PLnrGi_-oOR6wm0Vi-1OsiLiV5ePSPs9oF&index=21)  

## Future enhancements

- Custom Music Library: Add functionality to play songs from the user’s local storage.
- Natural Language Processing: Enhance the assistant’s ability to understand complex commands.
- GUI Integration: Create a graphical interface for better user interaction.
## Acknowledgements

This project was inspired by the fictional Jarvis AI from *Iron Man*. Special thanks to the developers of the Python libraries used in this project.
