from CommandPackages import WordPlay, Math, Multiply, Help
from LanguagePackages import AsciiArt, Commie, Speach

PackageDict = {
  "Math": Math.Math(),
  "WordPlay":WordPlay.WordPlay(),
  "Multiply":Multiply.Multiply(),
  "AsciiArt":AsciiArt.Art(),
  "Help":Help.Help(),
  "About":Help.About(),
  
}

LanguageCatch = {
  "lol":Speach.Lol(),
  "fuck":Speach.Fuck(),
  "Commie":Commie.CPP(),
}