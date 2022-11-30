python ./main.py --out_path ./out/out_posx.txt --max_frames 1200 --formula_type noise --amp 0.5 --noise_loop 3
python ./main.py --out_path ./out/out_posy.txt --max_frames 1200 --formula_type noise --amp 0.5 --noise_loop 3
python ./main.py --out_path ./out/out_rotz.txt --max_frames 1200 --formula_type noise --amp 0.5 --noise_loop 3
python deforum_setting_file_generator.py -o ./setting_files/out1.txt --t ./template/template.txt --a rotation_3d_x rotation_3d_y rotation_3d_z --k ./out/out_rotx.txt ./out/out_roty.txt ./out/outrot_z.txt

python ./main.py --out_path ./out/out_posx.txt --max_frames 1200 --formula_type noise --amp 0.5 --noise_loop 3
python ./main.py --out_path ./out/out_posy.txt --max_frames 1200 --formula_type noise --amp 0.5 --noise_loop 3
python ./main.py --out_path ./out/out_rotz.txt --max_frames 1200 --formula_type noise --amp 0.5 --noise_loop 3
python deforum_setting_file_generator.py -o ./setting_files/out2.txt --t ./template/template.txt --a rotation_3d_x rotation_3d_y rotation_3d_z --k ./out/out_rotx.txt ./out/out_roty.txt ./out/outrot_z.txt

python ./main.py --out_path ./out/out_posx.txt --max_frames 1200 --formula_type noise --amp 0.5 --noise_loop 3
python ./main.py --out_path ./out/out_posy.txt --max_frames 1200 --formula_type noise --amp 0.5 --noise_loop 3
python ./main.py --out_path ./out/out_rotz.txt --max_frames 1200 --formula_type noise --amp 0.5 --noise_loop 3
python deforum_setting_file_generator.py -o ./setting_files/out3.txt --t ./template/template.txt --a rotation_3d_x rotation_3d_y rotation_3d_z --k ./out/out_rotx.txt ./out/out_roty.txt ./out/outrot_z.txt