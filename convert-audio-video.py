import os
import subprocess
for dirpath, dirnames, filenames in os.walk(r'D:\Faculdade\Aulas'):
    for i in filenames:
       if(not os.path.isfile(dirpath + '/video_completo.mp4') and (i.lower()=="audio.mp4")):          
           inputfilepath = os.path.join(dirpath, i)
           outputfilepath = dirpath + '/audio.aac' 
           subprocess.call(['ffmpeg', '-i', inputfilepath, '-vn', outputfilepath])
        
    for i in filenames:
        if(not os.path.isfile(dirpath + '/video_completo.mp4') and (i.lower()=="video.mp4")):
            inputvideopath = os.path.join(dirpath,i)
            inputaudiopath = dirpath + '/audio.aac'
            outputfilepath = dirpath + '/video_completo.mp4'
            subprocess.call(['ffmpeg', '-i', inputvideopath, '-i', inputaudiopath, outputfilepath])
            os.remove(inputaudiopath)
