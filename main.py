import sort
import select
import devideconquer
import random
import copy
import matplotlib.pyplot as plt
import time
import timeit
import numpy
from math import log, floor

if __name__ == "__main__":

    ran = range(1, 21, 1)
    random_select = [8.157947334134129e-06, 5.5263514198973105e-06, 2.4868581389537905e-05, 7.157940886724139e-05, 4.657924768199168e-05, 4.618450829485619e-05, 0.00015329046200429457, 0.00015539573873568345, 0.0002646069691765128, 0.00047289778578835556, 0.0008905320573777362, 0.001688300358778631, 0.004816610001827648, 0.0054635878573428, 0.011745207304626101, 0.03031506387343826, 0.10067670173136634, 0.07014255749806846, 0.3282517216229408, 0.7718633975403199]
    normal_select = [5.2631918284736315e-06, 9.868484678388057e-06, 2.4342262206690545e-05, 5.9737227253175703e-05, 0.00013105347652899344, 0.00041237107976090895, 0.0019284334859527383, 0.0011098755768293768, 0.0017310637923849774, 0.0042677906739135565, 0.020848687050745458, 0.023689494840164107, 0.12959149341883913, 0.2782182411439232, 0.5074460348494353, 0.826044931079161, 2.0639567281420628, 4.658987932948515, 10.851694964875433, 87.50734998159857]

    for k in range(len(ran)):
        random_select[k] = log(random_select[k] * 10**7, 2)
        normal_select[k] = log(normal_select[k] * 10**7, 2)

    random_fit = numpy.polyfit(ran, random_select, 1)
    normal_fit = numpy.polyfit(ran, normal_select, 1)

    random_p = numpy.poly1d(random_fit)
    normal_p = numpy.poly1d(normal_fit)

    plt.figure(figsize=(12, 9))
    plt.scatter(ran, random_select, label="random", color="blue")
    plt.scatter(ran, normal_select, label="normal", color="red")
    plt.plot(ran, random_p(ran), label="random_fit", color="blue", linewidth=2)
    plt.plot(ran, normal_p(ran), label="normal_fit", color="red", linewidth=2)
    plt.xlabel("$log{n}$")
    plt.ylabel("$\log{Running Time}$")
    plt.text(3,18,"k = %s" % normal_fit[0],
        bbox={'facecolor':'red','alpha':0.5,'pad':10})
    plt.text(15, 13,"k = %s" % random_fit[0],
        bbox={'facecolor':'blue','alpha':0.5,'pad':10})
    plt.legend()
    plt.show()

