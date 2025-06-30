from PIL import Image

# Open and resize the square logo to 120x120
img = Image.open('/home/ubuntu/admind-privacy/assets/logo_admind_square.png')
img_resized = img.resize((120, 120), Image.Resampling.LANCZOS)
img_resized.save('/home/ubuntu/admind-privacy/assets/logo_admind_120x120.png')

print("Logo resized to 120x120 successfully!")

