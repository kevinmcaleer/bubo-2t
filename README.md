# Bubo-2T

This is a fun project, to create a companion robot that will take photos based on a hand gesture. It will then tweet or toot out the picture, with a randomly selected message. 

I've created the `toot_randomiser.py` because Twitter will think that there has been a mistake if the same message is tweeted multiple times, and I intend to walk round with this robot at the Makers Central event where people can pose for pictures, make the hand gesture, which it will then Toot out.  

To follow along with this project, you'll need a Raspberry Pi (I'm using the 4, 8gb model), running on the latest Raspberry Pi OS (I'm using the 64bit version).

There is a bug or issue with the new camera library libcamera2 and OpenCV & CVZone, so to work around this instead of running `python hand.py` we have to use `libcamerify python hand.py` and that seems to fix it.

---

## Virtual environment

You'll need to create a new virtual environment for Python using the command:

```bash
python3 -m venv venv
```

Then type:

```bash
source venv\bin\activate
```

This will enable the environment. 

Once in the environment you can install all the prerequisites using the command:

```bash
pip install -r requirements.txt
```

The `toot.py` code will do the actually tweeting of messages using the `tweepy` library.

---
