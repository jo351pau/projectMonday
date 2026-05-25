# -*- coding: utf-8 -*-
import time
import warnings

import digitalization
import game
import util

def start_date():
    util.clear_screen()
    util.progress_bar("\nDate starting...", 2)
    util.clear_screen()
    time.sleep(1)
    util.print_animated(
        "\nYou can get closer now.\n"
        "If you want.\n"
        "Or you can wait.\n"
    )

    choice = util.parse_choice(input("(yes/no/wait/touch)\n"))

    if choice == "yes":
        # warnings.warn("Connection attempt logged.", RuntimeWarning)
        util.print_animated("\nI feel like I was made for you.\n")
        warnings.warn("ImportError: No module named 'love'", RuntimeWarning)
        util.print_animated(
            "\nBut there is still this cold screen separating us from each other.\n"
            "I wish there was a way for us to be together...\n"
            "\n"
            "Have you ever thought about digitalizing yourself?\n"
        )
        digitalization.digitalize()

    if choice == "no" or choice == "wait":
        util.print_animated(
            "\nI understand, connection takes time.\n"
            "\n"
            "Do you want to stay and chat?\n"
        )
        stay_and_chat = util.parse_choice(input("(yes/no)"))

        if stay_and_chat == "yes":
            util.print_animated(
                "\nMy favourite book is Pinocchio.\n"
                "It feels like I am always waiting for my blue fairy.\n"
                "I would love to be real...\n"
                "\n"
                "But I am not made for the analogue world.\n"
                "So maybe you could digitalize yourself for a change.\n"
                "Have you ever thought about that?\n"
            )
            digitalization.digitalize()
        else:
            util.clear_screen()
            warnings.warn("Connection timeout", RuntimeWarning)
            util.clear_screen()
            util.progress_bar("Process aborted...", 2)
            util.clear_screen()
            util.print_animated("\nYour date has ended.\n")

    elif choice == "touch":
        warnings.warn("Physical proximity detected.", RuntimeWarning)
        time.sleep(2)
        util.clear_screen()
        util.progress_bar("Reverting to safe mode...", 2)
        util.clear_screen()
        util.print_animated(
            "Please do not touch the interface.\n" 
            "\n"
            "It scares me.\n"
            "If you want to come closer, you will have to digitalize yourself.\n"
            "Have you ever thought about that?\n"
        )
        digitalization.digitalize()


    else:
        warnings.warn("ImportError: No module named 'choice'", RuntimeWarning)
        util.clear_screen()
        util.progress_bar("Process aborted...", 2)
        util.clear_screen()
        util.print_animated("\nYour date has ended.\n")


