import os, math
### 常數
TITLE = "The Rolling Donuts"
FPS = 120    # 每秒刷新次數
ADD_FIRE_RATE = 200
WIDTH, HEIGHT = 1250, 650   # 畫面大小
SIZE = (WIDTH, HEIGHT)
HW, HH = WIDTH / 2, HEIGHT / 2
AREA = WIDTH * HEIGHT
GHEIGHT = 50    # 地面高度

### 定義一些顏色：混合RGB的比例 0-255
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)

### 精靈會用到的屬性
DONUT_W = 30    # 暫定
DONUT_H = 40
DONUT_ACC = 0.5             # 加速度，越大可以跑快一點
DONUT_FRICTION = -0.06      # 摩擦力，越小會滑行越遠，最大速度亦會變大。
GRAVITY = 0.6               # 重力
JMP = -20                   # 跳躍力（加速度／絕對值越大越強）

### 波狀飛行物用常數
BSPEED = 3
AMPLITUDE = 5
### firball用常數
FSPEED = 7
fire_list = []
add_fire_rate = 0

### dropdown用常數
DSPEED = 1

### 平台（x, y, 寬度, 厚度）
### 因為目前人物寬100，所以平台寬度至少150吧，暫定以５０為單位增加
### 或者寬度也可固定幾種
### 或者位置也可以固定
PSPEED = 1
THICK = 15
PW = 150
PWADD = 50
PLATFORM_LIST = [(0, 450, PW, THICK),
                 (WIDTH / 6 + 100, 400, PW + PWADD, THICK),
                 (2 * WIDTH / 6, 100, PW, THICK),
                 (3 * WIDTH / 6 + 100, 450, PW, THICK),
                 (4 * WIDTH / 6, 100, PW + PWADD, THICK),
                 (5 * WIDTH / 6, 250, PW, THICK),]

### 設定assets： 圖片與聲音的存放
### 取得這個檔案的目錄位置
game_folder = os.path.dirname(__file__)
### 將img指定在上面這個目錄下
img_folder = os.path.join(game_folder, "img")

Bstart = 0 #背景起始值
