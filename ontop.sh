# ffmpeg -video_size 160x120 -i /dev/video0 -itsoffset 0.6 -video_size 160x120 -i /dev/video1 -filter_complex "[0:v][1:v] vstack [one]; [one] scale=160:240 [two]; [two] stereo3d=abl:arcc [three]" -map "[three]" -r 10 output2.mkv
# ffmpeg -i /dev/video0 -filter_complex "stereo3d=sbs2l:arcc" output3.mkv
# /usr/local/bin/ffmpeg -i /dev/video0 -vf stereo3d=sbs2l:arcc output3.mkv
# ffmpeg -i /dev/video0 -filter_complex "[0:v]scale=1280:480 [outv]" -map "[outv]" -r 30 output.mkv
ffmpeg -video_size 320x240 -i /dev/video0 -itsoffset 0.6 -video_size 320x240 -i /dev/video1 -filter_complex "[0:v][1:v] vstack [one]; [one] scale=320:480 [two]; [two] stereo3d=abl:arcc [three]" -map "[three]" -r 10 output2.mkv
