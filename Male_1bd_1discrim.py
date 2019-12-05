from __future__ import division
import numpy
import random
import timeit
import sys

def maleharm_kin_bud(pat, G, mf, mm, mut, name):
    newfile = open(str(name) + ".txt", "a")
    start = timeit.default_timer()
    femaleadult = [[[0, 0, 0, 0, 0, 0, j] for i in range(3)] for j in range(pat)]
    maleadult = [[[0, 0, 0, 0, 0, 0, j] for i in range(3)] for j in range(pat)]
    Logger2 = [0 for i in range(G)]
    Logger1 = [0 for i in range(G)]
    Logger0 = [0 for i in range(G)]

    for g in range(G):
        FecPatch1 = [0 for i in range(pat)]
        FecMales = [[0 for i in range(3)] for j in range(pat)]
        maleharm = [[0 for i in range(3)] for j in range(pat)]
        femalejuv = [[[0, 0, 0, 0, 0, 0, j] for i in range(3)] for j in range(pat)]
        femalejuv1 = [[[0, 0, 0, 0, 0, 0, j] for i in range(3)] for j in range(pat)]
        femalejuv2 = []
        malejuv = [[[0, 0, 0, 0, 0, 0, j] for i in range(3)] for j in range(pat)]
        malejuv1 = [[[0, 0, 0, 0, 0, 0, j] for i in range(3)] for j in range(pat)]
        malejuv2 = []
        femaleadult0 = [[[0, 0, 0, 0, 0, 0, j] for i in range(3)] for j in range(pat)]
        maleadult0 = [[[0, 0, 0, 0, 0, 0, j] for i in range(3)] for j in range(pat)]
        ticklogger2 = 0
        ticklogger1 = 0
        ticklogger0 = 0

        for y in range(pat):
            if maleadult[y][0][6] == maleadult[y][1][6] == maleadult[y][2][6]:
                for x in range(3):
                    maleharm[y][x] = maleadult[y][x][0] + maleadult[y][x][1]
                    FecMales[y][x] = 1 + (maleharm[y][x]**(1/2))
                FecPatch1[y] = 1 - numpy.mean(maleharm[y])
            elif maleadult[y][0][6] != maleadult[y][1][6] != maleadult[y][2][6]:
                for x in range(3):
                    maleharm[y][x] = maleadult[y][x][4] + maleadult[y][x][5]
                    FecMales[y][x] = 1 + (maleharm[y][x]**(1/2))
                FecPatch1[y] = 1 - numpy.mean(maleharm[y])
            else:
                if maleadult[y][0][6] == maleadult[y][1][6] and maleadult[y][0][6] != maleadult[y][2][6]:
                    maleharm[y][0] = maleadult[y][0][2] + maleadult[y][0][3]
                    maleharm[y][1] = maleadult[y][1][2] + maleadult[y][1][3]
                    maleharm[y][2] = maleadult[y][2][4] + maleadult[y][2][5]
                elif maleadult[y][0][6] == maleadult[y][2][6] and maleadult[y][0][6] != maleadult[y][1][6]:
                    maleharm[y][0] = maleadult[y][0][2] + maleadult[y][0][3]
                    maleharm[y][1] = maleadult[y][1][4] + maleadult[y][1][5]
                    maleharm[y][2] = maleadult[y][2][2] + maleadult[y][2][3]
                elif maleadult[y][1][6] == maleadult[y][2][6] and maleadult[y][1][6] != maleadult[y][0][6]:
                    maleharm[y][0] = maleadult[y][0][4] + maleadult[y][0][5]
                    maleharm[y][1] = maleadult[y][1][2] + maleadult[y][1][3]
                    maleharm[y][2] = maleadult[y][2][2] + maleadult[y][2][3]
                else:
                    sys.exit("Error message")
                for x in range(3):
                    FecMales[y][x] = 1 + (maleharm[y][x]**(1/2))
                FecPatch1[y] = 1 - numpy.mean(maleharm[y])
        FecPatch = [0 if i < 0 else i for i in FecPatch1]
        FecPop = numpy.mean(FecPatch)
        FecCalc = numpy.ndarray.tolist((numpy.array(FecPatch))/FecPop)
        for y in range(pat):
            z = numpy.random.choice(pat, p=numpy.ndarray.tolist(numpy.array(FecCalc)/sum(FecCalc)))
            while z == y:
                z = numpy.random.choice(pat, p=numpy.ndarray.tolist(numpy.array(FecCalc)/sum(FecCalc)))
            for x in range(3):
                femalejuv[y][x][6] = z
                f = random.randrange(3)
                m = numpy.random.choice(3, p=numpy.ndarray.tolist(numpy.array(FecMales[z])/sum(FecMales[z])))
                if random.random() < 0.5:
                    if random.random() < mut:
                        femalejuv[y][x][0] = femaleadult[z][f][0] + random.uniform(-0.01, 0.01)
                    else:
                        femalejuv[y][x][0] = femaleadult[z][f][0]
                else:
                    if random.random() < mut:
                        femalejuv[y][x][0] = femaleadult[z][f][1] + random.uniform(-0.01, 0.01)
                    else:
                        femalejuv[y][x][0] = femaleadult[z][f][1]
                if random.random() < 0.5:
                    if random.random() < mut:
                        femalejuv[y][x][1] = maleadult[z][m][0] + random.uniform(-0.01, 0.01)
                    else:
                        femalejuv[y][x][1] = maleadult[z][m][0]
                else:
                    if random.random() < mut:
                        femalejuv[y][x][1] = maleadult[z][m][1] + random.uniform(-0.01, 0.01)
                    else:
                        femalejuv[y][x][1] = maleadult[z][m][1]
                if random.random() < 0.5:
                    if random.random() < mut:
                        femalejuv[y][x][2] = femaleadult[z][f][2] + random.uniform(-0.01, 0.01)
                    else:
                        femalejuv[y][x][2] = femaleadult[z][f][2]
                else:
                    if random.random() < mut:
                        femalejuv[y][x][2] = femaleadult[z][f][3] + random.uniform(-0.01, 0.01)
                    else:
                        femalejuv[y][x][2] = femaleadult[z][f][3]
                if random.random() < 0.5:
                    if random.random() < mut:
                        femalejuv[y][x][3] = maleadult[z][m][2] + random.uniform(-0.01, 0.01)
                    else:
                        femalejuv[y][x][3] = maleadult[z][m][2]
                else:
                    if random.random() < mut:
                        femalejuv[y][x][3] = maleadult[z][m][3] + random.uniform(-0.01, 0.01)
                    else:
                        femalejuv[y][x][3] = maleadult[z][m][3]
                if random.random() < 0.5:
                    if random.random() < mut:
                        femalejuv[y][x][4] = femaleadult[z][f][4] + random.uniform(-0.01, 0.01)
                    else:
                        femalejuv[y][x][4] = femaleadult[z][f][4]
                else:
                    if random.random() < mut:
                        femalejuv[y][x][4] = femaleadult[z][f][5] + random.uniform(-0.01, 0.01)
                    else:
                        femalejuv[y][x][4] = femaleadult[z][f][5]
                if random.random() < 0.5:
                    if random.random() < mut:
                        femalejuv[y][x][5] = maleadult[z][m][4] + random.uniform(-0.01, 0.01)
                    else:
                        femalejuv[y][x][5] = maleadult[z][m][4]
                else:
                    if random.random() < mut:
                        femalejuv[y][x][5] = maleadult[z][m][5] + random.uniform(-0.01, 0.01)
                    else:
                        femalejuv[y][x][5] = maleadult[z][m][5]
            for x in range(3):
                malejuv[y][x][6] = z
                f = random.randrange(3)
                m = numpy.random.choice(3, p=numpy.ndarray.tolist(numpy.array(FecMales[z])/sum(FecMales[z])))
                if random.random() < 0.5:
                    if random.random() < mut:
                        malejuv[y][x][0] = femaleadult[z][f][0] + random.uniform(-0.01, 0.01)
                    else:
                        malejuv[y][x][0] = femaleadult[z][f][0]
                else:
                    if random.random() < mut:
                        malejuv[y][x][0] = femaleadult[z][f][1] + random.uniform(-0.01, 0.01)
                    else:
                        malejuv[y][x][0] = femaleadult[z][f][1]
                if random.random() < 0.5:
                    if random.random() < mut:
                        malejuv[y][x][1] = maleadult[z][m][0] + random.uniform(-0.01, 0.01)
                    else:
                        malejuv[y][x][1] = maleadult[z][m][0]
                else:
                    if random.random() < mut:
                        malejuv[y][x][1] = maleadult[z][m][1] + random.uniform(-0.01, 0.01)
                    else:
                        malejuv[y][x][1] = maleadult[z][m][1]
                if random.random() < 0.5:
                    if random.random() < mut:
                        malejuv[y][x][2] = femaleadult[z][f][2] + random.uniform(-0.01, 0.01)
                    else:
                        malejuv[y][x][2] = femaleadult[z][f][2]
                else:
                    if random.random() < mut:
                        malejuv[y][x][2] = femaleadult[z][f][3] + random.uniform(-0.01, 0.01)
                    else:
                        malejuv[y][x][2] = femaleadult[z][f][3]
                if random.random() < 0.5:
                    if random.random() < mut:
                        malejuv[y][x][3] = maleadult[z][m][2] + random.uniform(-0.01, 0.01)
                    else:
                        malejuv[y][x][3] = maleadult[z][m][2]
                else:
                    if random.random() < mut:
                        malejuv[y][x][3] = maleadult[z][m][3] + random.uniform(-0.01, 0.01)
                    else:
                        malejuv[y][x][3] = maleadult[z][m][3]
                if random.random() < 0.5:
                    if random.random() < mut:
                        malejuv[y][x][4] = femaleadult[z][f][4] + random.uniform(-0.01, 0.01)
                    else:
                        malejuv[y][x][4] = femaleadult[z][f][4]
                else:
                    if random.random() < mut:
                        malejuv[y][x][4] = femaleadult[z][f][5] + random.uniform(-0.01, 0.01)
                    else:
                        malejuv[y][x][4] = femaleadult[z][f][5]
                if random.random() < 0.5:
                    if random.random() < mut:
                        malejuv[y][x][5] = maleadult[z][m][4] + random.uniform(-0.01, 0.01)
                    else:
                        malejuv[y][x][5] = maleadult[z][m][4]
                else:
                    if random.random() < mut:
                        malejuv[y][x][5] = maleadult[z][m][5] + random.uniform(-0.01, 0.01)
                    else:
                        malejuv[y][x][5] = maleadult[z][m][5]
        for y in range(pat):
            for x in range(3):
                femalejuv1[y][x] = [i for i in femalejuv[y][x]]
                malejuv1[y][x] = [i for i in malejuv[y][x]]
                if random.random() < mf:
                    femalejuv1[y][x] = "Empty"
                    femalejuv2.append(femalejuv[y][x])
                else:
                    pass
                if random.random() < mm:
                    malejuv1[y][x] = "Empty"
                    malejuv2.append(malejuv[y][x])
                else:
                    pass
        random.shuffle(femalejuv2)
        random.shuffle(malejuv2)
        for y in range(pat):
            for x in range(3):
                femaleadult0[y][x] = femalejuv2.pop() if femalejuv1[y][x] == "Empty" else femalejuv[y][x]
                maleadult0[y][x] = malejuv2.pop() if malejuv1[y][x] == "Empty" else malejuv[y][x]
                femaleadult[y][x] = [i if i > 0 else 0 for i in femaleadult0[y][x]]
                maleadult[y][x] = [i if i > 0 else 0 for i in maleadult0[y][x]]
                ticklogger2 += femaleadult[y][x][0] + femaleadult[y][x][1] + maleadult[y][x][0] + maleadult[y][x][1]
                ticklogger1 += femaleadult[y][x][2] + femaleadult[y][x][3] + maleadult[y][x][2] + maleadult[y][x][3]
                ticklogger0 += femaleadult[y][x][4] + femaleadult[y][x][5] + maleadult[y][x][4] + maleadult[y][x][5]
        Logger2[g] = ticklogger2 / (pat * 3 * 2)
        Logger1[g] = ticklogger1 / (pat * 3 * 2)
        Logger0[g] = ticklogger0 / (pat * 3 * 2)
        newfile.write(str([g, Logger2[g], Logger1[g], Logger0[g]]))
        newfile.write("," + '\n')
    newfile.close()
    stop = timeit.default_timer()
    print(numpy.mean(Logger2[G-1000:G-1]), numpy.mean(Logger1[G-1000:G-1]), numpy.mean(Logger0[G-1000:G-1]), mm, mf)
    print(stop - start)


maleharm_kin_bud(4000, 50000, 1, 0.2, 0.01, "pointf1m20_harm_1bd")
maleharm_kin_bud(4000, 50000, 1, 0.4, 0.01, "pointf1m40_harm_1bd")
maleharm_kin_bud(4000, 50000, 1, 0.6, 0.01, "pointf1m60_harm_1bd")
maleharm_kin_bud(4000, 50000, 1, 0.8, 0.01, "pointf1m80_harm_1bd")
