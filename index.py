from colordesc.colordescriptor import ColorDescriptor
import argparse
import glob
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True)
ap.add_argument("-i", "--index", required = True)
args = vars(ap.parse_args())

cd = ColorDescriptor((8, 12, 3))

output = open(args["index"], "w")

for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)
	features = cd.describe(image)
	features = [str(feature) for feature in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))
for imagePath in glob.glob(args["dataset"] + "/*.jpeg"):
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)
	features = cd.describe(image)
	features = [str(feature) for feature in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))
for imagePath in glob.glob(args["dataset"] + "/*.png"):
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)
	features = cd.describe(image)
	features = [str(feature) for feature in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))


output.close()