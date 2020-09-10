import os
import argparse
import wave
import math


def audio_cut(audio_in_path, audio_out_path, start_time, dur_time):
    """
    :param audio_in_path: 输入音频的绝对路径
    :param audio_out_path: 切分后输出音频的绝对路径
    :param start_time: 切分开始时间
    :param dur_time: 切分持续时间
    :return:
    """
    os.system("ffmpeg -i {in_path} -vn -acodec copy -ss {Start_time} -t {Dur_time}  {out_path}".format(in_path = audio_in_path,
               out_path = audio_out_path, Start_time = start_time, Dur_time = dur_time))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', default='')
    parser.add_argument('--out_dir', default='')
    args = parser.parse_args()
    audio_list = os.listdir(args.input_dir)

    start_time = 0 #切割开始时间
    dur_time = 1  #切割的片段时长s
    out_number = 0 #输出文件序号
    for file in audio_list:
        time_count = 0
        audio_in_path = args.input_dir+"/"+file
        print(audio_in_path)
        with wave.open(audio_in_path,'rb') as f:
            time_count += f.getparams().nframes/f.getparams().framerate
        print(time_count)
        for i in range(math.floor(time_count / dur_time)):
            audio_out_name = str(out_number)+".wav"   #切割完生成的片段名
            out_number = out_number+1
            print(audio_out_name)
            audio_out_path = args.out_dir + "/" + audio_out_name
            print(audio_out_path)
            audio_cut(audio_in_path, audio_out_path, start_time, dur_time)
            start_time = start_time + dur_time

if __name__ == "__main__":
    main()
