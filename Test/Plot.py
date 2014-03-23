__author__ = 'zm'

import Gnuplot, Gnuplot.funcutils
import getopt, sys

# The port number of each switch in fat-tree topology
K = 8

opts, args = getopt.getopt(sys.argv[1:], "K:", ["K=",])
for o, a in opts:
    if o in ("-K", "--K"):
        K = int(a)

Xrange=1100
Yrange=105

g = Gnuplot.Gnuplot(debug=1)

g("set autoscale")
g("set xlabel \"Throughput (Mbps)\" font \", 20\" offset 0, -0.5")
g("set ylabel \"CDF (%)\" font \", 20\"")
g("set xrange [0 : %d]" % Xrange)
g("set yrange [0 : %d]" % Yrange)
g("set ytics font \", 20\"")
g("set xtics font \", 20\"")
g("set key box right bottom")
g("set term postscript color enhanced solid")
g("set output \"cdf_K%d_a.eps\"" % K)
g("set key spacing 4.0 nobox right bottom font \",25\"")
g("plot \"K%d_S100_L100_a1_plot.dat\" using 1:($2 * 100) title \"a1\"w linespoint 4 lt rgb \"red\" lw 2.5," % K
  "\"K%d_S100_L100_a5_plot.dat\" using 1:($2 * 100) title \"a5\"w linespoint 6 lt rgb \"blue\" lw 2.5," % K
  "\"K%d_S100_L100_a10_plot.dat\" using 1:($2 * 100) title \"a10\"w linespoint 8 lt rgb \"green\" lw 2.5," % K)
