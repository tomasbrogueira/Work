# data augmentation using brightness, contrast, saturation, hue, and blur of a vector of images using tensorflow

import tensorflow as tf
import numpy as np
import cv2
import random
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def augment_brightness(image):
    # convert to HSV so that its easy to adjust brightness
    image1 = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    # randomly generate the brightness reduction factor
    # Add a constant so that it prevents the image from being completely dark
    random_bright = .25+np.random.uniform()
    # Apply the brightness reduction to the V channel
    image1[:,:,2] = image1[:,:,2]*random_bright
    # convert to RBG again
    image1 = cv2.cvtColor(image1,cv2.COLOR_HSV2RGB)
    return image1

def augment_contrast(image):
    # convert to HSV so that its easy to adjust brightness
    image1 = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    # randomly generate the brightness reduction factor
    # Add a constant so that it prevents the image from being completely dark
    random_contrast = .25+np.random.uniform()
    # Apply the brightness reduction to the V channel
    image1[:,:,2] = image1[:,:,2]*random_contrast
    # convert to RBG again
    image1 = cv2.cvtColor(image1,cv2.COLOR_HSV2RGB)
    return image1

def augment_saturation(image):
    # convert to HSV so that its easy to adjust brightness
    image1 = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    # randomly generate the brightness reduction factor
    # Add a constant so that it prevents the image from being completely dark
    random_saturation = .25+np.random.uniform()
    # Apply the brightness reduction to the V channel
    image1[:,:,2] = image1[:,:,2]*random_saturation
    # convert to RBG again
    image1 = cv2.cvtColor(image1,cv2.COLOR_HSV2RGB)
    return image1

def augment_hue(image):
    # convert to HSV so that its easy to adjust brightness
    image1 = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    # randomly generate the brightness reduction factor
    # Add a constant so that it prevents the image from being completely dark
    random_hue = .25+np.random.uniform()
    # Apply the brightness reduction to the V channel
    image1[:,:,2] = image1[:,:,2]*random_hue
    # convert to RBG again
    image1 = cv2.cvtColor(image1,cv2.COLOR_HSV2RGB)
    return image1

def augment_blur(image):
    # convert to HSV so that its easy to adjust brightness
    image1 = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    # randomly generate the brightness reduction factor
    # Add a constant so that it prevents the image from being completely dark
    random_blur = .25+np.random.uniform()
    # Apply the brightness reduction to the V channel
    image1[:,:,2] = image1[:,:,2]*random_blur
    # convert to RBG again
    image1 = cv2.cvtColor(image1,cv2.COLOR_HSV2RGB)
    return image1

def augment_image(image):
    # convert to HSV so that its easy to adjust brightness
    image1 = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    # randomly generate the brightness reduction factor
    # Add a constant so that it prevents the image from being completely dark
    random_bright = .25+np.random.uniform()
    random_contrast = .25+np.random.uniform()
    random_saturation = .25+np.random.uniform()
    random_hue = .25+np.random.uniform()
    random_blur = .25+np.random.uniform()
    # Apply the brightness reduction to the V channel
    image1[:,:,2] = image1[:,:,2]*random_bright
    image1[:,:,2] = image1[:,:,2]*random_contrast
    image1[:,:,2] = image1[:,:,2]*random_saturation
    image1[:,:,2] = image1[:,:,2]*random_hue
    image1[:,:,2] = image1[:,:,2]*random_blur
    # convert to RBG again
    image1 = cv2.cvtColor(image1,cv2.COLOR_HSV2RGB)
    return image1

def augment_images(images):
    augmented_images = []
    for image in images:
        augmented_images.append(augment_image(image))
    return augmented_images

def augment_images_brightness(images):
    augmented_images = []
    for image in images:
        augmented_images.append(augment_brightness(image))
    return augmented_images

def augment_images_contrast(images):
    augmented_images = []
    for image in images:
        augmented_images.append(augment_contrast(image))
    return augmented_images

def augment_images_saturation(images):
    augmented_images = []
    for image in images:
        augmented_images.append(augment_saturation(image))
    return augmented_images

def augment_images_hue(images):
    augmented_images = []
    for image in images:
        augmented_images.append(augment_hue(image))
    return augmented_images

def augment_images_blur(images):
    augmented_images = []
    for image in images:
        augmented_images.append(augment_blur(image))
    return augmented_images

def augment_images_brightness_contrast(images):
    augmented_images = []
    for image in images:
        augmented_images.append(augment_brightness(image))
        augmented_images.append(augment_contrast(image))
    return augmented_images

def augment_images_brightness_contrast_saturation(images):
    augmented_images = []
    for image in images:
        augmented_images.append(augment_brightness(image))
        augmented_images.append(augment_contrast(image))
        augmented_images.append(augment_saturation(image))
    return augmented_images

def augment_images_brightness_contrast_saturation_hue(images):
    augmented_images = []
    for image in images:
        augmented_images.append(augment_brightness(image))
        augmented_images.append(augment_contrast(image))
        augmented_images.append(augment_saturation(image))
        augmented_images.append(augment_hue(image))
    return augmented_images

def augment_images_brightness_contrast_saturation_hue_blur(images):
    augmented_images = []
    for image in images:
        augmented_images.append(augment_brightness(image))
        augmented_images.append(augment_contrast(image))
        augmented_images.append(augment_saturation(image))
        augmented_images.append(augment_hue(image))
        augmented_images.append(augment_blur(image))
    return augmented_images



