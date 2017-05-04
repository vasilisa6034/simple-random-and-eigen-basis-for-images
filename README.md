# simple-random-and-eigen-basis-for-images
my experience in variants basis for images.

This little example can help in understanding of images vector space. 
We can consider an image as vector, which dimensionality equal to number of pixels. Let's consider images with just three pixels. Easy to see that simpleast basis for such space (1,0,0), (0,1,0) and (0,0,1), but what if our images lie on one surface, or even one line in this space? Then we can transfere to another, more compact basis, for which we can store two (surface) or even one (line) rather three numbers (for each pixel). That's how compression  works.

Another case - we truncate our basis (simply throwing elements of basis - basis vectors). In straightforward case ((1,0,0), ...) we simply will throw pixels, but what will happen in more fitted basis case? In this sketch I tried to cover this questions.

I consider human face images. To form eigen basis I use this database http://vis-www.cs.umass.edu/lfw/. **dataPrepere.py** - help to form **referenceImages.dat** which consist of face images as columns in one matrix. Main file **simple_random_eigen_basis.py**.  File **inputImage.dat** consist of separated from database examine image. 

Then we use simple straightforward basis, where only one element equal to 1 and other to 0, expectedly reconstruction from such image projection give us same image.
![figure_1](https://cloud.githubusercontent.com/assets/19648595/25664016/5ecdfb6c-302a-11e7-85ef-cfbac1f33ae2.png)

If we will try to throw basis vector away we will get image without corresponding pixels. This dependence show how MSE changes corresponding to basis restriction (in random order).

![figure_2](https://cloud.githubusercontent.com/assets/19648595/25662323/2ca23fae-3025-11e7-8171-6b25113e37d2.png)

And how image will looks like when we leave only 60% of basis vectors.

![figure_3](https://cloud.githubusercontent.com/assets/19648595/25662316/2c351dfc-3025-11e7-8ae7-72343657cf51.png)

Well, actually instead of this basis we can use any orthonormal basis, for example random orthogonal vectors which norm equal to 1. And then let's restrict basis.

![figure_4](https://cloud.githubusercontent.com/assets/19648595/25662317/2c391b0a-3025-11e7-864b-fc45dcdcd263.png)

Same 60% remain but for new (random) basis

![figure_5](https://cloud.githubusercontent.com/assets/19648595/25662318/2c3cbc1a-3025-11e7-903d-038dab0de62c.png)


![figure_6](https://cloud.githubusercontent.com/assets/19648595/25662319/2c44acea-3025-11e7-8564-dac7a2b116ec.png)
![figure_7](https://cloud.githubusercontent.com/assets/19648595/25662320/2c52ec56-3025-11e7-8ae1-e70e212a54ce.png)
![figure_8](https://cloud.githubusercontent.com/assets/19648595/25662321/2c5c9e68-3025-11e7-89a8-30435b6435d6.png)

