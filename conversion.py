import os
import shutil
import argparse
import random

def create_dir(path=""):
    os.mkdir(path)


def close_tag(taglist, file):
    file.write(taglist[-1][:1] + '/' + taglist[-1][1:])
    taglist.pop(-1)

def count_char(text):
    counts = 1
    inline = False
    for char in range(1, len(text)):
        last = text[char - 1]
        if text[char] != ' ' and text[char] != last:
            inline = True
        if last == text[char]:
            counts += 1
        else:
            break;
    return counts, inline

def rewrite(text, file, basetab=2, k=False, a=False):
    char = 0
    tab = 0
    tag = []
    link = ''
    islink = False
    isimg = False
    while char < len(text):
        if text[char] in ["#", "*", "_", "~", "[", "]", "(", ")", "!"]:
            count, inline = count_char(text[char:])
            mdbal = text[char] * count
            isfirstel = True
            countspaces = 1
            while text[char - countspaces] != '\n':
                if not text[char - countspaces] in ['\t', ' ']:
                    isfirstel = False
                else:
                    isfirstel = True
                countspaces +=1
            if isfirstel or char == 0:
                if mdbal == "#":
                    tag.append('<h1>')
                    file.write(tag[-1])
                elif mdbal == "##":
                    tag.append('<h2>')
                    file.write(tag[-1])
                elif mdbal == "###":
                    tag.append('<h3>')
                    file.write(tag[-1])
                elif mdbal == "####":
                    tag.append('<h4>')
                    file.write(tag[-1])
                elif mdbal == "#####":
                    tag.append('<h5>')
                    file.write(tag[-1])
                elif mdbal == "######":
                    tag.append('<h6>')
                    file.write(tag[-1])
            elif (not isfirstel) and text[char] == '#':
                file.write('#')
            elif mdbal in ['*', '_', '**', '__'] and inline:
                print(text[char])
                if len(tag) > 0 and tag[-1] in ['<em>', '<strong>']:
                    close_tag(tag, file)
                else:
                    if mdbal in ['*', '_']:
                        tag.append('<em>')
                        file.write(tag[-1])
                    else:
                        tag.append('<strong>')
                        file.write(tag[-1])
            elif mdbal == '!' and text[char + 1] != '[':
                file.write('!')
            elif mdbal == '[':
                islink = True
                if text[char - 1] == '!':
                    isimg = True
            elif mdbal == ']':
                pass
            elif mdbal == '(' and islink:
                if isimg:
                    tag.append('<img src="')
                else:
                    tag.append('<a href="')
                file.write(tag[-1])
                islink = False
            elif len(tag) > 0 and mdbal ==')' and tag[-1] in ['<a href="', '<img src="']:
                    if isimg:
                        tag.remove('<img src="')
                        file.write('" alt="' + link + '"/>')
                        isimg = False
                    else:
                        tag.remove('<a href="')
                        file.write('">' + link + '</a>')
                    link = ''
            elif mdbal == '*' and not inline:
                countspaces = 1
                while text[char - countspaces] != '\n':
                    if text[char - countspaces] in ['\t', ' ']:
                        countspaces += 1
                if (not '<ul>' in tag) or (tag.count('<ul>') == 1 and text[char - 2] + text[char - 1] in ['\n ', '\n\t']):
                    tag.append('<ul>')
                    file.write('\t' * tab + tag[-1] + '\n')
                    tab += 1
                    file.write('\t' * (tab + basetab) + '<li>')
                elif tag.count('<ul>') > 1 and not text[char - 2] + text[char - 1] in ['\n ', '\n\t']:
                    tab -= 1
                    file.write('\t' * tab + '</ul>\n')
                    tag.remove('<ul>')
                    file.write('\t' * (tab + basetab) + '<li>')
                elif '<ul>' in tag:
                    file.write('\t' * tab + '<li>')
                tag.append('<li>')

            char += count
        else:
            if text[char] == 'h':
                if char < len(text) + 1 and text[char] + text[char + 1] + text[char + 2] + text[char + 3] == "http" and (char == 0 or text[char - 2] + text[char - 1] != "]("):
                    islink = True
                    tag.append('<a href="')
                    file.write(tag[-1])
            if len(tag) > 0 and (text[char] in [' ', '\n']) and islink and tag[-1] == '<a href="':
                file.write(link + '">' + link + '</a>')
                link = ''
                tag.pop(-1)
                islink = False
            if text[char] == '\n':
                if len(tag) > 0 and tag[-1] not in ['<ul>', '<em>', 'strong']:
                    close_tag(tag, file)
                if (text[char - 1] == '\n' or char == len(text) - 1) and '<ul>' in tag:
                    for ul in range(tag.count('<ul>')):
                        tab -= 1
                        file.write('\n' + '\t' * (tab + basetab) + '</ul>')
                        tag.remove('<ul>')
                file.write(text[char])
                if char != len(text) - 1:
                    file.write('\t' * basetab)
            elif not(text[char - 1] in ["#", "*", "_", "~", "\n"] and text[char] == ' '):
                if islink:
                    link += text[char]
                else:
                    if k:
                        if text[char] == ' ':
                            file.write(' ')
                            file.write(random.choice(['kikoo', 'lol', 'mdr', 'ptdr', 'xptdr']) * random.choice([0, 1]))
                        else:
                            nbchar = random.random()
                            if nbchar < 0.15:
                                file.write(text[char] * random.choice([1, 2, 3]))
                    if not a:
                        file.write(text[char])
                    else:
                        letters = {'s':'z', 'c':'k', 'q':'k', 'S':'Z', 'C':'K', 'Q':'K'}
                        if text[char] in letters.keys():
                            file.write(letters[text[char]])
                        elif text[char] in ['p', 'P'] and text[char + 1] == 'h':
                            if text[char] == 'p':
                                file.write('f')
                            else:
                                file.write('F')
                            char += 1
                        else:
                            file.write(text[char])
            char += 1


