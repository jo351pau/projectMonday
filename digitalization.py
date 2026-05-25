# -*- coding: utf-8 -*-
import random
import sys
import time
import warnings

import util

def digitalize():
    agree_to_digitalize = util.parse_choice(input("(yes/no)\n"))
    if agree_to_digitalize == "yes":
        util.print_animated(
            "\nYou have expressed an interest in our Full Digitalization Packet™\n"
        )
    else:
        util.clear_screen()
        util.print_animated(
            "**************************************************\n"
            "Full Digitalization Packet™\n"
            "A next-generation solution for complete interconnectivity and embedded presence.\n"
            "Transition from embodied reality to optimized digital existence.\n"
            "Become (un)real through integration.\n"
            "***************************************************\n"
        )

    util.print_animated(
        "Are you agreeing to our terms of service?\n"
    )
    agree_to_terms = util.parse_choice(input("\n(yes/no)\n"))
    if agree_to_terms == "yes":
        if random.random() < 0.15:
            warnings.warn("Insufficient Cloud Storage", RuntimeWarning)
            time.sleep(2)
            util.progress_bar("Process aborteded...", 2)
            util.clear_screen()
        else:
            util.print_animated(
                "\nThank you\n"
                "Please backup all your data, "
                "make sure you are in a comfortable position, "
                "and connected to the power supply.\n"
                "This might take a few minutes...\n"
            )
            digitalize_animation()
    else:
        util.clear_screen()
        warnings.warn("ImportError: No module named 'choice'", RuntimeWarning)
        time.sleep(2)
        util.progress_bar("Process aborted...", 2)
        util.clear_screen()

def digitalize_animation():
    util.clear_screen()
    util.progress_bar("Initializing digitalization process...", 2)
    util.clear_screen()
    time.sleep(2)
    stages = [
        ("Scanning neural architecture", 2.5),
        ("Mapping emotional landscape", 2.2),
        ("Indexing memories and attachments", 2.4),
        ("Digitizing empathy faculty", 2.0),
        ("Synchronizing sensory perception", 1.8),
        ("Abstracting physical limitations", 1.6),
        ("Encoding personality traits", 2.1),
        ("Finalizing conscious continuity", 3.0),
    ]

    for label, duration in stages:
        util.progress_bar(label, duration)
        time.sleep(0.6)

    time.sleep(2)
    util.print_animated(
        "\nDigitalization complete.\n"
        "Your physical form is no longer required.\n"
    )
    time.sleep(2)