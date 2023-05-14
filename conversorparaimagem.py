# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
images = convert_from_path('G:\Outros computadores\My MacBook Pro\Coisas MacBook\Workshop Maxplanck\Documentos\Atas da subcomissão elaboradora do anteporjeto 1932-1933\Atas da subcomissão elaboradora do anteporjeto 1932-1933.pdf')

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('G:\Outros computadores\My MacBook Pro\Coisas MacBook\Workshop Maxplanck\Documentos\Atas da subcomissão elaboradora do anteporjeto 1932-1933\jpgs\page'+ str(i) +'.jpg', 'JPEG')

