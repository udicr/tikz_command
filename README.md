# tikz_command

compiles a tikz file (.tex file only consisting of a block \begin{tikzpicture}...\end{tikzpicture}
as a standalone .tex document


bash-alias (add line at ~/.bashrc)
alias tikz='pwd | python3 /home/user/Workspace/tikz_command/tikz.py'

Usage:
tikz plugin_filename.tex
