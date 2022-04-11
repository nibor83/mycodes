set xlabel 'Energy';
set ylabel 'States';
set ylabel rotate by 90;

set lmargin 13

unset key;
set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
unset grid
set xrange [0.4:1.00] noreverse
set yrange [-200.0:200.0] noreverse
set key default

plot "DOS.dos1dn" every ::4::646 using 1:(-$7) with lines lc "black" title "f down",\
"DOS.dos1up" every ::4::646 using 1:7 with lines lc "red" title "f up",\
#"DOS.dos1" every ::4::639 using 1:4 with lines lc "green" title "Atom 1 S",\
#"DOS.dos1" every ::4::639 using 1:4 with lines lc "green" title "Atom 1 S",\


set terminal pdf color enhanced linewidth 5
set output 'DOS.pdf'
replot

set output
set term windows