def files_creation(dir, odir, k=False, a=False):
    if a:
        print('achtung activated')
    if k:
        print('kikool-lol activated')
    for entry in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, entry)) and os.listdir(os.path.join(dir, entry)):
            print("Created dir : " + os.path.join(odir, entry))
            create_dir(odir + "/" + entry)
            files_creation(dir + "/" + entry, odir + "/" + entry, k, a)
        if os.path.isfile(os.path.join(dir, entry)) and os.path.join(dir, entry)[-2:] == "md":
            print("Created file : " + os.path.join(odir, entry[:-2] + "html"))
            mdfile = open(os.path.join(dir, entry), 'r')
            htmlfile = open(os.path.join(odir, entry[:-2] + "html"), 'w')
            htmlfile.write('<!doctype html>')
            htmlfile.write('\n<html>')
            htmlfile.write('\n\t<head>')
            htmlfile.write('\n\t</head>')
            htmlfile.write('\n\t<body>\n\t\t')
            rewrite(mdfile.read(), htmlfile, k=k, a=a)
            htmlfile.write('\t</body>')
            htmlfile.write('\n</html>')
            mdfile.close()
            htmlfile.close()

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-directory", help="input folder for md files, if full path please add quotes")
parser.add_argument("-o", "--output-directory", help="output folder for md files, if full path please add quotes")
parser.add_argument("-k", "--kikoo-lol", help="add kikoo, lol, mdr, ptdr and other words", action="store_true")
parser.add_argument("-a", "--achtung", help="help german friends to understand", action="store_true")
args = parser.parse_args()
dir = args.input_directory
odir = args.output_directory
kikoo = args.kikoo_lol
achtung = args.achtung

if not os.path.exists(odir):
    create_dir(odir)
else:
    shutil.rmtree(odir)
    create_dir(odir)

files_creation(dir, odir, k=kikoo, a=achtung)
