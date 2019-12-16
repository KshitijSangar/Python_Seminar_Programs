"""
1. Import Package
2. Implement Functionality
3. Save File as Audio File
4. Open File
"""

import os
import gtts

Mytext = "chutiya ruturaj"
Myfile = gtts.gTTS(text = Mytext, lang='en', slow=False)


Myfile.save("MyAudio.mp3")
os.system("MyAudio.mp3")