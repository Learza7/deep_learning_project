import os

dossiersEtape = ['test','train','validation']
dossiersEmotion = ['angry','fearful','happy','sad','surprised']

nbImage = 0
for etape in dossiersEtape:
    nbEtape = 0
    print(etape + ' :')
    for emotion in dossiersEmotion:
        nbLocal = 0
        folder_path = 'emotion_images/' + etape + '/' + emotion
        for filename in os.listdir(folder_path):
            nbLocal += 1
        print('  - ' + emotion + ' : ' + str(nbLocal))
        nbEtape += nbLocal
    print('  => Total ' + etape + ' : ' + str(nbEtape) + '\n')
    nbImage += nbEtape
print('Total images BD : ' + str(nbImage))