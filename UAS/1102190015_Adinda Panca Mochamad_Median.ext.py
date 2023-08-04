from PIL import Image

def apply_median_filter(image, kernel_size):
    filtered_image = image.copy()
    width, height = image.size
    pad = kernel_size // 2
    
    for i in range(pad, width - pad):
        for j in range(pad, height - pad):
            window = [
                image.getpixel((x, y))
                for x in range(i - pad, i + pad + 1)
                for y in range(j - pad, j + pad + 1)
            ]
            median_value = sorted(window)[len(window) // 2] #Ambil Nilai Median
            filtered_image.putpixel((i, j), median_value)
    return filtered_image


kernel_size = 3
gambarmentah = Image.open("D:/File ITTS S1 CE/SEMESTER 8/CEC30C3 Digital Computer Vision/UAS/boneka2.jpg")

filtermedian = apply_median_filter(gambarmentah, kernel_size)
filtermedian.show()