# learngermanwithsongs
Ranking German songs according to their difficulty.

The code in this repository is a tool that can help German learners to find simple songs to learn German with. The ranking used is based on the average difficulty of the words used measured by their frequency. To capture the frequency the following source was used:

Institut für Deutsche Sprache (2014): Korpusbasierte
Wortformenliste DeReWo, DeReKo-2014-II-MainArchive-STT.100000,
https://www.ids-mannheim.de/digspra/kl/projekte/methoden/derewo/, Institut für Deutsche Sprache,
Programmbereich Korpuslinguistik, Mannheim, Deutschland

which is found in the file wordfreq.tsv. More information about the source in the wordfreq.readme file.

# 99 Songs ranked
I have used the code to rank some songs according to the difficulty of their vocabulary from easy to difficult:
1. Echt by Glasperlenspiel
1. Die immer lacht by Stereoact feat. Kerstin Ott
1. Mein Herz by Beatrice Egli
1. Applaus!! Applaus!! by Sportfreunde Stiller
1. Liebe ist meine Rebellion by Frida Gold
1. Wolke 4 by Philipp Dittberner & Marv
1. Millionen Lichter by Christina Stürmer
1. Nur in meinem Kopf by Andreas Bourani
1. So wie du warst by Unheilig
1. Auf uns by Andreas Bourani
1. Ich lass für dich das Licht an by Revolverheld
1. Herz über Kopf by Joris
1. Tage wie diese by Die Toten Hosen
1. Chöre by Mark Foster
1. 80 Millionen by Max Giesinger
1. Lass uns gehen by Revolverheld
1. Altes Fieber by Die Toten Hosen
1. Übermorgen by Mark Foster
1. Wovon sollen wir träumen by Frida Gold
1. Da Da Da ich lieb dich nicht du liebst mich nicht aha aha aha by Trio
1. Auf anderen Wegen by Andreas Bourani
1. M+F by Die Ärzte
1. Wie schön du bist by Sarah Connor
1. Ist da jemand by Adel Tawil
1. Liebe by Sido
1. Cello (MTV Unplugged) by Udo Lindenberg feat. Clueso
1. Hulapalu by Andreas Gabalier
1. Bei meiner Seele by Xavier Naidoo
1. Wohin willst du by Gestört aber GeiL feat. Lea
1. Deutschland by Rammstein
1. Du by Cro
1. Boot by Apache 207
1. Atemlos durch die Nacht by Helene Fischer
1. Herzbeben by Helene Fischer
1. 110 by Capital Bra x Samra & Lea
1. Leiser by LEA
1. Vincent by Sarah Connor
1. Halt dich an mir fest by Revolverheld feat. Marta Jandová
1. 200 km/h by Apache 207
1. Wir sind am Leben by Rosenstolz
1. Lieblingsmensch by Namika
1. Au revoir by Mark Foster feat. Sido
1. Geiles Leben by Glasperlenspiel
1. Wir sind gross by Mark Foster
1. Einmal um die Welt by Cro
1. Wolke 10 by Mero
1. Easy by Cro
1. Lieder by Adel Tawil
1. Was du Liebe nennst by Bausa
1. Flash mich by Mark Foster
1. Tamam Tamam by Summer Cem
1. Vermissen by Juju feat. Henning May
1. Zusammen by Die Fantastischen Vier feat. Clueso
1. 500 PS by Bonez MC & RAF Camora
1. Traum by Cro
1. Nur noch kurz die Welt retten by Tim Bendzko
1. Benzema by Capital Bra
1. Stimme by EFF
1. Strobo Pop by Die Atzen mit Nena
1. Sowieso by Mark Foster
1. Roller by Apache 207
1. Astronaut by Sido feat. Andreas Bourani
1. Amoi seg' ma uns wieder by Andreas Gabalier
1. Unter meiner Haut by Gestört aber GeiL & Koby Funk feat. Wincent Weiss
1. Je ne parle pas français by Namika feat. Black M
1. Magisch by Olexesh feat. Edin
1. Lila Wolken by Marteria / Yasha / Miss Platnum
1. Fame by Apache 207
1. Casanova by Summer Cem & Bausa
1. Cherry Lady by Capital Bra
1. So wie du bist by MoTrip feat. Lary
1. Unterwegs by KitschKrieg feat. Jamule
1. Bilder im Kopf by Sido
1. Schau nicht mehr zurück by Xavas
1. Kein Wort by Juju x Loredana
1. Bläulich by Apache 207
1. Von allein by Culcha Candela
1. Bye Bye by Cro
1. Ohne mein Team by Bonez MC & RAF Camora feat. Maxwell
1. Holz by 257ers
1. Heute mit mir by Nimo
1. Unendlichkeit by Cro
1. One Night Stand by Capital Bra
1. Berlin City Girl by Culcha Candela
1. Whatever by Cro
1. Palmen aus Plastik by Bonez MC & RAF Camora
1. Neymar by Capital Bra feat. Ufo361
1. Leider geil (leider geil) by Deichkind
1. Wieder Lila by Samra & Capital Bra
1. In meinem Benz by AK Ausserkontrolle x Bonez MC
1. Melodien by Capital Bra feat. Juju
1. Prinzessa by Capital Bra
1. Primo by RAF Camora
1. Ahnma by Beginner feat. Gzuz & Gentleman
1. Holland by 257ers
1. Bück dich hoch by Deichkind
1. Ein Antrag auf Erteilung eines Antragformulars by Reinhard Mey
1. Augenbling by Seeed
1. Nummer 1 by Zuna feat. Azet & Noizy!

# How to make your own ranking?
1. Download the repository
2. Install the software listed in requirements.txt
2. Run /model/initialise.py
3. Input song title, Artist, and Lyrics of the songs you are interested in into the /data/input.xlsx file.
4. Run /model/model.py
5. Checkout the results in /model/results.xlsx - the higher the score, the easier the vocab!
