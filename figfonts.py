from pyfiglet import FigletFont, Figlet
import sys

def list_fonts():
    f = FigletFont()
    fonts = f.getFonts()
    print("fonts=", fonts)
    #print("fonts=%s" % fonts)
    #print("fonts={}".format(fonts))
    #print(f'fonts={fonts}')

def get_fonts():
    f = FigletFont()
    fonts = f.getFonts()
    
    fonts = fonts[:]
    
    return fonts

def output(font, text):
    f = Figlet(font=font)
    r = f.renderText(text)
    #sys.stdout.write(r)
    print(r)

def samples():
    fonts = get_fonts()
    print(f'n fonts={len(fonts)}')
    for i, font in enumerate(fonts):
        fontname = font
        output(font, f'{i} {fontname}: hi there')
       

if __name__ == '__main__':
    #list_fonts()
    samples()