import pygame


def main():

    # 创建一个窗口
    screen = pygame.display.set_mode((460, 680), pygame.RESIZABLE, 32)
    # 选择背景图片
    background = pygame.image.load("./images/background.png")
    # 将背景图片放到窗口
    # 创建一个飞机

    screen.blit(background, (0, 0))

    # 显示窗口的内容
    while 1 :
        # 获取事件
        for  event  in  pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()

        # 显示窗口的内容
        pygame.display.update()


if __name__ == '__main__':
    main()
