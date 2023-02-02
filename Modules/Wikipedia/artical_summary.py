import wikipedia

result = wikipedia.search("facebook", results = 5)
print(result)
# ............................................................

wikipedia.set_lang("hi")
print(wikipedia.summary("India"))