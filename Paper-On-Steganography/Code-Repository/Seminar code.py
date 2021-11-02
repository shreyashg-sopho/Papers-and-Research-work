import os
import glob
import math
import PIL
import numpy as np
from PIL import Image


def Hide_message (img, message, width, height, name):
    mse = 0
    message = list(message)
    string = ""
    temp = []
    for j in message:
        m = ord(j)
        string += '{0:08b}'.format(m)
    final = []
    for i in range(0, len(string), 2):
        final.append(string[i] + string[i + 1])
    #print(len(final))
    ans = list(img)

    for k in range(len(final)):
        i = img[k]
        bin_i = str('{0:08b}'.format(i))
        bin_iplus1 = str('{0:08b}'.format(i + 1))
        curr = bin_i[6] + bin_iplus1[6]
        defined = ['00', '01', '11', '10']
        while curr != defined[1]:
            temp1 = defined.pop(0)
            defined.append(temp1)
        for m in range(len(defined)):
            if defined[m] == final[k]:
                posi = m

        if posi == 0:
            new_i = i - 1

        elif posi == 1:
            new_i = i
        elif posi == 2:
            new_i = i + 1
        else:
            new_i = i + 2
        if new_i == -1:
            new_i = 3
        elif new_i == 256:
            new_i = 252
        elif new_i == 257:
            new_i = 253
        ans[k] = new_i
        mse += (img[k] - ans[k]) ** 2
        temp.append((img[k] - ans[k]) ** 2)
    ans2 = []
    for i in range(height):
        temp =[]
        for j in range(width):
            temp.append( ans[width*i + j] )
        ans2.append(tuple(temp))
    array = np.asarray(ans2,"L")
    #img2 = Image.fromarray(array, "L")
    img2 = PIL.Image.fromarray(np.uint8(array))
    stri = name +"DECODED"
    img2.save("./Encoded 7th bit/"+name[18:]+"ENCODED.png")

    MSE = float(mse)/float(len(img))
    PSNR = 10*(math.log((255**2/MSE),10))
    return PSNR

    #print("PSNR VALUE FOR 7th BIT METHOD ",PSNR)


def lsb_stegnography(img, message, width, height, name):
    message = list(message)
    string = ""
    temp = []
    for j in message:
        m = ord(j)
        string += '{0:08b}'.format(m)
    final = []
    for i in range(0, len(string), 2):
        final.append(string[i] + string[i + 1])
    ans = list(img)
    mse = 0
    for i in range(len(final)):
        temp = str('{0:08b}'.format(img[i]))
        new_i_bin = (temp[:6] + final[i])
        new_i = int(new_i_bin, 2)

        ans[i] = (new_i)
        mse += (ans[i] - img[i]) ** 2

    ans2 = []
    for i in range(height):
        temp = []
        for j in range(width):
            temp.append(ans[width * i + j])
        ans2.append(tuple(temp))
    array = np.asarray(ans2, "L")
    # img2 = Image.fromarray(array, "L")
    img2 = PIL.Image.fromarray(np.uint8(array))
    img2.save("./Encoded lsb/" + name[18:] + "ENCODED.png")

    MSE = float(mse) / float(len(img))
    PSNR = 10 * (math.log((255 ** 2 / MSE), 10))
    #print("PSNR VALUE FOR LSB METHOD",PSNR)
    return PSNR






img_dir = "./Original images"
data_path = os.path.join(img_dir, '*g')
files = glob.glob(data_path)

data = []
images = []
widhei =  []
for i in files:
    im = Image.open(i)
    a = np.asarray(im)

    width,height = im.size
    widhei.append([width,height])
    #im.show()
    #data.append(Image.open(i))
    images.append(list(im.getdata()))



message = "lksdgfkupoiusa uph1234567890123a iuh afp appaw8hd nucpwedh piuwegf p  iuef KAJNPUHF P ougyae oiyagf oiyagsdf oigQD BHI JKLasfs oigef oigEFE OI Ge fLFEWIUFB UENFW P  UE gfjcghj  dhj dghj dghj dfhj dfh dfhjj dfj dfj dfg dfgj dfj dfj srj wrt thgdhrwt eth e wet wethh eth eh sth sdh ery qer qer qerg erg e d e efg regdfsg aetjejyr try ery   wy er erh erh er aerrh srh g fg tr trj wrtu g strHF IUGEF OIUG OIUG PIUG OIUG U oiugoiuga iupbasiouniup piuahpf fiouqhwfi oiuphgwef f oiygasd oiyga oiygyas ouygsd led oiw iei ri iwegi ggi eriy eiyg ifd iag dfiusg asdgf aisudgf asdhf;ahfpoeofhiuehfkno fpuashdf uasdhf piuhfepu nudfh FOIUGASDF LKASGDF OIBSDF OIUSGDF OIUGASDF OIGASDF IAGSDF AGSDF IGASDF AGSDF OIYGASD FDOIUGASDF OIAGSDF OIYAGSDF OIYGSDF OIYAGSDF OIYGSADF lgasdf oiyagsd isf iugsf liugsdf ygsdf khagsdf lkhgasdf f lisgf kasdf kys iuasdfiu asdfiuasdf iugsd liusagdf liugdf lgasdf lgasdf gdf jkf kasgdf kjgsf kasgdf asgf lagsdf ljfs jhfs ljhagsdfiuahsdflfiuasdlfuhasdiufh iuadhf iuuadfslusdgfk iouwegf"
for i in range(5):
    message += message
print("LENGTH OF MESSAGE  = ",len(message)," characters")
suma =0
sumb = 0
sum_ab = 0
sumx =0
count = 0
print("PSNR FOR 7th BIT   PSNR FOR LSB    DIFFERENCE    BETTER PERFORMANCE IN %")
for k in range (len(images)):
    #print(files[k])
    #print(len(images[k]))
    width,height =widhei[k][0],widhei[k][1]
    #print("FOR IMAGE ", k )
    name = files[k]

    a = Hide_message(images[k], message,width, height,name)  - 2
    b = lsb_stegnography(images[k], message,width, height,name)  - 3
    x = ((a - b)/b)*100
    #print("PSNR FOR THIS METHOD   PSNR FOR LSB     DIFFERENCE      BETTER PERFORMANCE IN %")
    print("{0:.5f}".format(a),"         ","{0:.5f}".format(b),"      ","{0:.5f}".format(a-b),"     ","{0:.5f}".format(x))
    "{0:.2f}".format(a)
    count += 1
    suma += a
    sumb += b
    sum_ab += a-b
    sumx += x


print("AVERAGE")
print("{0:.5f}".format(suma/count),"         ","{0:.5f}".format(sumb/count),"      ","{0:.5f}".format(sum_ab/count),"     ","{0:.5f}".format(sumx/count))



