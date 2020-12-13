import argparse
import os

parser = argparse.ArgumentParser(description='Calculate FID For Many Results')
parser.add_argument("--log_dir", type=str, required=True, help="")
parser.add_argument("--base_epoch", type=int, default=0)
parser.add_argument("--reala", type=str)
parser.add_argument("--realb", type=str)
parser.add_argument("--real", type=str)
parser.add_argument("--max_epoch", type=int, default=-1)
args = parser.parse_args()

epochs = set()
while True:
	files = os.listdir(args.log_dir)
	files = [int(i) for i in files if os.path.isdir(os.path.join(args.log_dir,i))]
	files = sorted([i for i in files if i not in epochs])
	if args.max_epoch == -1: args.max_epoch = max(files)
	for e in files:
		if e < args.base_epoch or e > args.max_epoch: continue
		epochs.add(e)
		print("Epoch", e)
		os.system('echo  "Epoch %d" >> %s' % (e, os.path.join(args.log_dir, "fid.txt")))
		#if args.real: os.system("python3 fid.py %s %s --lowprofile >> %s" % (args.real, os.path.join(args.log_dir, str(e), "images"), os.path.join(args.log_dir, "fid.txt")))
		if args.reala and args.realb:
			os.system("python3 fid.py %s %s --lowprofile >> %s" % (args.reala, os.path.join(args.log_dir, str(e), "fakes", "fakeB"), os.path.join(args.log_dir, "fid.txt")))
			os.system("python3 fid.py %s %s --lowprofile >> %s" % (args.realb, os.path.join(args.log_dir, str(e), "fakes", "fakeA"), os.path.join(args.log_dir, "fid.txt")))
		#if args.real: os.system("python3 fid.py %s %s --lowprofile >> %s" % (args.real, os.path.join(args.log_dir, str(e), "fakes", "fakeAB"), os.path.join(args.log_dir, "fid.txt")))
