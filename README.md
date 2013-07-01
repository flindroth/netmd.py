netmd.py
========

netmd.py is a program for transferring songs to your NetMD device in SP mode (ATRAC3 codecs are not openly available).


Example invocation
------------------

    $ ./netmd.py -f file.mp3

This command will transcode the song contained in file.mp3 to 16-bit PCM (big endian), extract its ID3 artist/title information, and transfer it to the first connected NetMD device it can find.
 
    $ ./netmd.py -h

Show help.

What is left to do?
-------------------
A lot of things. The libnetmd library ideally needs to be modified to throw sane exceptions, as well as be compatible with Python 3. The libnetmd authors (from the linux-minidisc project) are working on the C version of the library, and the python version has not been touched for a long time.

Also, error handling needs to be greatly improved across the board. This is something I personally will be working on, so rest assured this program will look a LOT more polished in the near future.


