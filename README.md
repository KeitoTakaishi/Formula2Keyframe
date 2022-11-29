# About

This project generates KeyFrame using Easing Functions.
You can use KeyFrame generated for deforum stable diffusion and etc.

# How to use

`sudo ./examples/run.sh`

# Example
![sample](./examples/out.gif)

![sample](./examples/keyframe.png)


## Easing/easeOutCubic
```_.py
python ./main.py --out_path ./out/out.txt --formulra_type easing --ease_loop --amp 3.0 --freq 5 --offset 0.0 --easing easeOutCubic --preview
```
![sample](./examples/easeOutCubic_loop.png)

```_.py
python ./main.py --out_path ./out/out.txt --formulra_type easing --amp 3.0 --freq 5 --offset 0.0 --easing easeOutCubic --preview
```
![sample](./examples/easeOutCubic.png)


```_.py
python ./main.py --out_path ./out/out.txt --max_frames 600 --formulra_type noise --amp 3.0 --noise_loop 3 --preview
```
![sample](./examples/noise_3.png)

```_.py
python ./main.py --out_path ./out/out.txt --max_frames 600 --formulra_type noise --amp 3.0 --noise_loop 5 --preview
```
![sample](./examples/noise_5.png)

## Easing/noise

# Reference

- [easing function](https://easings.net/#easeOutExpo "easing function")
