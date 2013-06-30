def readTag(filename):
    id3data = None
    try:
        id3data = subprocess.check_output(['id3v2','-l',filename])
        title = None
    except CalledProcessError as e:
        title = os.path.basename(filename)

