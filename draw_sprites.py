import Image
import ImageDraw
def draw_sprite(image, coor, color=0):
    draw = ImageDraw.Draw(image)
    x0=coor[0]-10
    x1=coor[0]+10
    y0=coor[1]-10
    y1=coor[1]+10
    if(color):
        draw.ellipse((x0,y0,x1,y1),fill=color)
    else:
        draw.ellipse((x0,y0,x1,y1))
    return image
def draw_face(image, coor,text="?"):
    print "not done yet"
    color()
    if(text=="?"):
        draw_sprite
def draw_sprites(image, data):
    for face in data:
        image=draw_sprite(image, face[0])
        

        '''
        for feature in face[1]:

            image=draw_sprite(image, )
        '''
            

if __name__ == "__main__":
    im = Image.open("test.jpg")
    draw_sprites(im, [[[162,66],["t", "f"]],[[34,43],["t", "l","g"]],[[215,34],["g","f","t"]]])
