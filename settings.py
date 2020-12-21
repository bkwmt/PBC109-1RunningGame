import os
### 常數
TITLE = "The Rolling Donuts"
FPS = 120    # 每秒刷新次數
ADD_FIRE_RATE = 200
WIDTH, HEIGHT = 1250, 650
SIZE = (WIDTH, HEIGHT)
HW, HH = WIDTH / 2, HEIGHT / 2
AREA = WIDTH * HEIGHT

### 定義一些顏色：混合RGB的比例 0-255
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

### 精靈會用到的屬性
DONUT_ACC = 0.5             # 加速度，越大可以跑快一點
DONUT_FRICTION = -0.06      # 摩擦力，越小會滑行越遠，最大速度亦會變大。

### 設定assets： 圖片與聲音的存放
### 取得這個檔案的目錄位置
game_folder = os.path.dirname(__file__)
### 將img指定在上面這個目錄下
img_folder = os.path.join(game_folder, "img")
