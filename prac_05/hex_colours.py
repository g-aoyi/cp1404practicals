"""
CP1404/CP5632 Practical
Hex Colours
"""

COLOR_TO_HEX = {
    "absolutezero": "#0048ba",
    "acidgreen": "#b0bf1a",
    "aliceblue": "#f0f8ff",
    "alizarincrimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "antiquewhite": "#faebd7",
    "antiquewhite1": "#ffefdb",
    "antiquewhite2": "#eedfcc"
}

color = input("Enter color name: ").lower()
while color != "":
    if color in COLOR_TO_HEX:
        print(f"{color.title()} is {COLOR_TO_HEX[color]}")
    else:
        print("Invalid color")
    color = input("Enter color name: ").lower()
