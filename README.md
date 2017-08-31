# amazon-to-srt
1. Get the subtitles from amazon (if you need this tool, you should already know how)
2. Convert them into .srt files


## Usage
- Install python 3.4+ (tested with python3.4, python3.5)
- Clone this repository: `git clone https://github.com/mawashii/amazon-to-srt.git`
- Run the script in your shell: `python ./convert.py [input directory] [output directory]`
	- You don't need to specifiy either directory, if you leave them empty the script defaults to the current directory
	- All `*.xml` and `*.dfxp` files inside the input directory will be converted to `*.srt` files in the output directory
	- Naming convention: `input_file.xml` will become `input_file.srt`

## Notes
- Loosely based on https://github.com/isaacbernat/netflix-to-srt
- Some very basic error handling has been added, no timestamp plausibility checks
