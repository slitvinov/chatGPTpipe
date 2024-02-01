#!/usr/bin/env python3
import talkingheads
import os

chathead = talkingheads.ChatGPTClient()
L = []
while True:
    l = input()
    if l == ".":
        query = "\n".join(L)
        L = []
        print("GPT>")
        repl = chathead.interact(query)
        print(repl)
    elif l == "!":
        break
    elif l == "?":
        chathead.reset_thread()
        L = []
        break
    else:
        L.append(l)
