import os
import os.path as osp
import glob

rawdir = osp.join(os.getcwd(), "raw")

if not os.path.isdir(rawdir):
    raise Exception("ERROR: `raw` directory does not exist in currently working directory.")

genuine_pattern = "*EVLI0000.FTZ"
faked_pattern   = "*EVLF0000.FTZ"
len_ext = len(faked_pattern) - 1 
assert len_ext == len(genuine_pattern) - 1 

G_filelist = list(glob.glob(osp.join(rawdir, genuine_pattern)))
G_filedict = {common : G_file for common, G_file in zip(map(lambda file: osp.basename(file)[:-len_ext], G_filelist), G_filelist)}
F_filelist = list(glob.glob(osp.join(rawdir, faked_pattern)))

i = 0
for F_file in F_filelist:
    if osp.getsize(F_file) == 0:
        print(f"{osp.basename(F_file)} found to be void", end=" ")
        common_path = osp.basename(F_file)[:-len_ext]
        os.remove(F_file)
        del F_filelist[i]
        print("and removed")
        if not common_path in G_filedict:
            continue
        os.remove(G_file)
        G_file = G_filedict[common_path]
        del G_filedict[common_path]
        print(f"companion file {osp.basename(G_file)} removed too")
        print()
    else:
        i+=1

F_filedict = {common : G_file for common, G_file in zip(map(lambda file: osp.basename(file)[:-len_ext], F_filelist), F_filelist)}

F_m_G = set(F_filedict) - set(G_filedict)

if len(F_m_G) > 0:
    for key in F_m_G:
        print(f"{key} found to be companionless", end = " ")
        os.remove(F_filedict[key])
        del F_filedict[key]
        print("and removed")

G_m_F = set(G_filedict) - set(F_filedict)

if len(G_m_F) > 0:
    for key in G_m_F:
        print(f"{key} found to be companionless", end = " ")
        os.remove(G_filedict[key])
        del G_filedict[key]
        print("and removed")
