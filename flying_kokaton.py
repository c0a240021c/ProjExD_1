import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    gg_img = pg.transform.flip(bg_img,True,False)#練習8
    kk_img = pg.image.load("fig/3.png")#練習2前半
    kk_img = pg.transform.flip(kk_img,True,False)#練習2後半

    kk_rct = kk_img.get_rect() # Rect属性の取得
    kk_rct.center= 300,200 # Rectのcenter属性に、初期座標を設定

    tmr = 0
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        
        k_lst = [-1,0]

        
        if key_lst[pg.K_UP]:
            k_lst[1] += -1
        if key_lst[pg.K_DOWN]:
            k_lst[1]+=1
        if key_lst[pg.K_LEFT]:
            k_lst[0] += -1
        if key_lst[pg.K_RIGHT]:
            k_lst[0] += 2
        
        
        
        kk_rct.move_ip(k_lst)

        x = tmr % 3200 #練習9
        

        screen.blit(bg_img, [-x, 0])
        screen.blit(gg_img, [-x+1600, 0])#練習7、練習8
        screen.blit(bg_img, [-x+3200, 0])#練習9
        screen.blit(kk_img,kk_rct)#練習4

        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()