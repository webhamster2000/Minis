import sys, struct

print("Load", sys.argv[1], "and export video to", sys.argv[1] + ".h264")

f = open(sys.argv[1], "rb")
video = open(sys.argv[1] + ".h264", "wb")

fileheader = f.read(16)
full_len = 0

while True:
    id = f.read(4) # ID tag HXAF = Audio, HXVF = Video, HXFI = File Index
    if id == "" or id == b"HXFI": break
    len = struct.unpack('i', f.read(4))[0] # conten length as 4 byte integer
    f.read(20 - 4 - 4 - 4) # some random buffer
    content = f.read(len) # actual video content
    if id == b"HXVF": #video
        video.write(content)
    full_len += len

f.close()
video.close()
print("Done - extracted", full_len, "bytes of video")