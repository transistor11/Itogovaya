import requests

def isAlchemist():
    res = requests.get("https://kitsu.io/api/edge/anime?filter[text]=fullmetall")
    return "alchemist".encode() in res.content

def isPiece():
    res = requests.get("https://kitsu.io/api/edge/anime?filter[text]=one")
    return "piece".encode() in res.content

def isCastle():
    res = requests.get("https://kitsu.io/api/edge/anime?filter[text]=moving")
    return "castle".encode() in res.content

def isAssassination():
    res = requests.get("https://kitsu.io/api/edge/anime?filter[text]=classroom")
    return "assassination".encode() in res.content

def isUltimate():
    res = requests.get("https://kitsu.io/api/edge/anime?filter[text]=collider")
    return "ultimate".encode() in res.content

print("Is Alchemist?", isAlchemist())
print("Is Piece?", isPiece())
print("Is Castle?", isCastle())
print("Is Assassination?", isAssassination())
print("Is Ultimate?", isUltimate())
