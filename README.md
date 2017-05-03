# simple-random-and-eigen-basis-for-images
my experience in variants basis for images
This little example can help in understanding of images vector space. 
We can consider an image as vector, which dimensionality equal to number of pixels. Let's consider images with just three pixels. Easy to see that simpleast basis for such space (1,0,0), (0,1,0) and (0,0,1), but what if our images lie on one surface, or even one line? Then we can transfere to another, more compact basis, for which we can store two (surface) or even one (line) rather three numbers (for each pixel). That's how compression  works.
Another case - we truncate our scape (simply throwing elements of basis - basis vectors). In straightforward case ((1,0,0), ...) we simply will throw pixels, but what will happen in more fitted basis case? In this sketch I tried to cover this questions.

I consider human face images. To form eigen basis I use this database http://vis-www.cs.umass.edu/lfw/. **dataPrepere.py** - help to form **referenceImages.dat** which consist of face images as columns in one matrix. Main file **simple_random_eigen_basis.py**. **inputImage.dat** consist of separated from database image. 



