from PIL import Image, ImageDraw
n = int(input())
m = int(input())

img = Image.new('RGB', (n, 9*m), 'Yellow')
dib = ImageDraw.Draw(img)
y1 = 0
for i in range(9):
  if (i%2 ==1):
   dib.polygon([(0,y1), (n, y1), (n, y1+m-1), (0, y1+m-1)], "Red")
  y1 = y1 + m 
img.save('output.png')
