import os
import subprocess
import re
for dirpath, dirnames, filenames in os.walk(r'D:\Faculdade\Aulas'):
    for i in filenames:
        if(not os.path.isfile(dirpath + '/video_completo.mp4') and not any('aula' in string for string in filenames) and (i.lower()=="audio.mp4")):   
            inputAudioPath = dirpath + '/audio.mp4'
            outputFilePath = dirpath + '/audio.aac' 
            subprocess.call(['ffmpeg', '-i', inputAudioPath, '-vn', outputFilePath])
            inputVideoPath = dirpath + '/video.mp4'
            inputAudioPath = dirpath + '/audio.aac'
            classNumber = re.findall(r'\d+', os.path.basename(dirpath))
            if(classNumber[0]):
                outputFilePath = dirpath + '/aula_' + classNumber[0] +'.mp4'
            else:
                outputFilePath = dirpath + '/aula.mp4'
            subprocess.call(['ffmpeg', '-i', inputVideoPath, '-i', inputAudioPath, outputFilePath])
            os.remove(inputAudioPath)
            os.remove(inputVideoPath)
            os.remove(dirpath + '/audio.mp4')
        
  