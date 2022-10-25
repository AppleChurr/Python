# Remove Back Ground with U2net Model

## Install
    pip install rembg

## Model Path 
    C:\Users\JM-Sa\.u2net\

    U2net : https://drive.google.com/uc?id=1tCU5MM1LhRgGou5OpmpjBQbSrYIUoYab
    U2netp : https://drive.google.com/uc?id=1tNuFmLv0TSNDjYIkjEdeH1IWKQdUA4HR
    U2net_human_seg : https://drive.google.com/uc?id=1ZfqwVxu-1XWC1xU1GHIP-FM_Knd_AX5j
    U2net_cloth_seg : https://drive.google.com/uc?id=15rKbQSXQzrKCQurUjZFg8HqzZad8bcyz

### Model Train
    https://github.com/danielgatis/rembg/issues/193#issuecomment-1055534289

## Commend
    $ rembg i ./in.bmp ./out.bmp
    $ rembg i ./in.bmp ./out.bmp -m u2net
    $ rembg i ./in.bmp ./out_u2net.bmp -m u2net
    $ rembg i ./in.bmp ./out_u2netp.bmp -m u2netp
    $ rembg i ./in.bmp ./out_u2net_cloth_seg.bmp -m u2net_cloth_seg
    $ rembg i ./in.bmp ./out_u2net_human_seg.bmp -m u2net_human_seg

## Opencv Version
    $ pip install opencv-python==4.5.5.64

## Youtube
    https://www.youtube.com/watch?v=r29j8u7XwoM

