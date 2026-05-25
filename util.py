# -*- coding: utf-8 -*-
import sys
import time

def print_animated(text):
    for char in text:
        if char == "\n":
            time.sleep(1)
        if char == ",":
            time.sleep(0.5)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def parse_choice(raw):
    raw = raw.strip().lower()

    if raw in ["yes", "y", "ok", "sure", "closer"]:
        return "yes"
    if raw in ["no", "n", "stop"]:
        return "no"
    if raw in ["wait", "later", "idk", "i dont know", "dont know", "i don't know", "don't know"]:
        return "wait"
    if raw in ["touch", "reach"]:
        return "touch"

    return "unknown"

def parse_emotion(raw):
    raw = raw.strip().lower()

    if raw in ["happy", "good", "great", "awesome", "fun", "excited", "joy", "close", "romantic", "connected", "yay", "loving"]:
        return "positive"
    if raw in ["sad", "lonely", "stop", "angry", "mad", "bad", "hate", "unhappy", "no", "frustrated", "down", "cold", "tired"]:
        return "negative"
    if raw in ["ok", "later", "maybe", "fine", "so-so", "average", "meh"]:
        return "neutral"

    return "unknown"

def progress_bar(label, seconds):
    sys.stdout.write("\n" + label + " ")
    sys.stdout.flush()

    steps = 20
    delay = float(seconds) / steps

    for i in range(steps):
        sys.stdout.write("#")
        sys.stdout.flush()
        time.sleep(delay)