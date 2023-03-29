import os

dossiersEtape = ['test', 'train', 'validation']
dossiersEmotion = ['angry', 'fearful', 'happy', 'sad', 'surprised']

nbImage = 0
totalEmotions = {}

for emotion in dossiersEmotion:
    totalEmotions[emotion] = 0

for etape in dossiersEtape:
    nbEtape = 0
    print(etape + ' :')
    for emotion in dossiersEmotion:
        nbLocal = 0
        folder_path = 'emotion_images/' + etape + '/' + emotion
        for filename in os.listdir(folder_path):
            nbLocal += 1
        totalEmotions[emotion] += nbLocal
        
        print('  - ' + emotion + ' : ' + str(nbLocal))
        nbEtape += nbLocal
    print('  => Total ' + etape + ' : ' + str(nbEtape) + '\n')
    nbImage += nbEtape


print("Total :")
for emotion, count in totalEmotions.items():
    proportions = []
    for etape in dossiersEtape:
        folder_path = 'emotion_images/' + etape + '/' + emotion
        nbLocal = len(os.listdir(folder_path))
        proportion = (nbLocal / count) * 100
        proportions.append("{:.2f}".format(proportion) + '%')
    print("- " + emotion + " : " + str(count) + " (" + ", ".join(proportions) + ")")

print('Total images BD : ' + str(nbImage))

