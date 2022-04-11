set xlabel 'K-points';
set ylabel 'Energy';
set ylabel rotate by 90;

set lmargin 13

unset key;
set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
unset grid
set yrange [-5:5] noreverse
set xrange [0.00:1.8911] noreverse
set key default

plot "bands_new2up.txt" every ::1::162 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::160.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::322.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::484.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::646.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::808.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::970.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::1132.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::1294.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::1456.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::1618.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::1780.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::1942.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::2104.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::2266.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::2428.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::2590.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::2752.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::2914.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::3076.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::3238.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::3400.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::3562.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::3724.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::3886.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::4048.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::4210.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::4372.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::4534.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::4696.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::4858.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::5020.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::5182.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::5344.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::5506.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::5668.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::5830.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::5992.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::6154.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::6316.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::6478.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::6640.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::6802.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::6964.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::7126.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::7288.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::7450.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2up.txt" every ::7612.0544::-318.13280000000003 using 1:2 with lines lc "black",\
"bands_new2dn.txt" every ::1::162 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::160.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::322.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::484.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::646.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::808.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::970.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::1132.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::1294.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::1456.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::1618.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::1780.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::1942.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::2104.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::2266.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::2428.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::2590.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::2752.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::2914.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::3076.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::3238.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::3400.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::3562.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::3724.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::3886.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::4048.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::4210.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::4372.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::4534.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::4696.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::4858.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::5020.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::5182.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::5344.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::5506.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::5668.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::5830.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::5992.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::6154.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::6316.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::6478.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::6640.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::6802.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::6964.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::7126.4457::-254.35090000000002 using 1:2 with lines lc "red",\
"bands_new2dn.txt" every ::7288.4457::-254.35090000000002 using 1:2 with lines lc "red",\


set terminal pdf color enhanced linewidth 5
set output 'bands.pdf'
replot

set output
set term windows
