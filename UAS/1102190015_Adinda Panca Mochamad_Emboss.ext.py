from PIL import Image

def apply_emboss_filter(image, kernel):
    width, height = image.size
    kernel_size = len(kernel)
    pad = kernel_size // 2
    
    filtered_image = Image.new("L", (width, height))
    for i in range(pad, width - pad):
        for j in range(pad, height - pad):
            new_pixel_value = 0
            for x in range(kernel_size):
                for y in range(kernel_size):
                    pixel_value = image.getpixel((i + x - pad, j + y - pad))
                    new_pixel_value += pixel_value * kernel[x][y]
            new_pixel_value = min(max(new_pixel_value, 0), 255)
            filtered_image.putpixel((i, j), int(new_pixel_value))
    return filtered_image

mentahpng = "D:/File ITTS S1 CE/SEMESTER 8/CEC30C3 Digital Computer Vision/UAS/sidikjari.png"
gambar = Image.open(mentahpng).convert("L")  #GRAYSCALE

emboss_kernel = [
    [0, 0,  0],
    [-4,  0,  -4],
    [ 0,  0,  0]
]

embosss = apply_emboss_filter(gambar, emboss_kernel)
embosss.show()
