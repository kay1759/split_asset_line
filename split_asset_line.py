import glob,os,re,shutil,tempfile
from functools import reduce

def sorted_number_split(html_base, assetdir, ext):
    assetfiles = glob.glob(f"{html_base}{assetdir}/*.{ext}")

    filenames = map(os.path.basename, assetfiles)
    numberfiles = filter(lambda line: re.match(re.compile(f"[0-9]+\.{ext}"), line), filenames)
    numberstrs = map(lambda line: re.sub(re.compile(f"\.{ext}"), "", line), numberfiles)
    numbers = map(int, numberstrs)
    return list(sorted(numbers))


def convert_line(line, assetdir, assetfile, ext, assetnumbers, include_orgname):
    if re.search(f"{assetdir}/{assetfile}.{ext}", line):
        converted_line = reduce(lambda accu, num: accu + line.replace(f"{assetdir}/{assetfile}.{ext}",  f"{assetdir}/{num}.{ext}"), assetnumbers, "")
        if include_orgname:
            converted_line += line
    else:
        converted_line = line

    return converted_line


def split_asset_line(sourcefile, html_base, assetdir, assetfile, ext, include_orgname):
    with open(sourcefile) as fr:
        lines = fr.readlines()

    assetnumbers = sorted_number_split(html_base, assetdir, ext)

    converted_lines = reduce(lambda accu, line: accu + convert_line(line, assetdir, assetfile, ext, assetnumbers, include_orgname), lines, "")

    with open(sourcefile, 'w') as fw:
        fw.write(converted_lines)

    return



if __name__ == '__main__':
    import sys

    args = sys.argv

    if len(args) < 6 or len(args) > 7:
        pass   
    else:
        sourcefile = args[1]  # "./script.html.erb"
        html_base = args[2]   # "../webapp/priv/static"
        assetdir = args[3]       # "/assets/js/admin"
        assetfile = args[4]      # "admin"
        ext = args[5]         # "js"

        if len(args) == 6:
            include_orgname = True
        else:
            include_orgname = bool(args[6])

        split_asset_line(sourcefile, html_base, assetdir, assetfile, ext, include_orgname)

