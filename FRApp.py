import re
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/calcpixval',methods = ['POST', 'GET'])
def calcpixval():
	def normalizeimg(width, height, corners):

#	Get the values of the biggest and smallest corners and the difference between them
		highcorner = max(corners)
		lowcorner = min(corners)
		diffcorner = [0, 0]
		diffcorner[0] = highcorner[0] - lowcorner[0]
		diffcorner[1] = highcorner[1] - lowcorner[1]

#	make 3 arrays the size of the final image, one for the original image, one normalized to 0.0 - 1.0, and
#	one that will get the transformed pic in it
		origpix = [[0.0, 0.0] for i in range(width * height)]
		normpix = [[0.0, 0.0] for i in range(width * height)]
		tfdpix = [[0.0, 0.0] for i in range(width * height)]

#	fill empty array with original pixel values
		for i in range(len(origpix)):
			origpix[i][0] = i % height
			origpix[i][1] = int(i / height)

#	normalize original pixel values between 0.0 and 1.0
		for i in range(len(normpix)):
			normpix[i][0] = (float(origpix[i][0]) * 100) / (height - 1) / 100
			normpix[i][1] = (float(origpix[i][1]) * 100) / (width - 1) / 100

#	multiply our normalized values with the difference of the corner values, and add the lowest (offset) value
		for i in range (len(tfdpix)):
			tfdpix[i][0] = (diffcorner[0] * normpix[i][0]) + lowcorner[0]
			tfdpix[i][1] = (diffcorner[1] * normpix[i][1]) + lowcorner[1]

#	Return the array we've generated
		return tfdpix

#	Get inputs
	piccorners = eval(request.form['corners'])
	dimensions = eval(request.form['dimensions'])
	width = dimensions[0]
	height = dimensions[1]

#	Functon call
	return normalizeimg(height, width, piccorners)

if __name__ == '__main__':
   app.run(debug = True)
