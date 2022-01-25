
print gnuplot.view


set terminal png size 1280,941 crop 
set output 'testimage.png'

set xlabel "Time [sec]"
set ylabel "Radius [m]"
set title "My first plot with gnuplot"

plot sin(x)/x

set terminal svg size 400,300 enhanced fname ’arial’ fsize 10 butt solid
set key inside bottom right
set xlabel ’Time’
set title ’joli graph’
plot "Mini projet-Voiture.py" using 1:2 title ’Hum.’ with lines, "data.txt" using 1:3 title
’Temp’ with linespoints

