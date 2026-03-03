# Displays two images side by side in a matplotlib window.
# Used to compare the original photo and its normalized depth heatmap.

import matplotlib.pyplot as plt

def compare_image(image1, image2):
    figure, axes = plt.subplots(1,2)

    axes[0].imshow(image1)
    axes[0].set_title('Original')
    axes[0].axis("off")

    axes[1].imshow(image2)
    axes[1].set_title('New')
    axes[1].axis("off")

    plt.tight_layout()

    plt.show()
