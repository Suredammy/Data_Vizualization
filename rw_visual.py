import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    #Make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, graph = plt.subplots(figsize = (16, 9), dpi = 125)
    #Color the points.
    point_numbers = range(rw.num_points)
    #graph.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors = 'none', s = 1)
    #graph.scatter(rw.x_values, rw.y_values, s = 10)
    graph.plot(rw.x_values, rw.y_values, linewidth = 0.5)

    #Set chart title and label axes.
    graph.set_title("A Plot of Random Walk", fontsize= 24)      

    #Emphasize the first and last points.
    graph.scatter(0,0, c = 'red', edgecolors = 'none', s=50)
    graph.scatter(rw.x_values[-1], rw.y_values[-1], c= 'green', edgecolors = 'none', s =50)

    #Remove the axes.
    graph.get_xaxis().set_visible(False)
    graph.get_yaxis().set_visible(False)

    

    plt.show()      

    keep_running  = input("Make another walk? (y/n): ")
    if keep_running == "n" or keep_running == "N":
        break