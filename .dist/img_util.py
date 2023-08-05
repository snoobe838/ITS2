import matplotlib.pyplot as plt

def imshow(im, title,type = '' ):
    if type:
        plt.imshow(im, cmap= type)
    else:
        plt.imshow(im)
    plt.title(title)
    plt.axis('off')