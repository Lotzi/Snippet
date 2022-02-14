# EP - Finder
import sys
import time

import lichesspy.api
import lichesspy.pgn
from lichesspy.format import PYCHESS

# sys
start_time = time.time()

# Erzeuge Liste mit En Passant Zügen
ep_white = ["hxg6"]
ep_black = ["hxg3"]
for white in range(97, 104):
    ep_white.append(chr(white)+"x"+chr(white+1)+"6")
    if chr(white) != "a":
        ep_white.append(chr(white)+"x"+chr(white-1)+"6")
for black in range(97, 104):
    ep_black.append(chr(black)+"x"+chr(black+1)+"3")
    if chr(black) != "a":
        ep_black.append(chr(black)+"x"+chr(black-1)+"3")

# Read File Line for Line
out = open('mygames.txt', 'r').readlines()

# Load Token from File
data = []
for line in out:
    data.append(line.split(",")[0])

# load and test PGN Data
flag = False
for i in range(len(data)):
    pgn = lichesspy.pgn.from_game(
        lichesspy.api.game(str(data[i]), with_moves=1))
    if "[ECO '']" not in pgn:
        # Test white
        for ep in ep_white:
            # Pre Test White
            if ep in pgn and ep[2]+"5" in pgn:
                pos_pgn = pgn.find(ep)
                pos_pre = pgn.find(ep[2]+"5")
                if pos_pgn - pos_pre <= 10:
                    # UI White
                    print("Game:"+str(i)+",status:true,color:white,token:"+str(data[i])+",Diff:"+str(pos_pgn - pos_pre))
                    flag = True
            for ep in ep_black:
                # Pre Test Black
                if ep in pgn and ep[2]+"4" in pgn:
                    pos_pgn = pgn.find(ep)
                    pos_pre = pgn.find(ep[2]+"4")
                    print(pos_pgn,pos_pre)
                    if pos_pgn - pos_pre <= 10:
                        # UI Black
                        print("Game:"+str(i)+",status:true,color:black,token:"+str(data[i])+",Diff:"+str(pos_pgn - pos_pre))
                        flag = True
        if not flag:
            print("Game:"+str(i)+",status:false")
        else:
            flag = False


# Exit
print("--- %s seconds ---" % (time.time() - start_time))
print("END")
sys.exit(0)
