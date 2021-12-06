import matplotlib.pyplot as pyp
import razl

def color(messege):
    res = razl.dvazl(messege)
    for a in range(32):
        for b in range(32):
            if (res[a][b] > 90):
                print(str(res[a][b]) + ' - столько сочетаний букв ' + chr(a + 1072) + chr(b + 1072))

    pyp.imshow(res)
    pyp.show()