import io
from google.cloud import vision
from google.cloud.vision import types
#print vision.methods
client = vision.ImageAnnotatorClient()

file_name = 'IMG_0510.JPG'

with io.open(file_name, 'rb') as image_file:
	content = image_file.read()
	image = types.Image(content=content)



response_texts = client.text_detection(image=image)
texts = response_texts.text_annotations


print('Texts:')
for text in texts:
	print('\n"{}"'.format(text.description))
	vertices = (['({},{})'.format(vertex.x, vertex.y)
		for vertex in text.bounding_poly.vertices])
	print('bounds: {}'.format(','.join(vertices)))

