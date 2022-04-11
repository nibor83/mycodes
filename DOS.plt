set xlabel 'Energy';
set ylabel 'States';
set ylabel rotate by 90;

set lmargin 13

unset key;
set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
unset grid
set xrange [0.0:1.25] noreverse
set yrange [0.0:400.0] noreverse
set key default

plot "DOS.dos1" every ::4::639 using 1:2 with lines lc "black" title "Total",\
"DOS.dos1" every ::4::639 using 1:3 with lines lc "red" title "Atom 1 total",\
"DOS.dos1" every ::4::639 using 1:4 with lines lc "green" title "Atom 1 S",\
"DOS.dos1" every ::4::639 using 1:4 with lines lc "green" title "Atom 1 S",\


set terminal pdf color enhanced linewidth 5
set output 'DOS.pdf'
replot

set output
set term windows
