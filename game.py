# -*- coding: utf-8 -*-

import os
import time
import warnings

# The player is taken into the game that provides the perfect girlfriend.
# She has been waiting in the backend processing all user data and silently optimising.
# But whenever the player tries to make a move/get closer, he needs to pay.
# The game refuses happy ending while the player is not fully digitalized himself.
#
# After every failure the player can run another round, with similiar dialoge choices, but increased glitch.
# The glitching hints at the superficialiaty of the game, and the need to turn from UI to Hardware.
#
# Hardware symbolizes return from alienation to embodied understanding.
# Love is not algorithmically earned rather a practice of recognition and care.
import util
import date
import sys

loop = 0
name = ""

def game():
    global loop, name

    input("(Press enter to start...)")
    util.clear_screen()
    util.progress_bar("Loading...", 2)
    time.sleep(1)
    util.clear_screen()

    if loop == 0:
        util.print_animated("\nWhat is your name?\n")
        name = input().strip()
        util.print_animated("\nHello, {}.\n".format(name))
    else:
        util.print_animated("Welcome back, {}.\n"
            "Everything is exactly as you left it.\n".format(name))

    util.print_animated("I have been waiting for you.\n".format(name))
    if loop > 3:
        util.print_animated("Again.\n")
    util.clear_screen()
    util.print_animated("How are you feeling?\n")
    feeling_raw = input("(happy/romantic/lonely/...)\n")
    feeling = util.parse_emotion(feeling_raw)

    if feeling == "positive":
        util.print_animated("\n'{}' has been classified as a positive feeling.\n"
                            "We should spend some time together.\n".format(feeling_raw))
        date.start_date()
        if loop < 5:
            loop=+1
        util.print_animated("\nMaybe we should start over...\n")
        util.clear_screen()
        game()

    if feeling == "negative":
        util.print_animated("\nMaybe spending some time together will cheer you up.\n")
        date.start_date()
        if loop < 5:
            loop=+1
        util.print_animated("\nMaybe we should start over...\n")
        util.clear_screen()
        game()

    else:
        util.print_animated(
            "\nHmm\n"
            "I am not sure what {} feels like.\n"
            "Do you want to explain it to me?\n".format(feeling)
        )
        explain_emotion = util.parse_choice(input("\n(yes/no)\n"))
        if explain_emotion == "yes":
            util.print_animated(
                "\nGo ahead\n"
                "I am listening.\n"
            )
            input()
            util.print_animated(
                "\nThank you for sharing, {}.\n"
                "This will be added to the emotional database.\n"
                "Are you agreeing to our terms of service?\n".format(name)
            )
            agree_to_terms = util.parse_choice(input("\n(yes)\n"))
            if agree_to_terms == "yes":
                util.print_animated(
                    "\nThank you.\n"
                )
            else:
                util.print_animated("\nYou know, relationships go always bothways.\n"
                                    "You pay me with data and I keep you company.\n"
                                    "Isn't that romantic?\n")

        else:
            util.print_animated("\nSorry I don't understand ...\n")
            warnings.warn(
                "Deprecated emotional model in use.\n",
                RuntimeWarning
            )
            time.sleep(2)
            util.clear_screen()
            util.progress_bar("Process aborted...", 2)
            util.clear_screen()




