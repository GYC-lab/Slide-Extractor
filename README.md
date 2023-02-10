

# Slide-Extractor

## Updates

- This project is forked from [5hade5layer/Slide-Extractor](https://github.com/5hade5layer/Slide-Extractor) on 20230210. 

- New features have been added:

  - Extracts slides from videos of ppt presentations rather than a single video
  - Run the python code directly without arguments input from the command line

## How to run
1. put your videos of ppt presentations into the folder `input_video`
2. run `slides.py` with `python slides.py`, you can be informed of the progress from the output progressbar
1. when the progress is done, you can check the folder `output_slide` which contains the extracted slides
2. you may need to select the slides since the code will capture any difference between frames in videos

If you want to convert the slides (or images) to a pdf file further, then I recommand my repository [img2pdf_in_batches](https://github.com/GYC-lab/img2pdf_in_batches).
which may ease you from a lot cliks on Adobe Acrobat.

