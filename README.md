# tikz_command

compiles a tikz (.tex or .tikz) file as a standalone document
(.tex file only consisting of a block 
\begin{tikzpicture}...\end{tikzpicture})



bash-alias (add line at ~/.bashrc)

alias tikz='pwd | python3 YOUR_GLOBAL_PATH_TO_THE_FILE/tikz.py'


Usage:

tikz plugin_filename.tex
