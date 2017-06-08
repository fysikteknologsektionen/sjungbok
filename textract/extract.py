import re, os

def extract(file_path):
    pattern = r"\\begin\{song\}\{([^\}]+)\}\{([^\}]+)\}"
    fileopen = False
    with open(file_path) as f:
        for line in f:
            str=line.strip()
            if fileopen:
                f2.write(str+"\n")
            if "\\begin{song}" in str:
                sObj = re.search(pattern, str)
                tex=sObj.group(2)+".tex"
                print(tex)
                f2 = open("../texter/"+tex,"w")
                fileopen = True
                f2.write(sObj.group()+"\n")
            if "\\end{song}" in str:
                f2.close()
                fileopen = False

def main():
    file_path = "hyfsvisor.tex"
    for file_path in os.listdir('.'):
        if file_path.endswith(".tex"):
            print("Extracting from "+file_path)
            extract(file_path)

if __name__ == "__main__":
    main()