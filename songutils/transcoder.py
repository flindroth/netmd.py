import subprocess

def transcode(filename):
    # TODO: Isolate temporary files for multiple instances of transcode
    filename_out = "/tmp/transcode.out"
    try:
        subprocess.call(['ffmpeg','-y','-i',filename,'-f','s16be',filename_out])
    except CallProcessError as e:
        filename_out = None

    return filename_out    
