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

plot "bands_new2.txt" every ::1::162 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::164::325 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::327::488 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::490::651 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::653::814 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::816::977 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::979::1140 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::1142::1303 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::1305::1466 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::1468::1629 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::1631::1792 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::1794::1955 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::1957::2118 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::2120::2281 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::2283::2444 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::2446::2607 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::2609::2770 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::2772::2933 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::2935::3096 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::3098::3259 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::3261::3422 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::3424::3585 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::3587::3748 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::3750::3911 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::3913::4074 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::4076::4237 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::4239::4400 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::4402::4563 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::4565::4726 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::4728::4889 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::4891::5052 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::5054::5215 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::5217::5378 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::5380::5541 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::5543::5704 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::5706::5867 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::5869::6030 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::6032::6193 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::6195::6356 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::6358::6519 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::6521::6682 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::6684::6845 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::6847::7008 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::7010::7171 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::7173::7334 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::7336::7497 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::7499::7660 using 1:2 with lines lc "black",\
"bands_new2.txt" every ::7662::7823 using 1:2 with lines lc "black",\


set terminal pdf color enhanced linewidth 5
set output 'bands2.pdf'
replot

set output
set term windows
