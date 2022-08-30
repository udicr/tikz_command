# -*- coding: utf-8 -*-
import sys
import subprocess

def help():
    print("Help information")

def wrapper(content, additional_packages=None, resize_box = None):
    lines = [r"\documentclass[crop,tikz]{standalone}",r"\usepackage{tikz}",r"\begin{document}", *content, r"\end{document}"]
    return lines

def read_content(file):
    return file.readlines()

def touch_tmp():
    subprocess.call(["touch","tmp.tex"])

def write_tmp(content):
    with open("tmp.tex",'w') as tmp_file:
        for line in content:
            tmp_file.writelines(line.strip()+"\n")

def pdflatex_tmp():
    subprocess.call(["pdflatex","tmp.tex"])

def okular_tmp():
    subprocess.call(["okular","tmp.pdf"])

def mv_pdf(abs_path):
    subprocess.call(["mv","tmp.pdf",abs_path.strip()+"/tmp.pdf"])

def delete_tmp():
    subprocess.call(["rm","tmp.tex","tmp.aux","tmp.log"])

if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) < 2:
        help()
    else:
        try:
            filename = sys.argv[1]
            abs_path = sys.stdin.read()
            print(abs_path)
            with open(filename,'r') as file:
                content = read_content(file)
            wrapped =  wrapper(content)
            touch_tmp()
            write_tmp(wrapped)
            pdflatex_tmp()
            #mv_pdf(abs_path)
            okular_tmp()
            delete_tmp()
        except FileNotFoundError as e:
            print(e)





