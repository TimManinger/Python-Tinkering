import pydub
import os.path


def split_file(in_path, out_path, split_len = 30000):
    """ Converts an mp3 into chunks of specified length (default 30s)

        in_path: absolute path including filename and extension
        out_path: folder to put chunks into, should have / at the end
        split_len: chunk length in milliseconds
    """
    in_file = pydub.AudioSegment.from_file(in_path, format="mp3")
    
    # ensure output path exists
    dir = os.path.dirname(out_path)
    if not os.path.exists(dir):
        os.makedirs(dir)
    
    for i, chunk in enumerate(in_file[::split_len]):
        with open(out_path+("%s.mp3" % i), "wb") as out_file:
            chunk.export(out_file, format="mp3")
