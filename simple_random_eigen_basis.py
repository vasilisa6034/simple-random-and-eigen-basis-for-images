# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:34:40 2017

@author: temp
"""

import pickle

import numpy as np
import matplotlib.pyplot as plt

#%% load images 
with open(r'referenceImages.dat') as f:
    referenceImages=pickle.load(f)
y,x,z = referenceImages.shape
colImages = np.reshape(referenceImages, (y*x,z)) #transform images (matrces) to vectors(columns)
del referenceImages

# pick input image
with open(r'inputImage.dat') as f:
   im=pickle.load(f)
im = im.flatten()
#%% simple basis
# simple basis is pixels by itself, soo each basis vector has only one nonzero element. Dimention of space equal to number of pixel in image


simple_basis = np.eye(len(im)) # it's simplest ortonormal basis
# obviosly if we project our images on such basis and then reconstruct it we will get same result

proj = np.dot(simple_basis.T, im)
reconstr = np.dot(simple_basis,proj)

f,(ax1,ax2)=plt.subplots(1,2)
ax1.matshow(np.reshape(reconstr,(y,x)), cmap='gray')
ax1.axis('off')
ax1.set_title('reconstructed')
ax2.matshow(np.reshape(im,(y,x)), cmap='gray')
ax2.axis('off')
ax2.set_title('initial')

#%%
#but now what if we suppress numbers of projection?
#right, we simple cut off image, by suppressing it's basis
#lets, get MSE dependence from basis suppression in random order
plt.figure()
supr_bas_lim = 1000
mse = np.zeros(supr_bas_lim)
for i in np.arange(supr_bas_lim):
    suppressed_basis = simple_basis[:,np.random.choice(range(len(im)), len(im)-i, replace=False)]
    proj = np.dot(suppressed_basis.T, im)
    reconst = np.dot(suppressed_basis,proj)
    mse[i]= np.sum(np.abs(im-reconst)/255)/len(im)*100
plt.plot(mse)
ax = plt.gca()
ticks_lables = [item.get_text() for item in ax.get_xticklabels()]
new_ticks = np.linspace(100,(len(im)-np.float16(supr_bas_lim))/len(im)*100, len(ticks_lables),dtype = np.int)
ax.set_xticklabels(new_ticks)
plt.xlabel('% of initial basis')
plt.ylabel('MSE, %')
plt.title('reconstracted image simple basis')

f,(ax1,ax2)=plt.subplots(1,2)
ax1.matshow(np.reshape(reconst,(y,x)), cmap='gray')
ax1.axis('off')
ax1.set_title('reconstracted image from {}% of simple basis'.format(new_ticks[-1]))
ax2.matshow(np.reshape(im,(y,x)), cmap='gray')
ax2.axis('off')
ax2.set_title('initial')
del simple_basis
#%% OK, next thing more interest. We will try to pickup random basis

basis = np.random.rand(len(im),len(im)) #uniform distribution
basis = basis.T - np.mean(basis,axis=1) # substract mean for convolution matrix calculation
basis = basis.T
conv = np.dot(basis,basis.T) # convolution matrix, show depences between pixels of image.
val,vec = np.linalg.eig(conv) # in purpose to get orthonormal basis calculation of eigen vectors should be perform.
random_basis = vec#eigen vector will considered as basis

#%% let's calculate MSE depenence as in previos example
plt.figure()
supr_bas_lim = 1000
mse = np.zeros(supr_bas_lim)
for i in np.arange(supr_bas_lim):
    suppressed_basis = random_basis[:,np.random.choice(range(len(im)), len(im)-i, replace=False)]
    proj = np.dot(suppressed_basis.T, im)
    reconst = np.dot(suppressed_basis,proj)
    mse[i]= np.sum(np.abs(im-reconst)/255)/len(im)*100
plt.plot(mse)
ax = plt.gca()
ticks_lables = [item.get_text() for item in ax.get_xticklabels()]
new_ticks = np.linspace(100,(len(im)-np.float16(supr_bas_lim))/len(im)*100, len(ticks_lables),dtype = np.int)
ax.set_xticklabels(new_ticks)
plt.xlabel('% of initial basis')
plt.ylabel('MSE, %')
plt.title('reconstracted image random basis')


f,(ax1,ax2)=plt.subplots(1,2)
ax1.matshow(np.reshape(reconst,(y,x)), cmap='gray')
ax1.axis('off')
ax1.set_title('reconstracted image from {}% of random basis'.format(new_ticks[-1]))
ax2.matshow(np.reshape(im,(y,x)), cmap='gray')
ax2.axis('off')
ax2.set_title('initial')
del random_basis, basis, conv, vec
#%% eigen basis

colImages_zeromean = colImages.T - np.mean(colImages, axis=1)
colImages_zeromean = colImages_zeromean.T
conv = np.dot(colImages_zeromean,colImages_zeromean.T)
val,eigen_basis = np.linalg.eig(conv)
#%% let's check how basis looks like
#first 200 vectors
n=100
eigen_basis_images = np.reshape(eigen_basis[:,:n], (y,x,n))
width = 10 # number of images in row
height = np.int(np.ceil(n/width))
bigImage = np.zeros((height*y,width*x))
try:
    c = 0
    for row in np.arange(height):
        for col in np.arange(width):
            bigImage[row*y:row*y + y, col*x:col*x + x]=eigen_basis_images[:,:,c]
            c+=1
except:
    pass
plt.matshow(bigImage, cmap= 'gray')
plt.axis('off')
#%% MSE depenence

plt.figure()
supr_bas_lim = 2000
mse = np.zeros(supr_bas_lim)
reconstIm = np.zeros((y,x,supr_bas_lim))
for i in np.arange(supr_bas_lim):
    proj = np.dot(eigen_basis[:,:len(im)-i].T, im)
    reconst = np.dot(eigen_basis[:,:len(im)-i],proj)
    mse[i]= np.sum(np.abs(im-reconst)/255)/len(im)*100
plt.plot(mse)
ax = plt.gca()
ticks_lables = [item.get_text() for item in ax.get_xticklabels()]
new_ticks = np.linspace(100,(len(im)-np.float16(supr_bas_lim))/len(im)*100, len(ticks_lables),dtype = np.int)
ax.set_xticklabels(new_ticks)
plt.xlabel('% of initial basis')
plt.ylabel('MSE, %')
plt.title('reconstracted image eigen basis')

f,(ax1,ax2)=plt.subplots(1,2)
ax1.matshow(np.reshape(reconst,(y,x)), cmap='gray')
ax1.axis('off')
ax1.set_title('reconstracted image from {}% of eigen basis'.format(new_ticks[-1]))
ax2.matshow(np.reshape(im,(y,x)), cmap='gray')
ax2.axis('off')
ax2.set_title('initial')