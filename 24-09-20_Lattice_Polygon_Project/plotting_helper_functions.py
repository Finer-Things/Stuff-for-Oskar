from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.path import Path
import numpy as np
import seaborn as sns


def plot_setup(biggest_n, number_of_columns):
    number_of_rows = (biggest_n - 1) // number_of_columns + 1
    figure, axes = plt.subplots(number_of_rows, number_of_columns, figsize=(3*number_of_columns, 3*number_of_rows),
                                        sharex=True, 
                                        sharey=True, 
                                        subplot_kw={'aspect': 'equal'})
    return figure, axes


def create_plots(vertex_rule, biggest_n, number_of_columns, axes):
    # Plot Squares
    size_range = range(1, biggest_n + 1)
    # vertices = [(0,0), (n,0), (n,n), (0,n)]
    if biggest_n == 1:
        draw_polygon(*vertex_rule(1), axes = axes)
        # axes.fill([0,n,n,0], [0,0,n,n])
    elif biggest_n <= number_of_columns:
        for figure_index, square_size in enumerate(size_range):
            n = square_size
            draw_polygon(*vertex_rule(square_size), axes = axes[figure_index])
            # axes[figure_index].fill([0,n,n,0], [0,0,n,n])
    else:
        for figure_index, square_size in enumerate(size_range):
            row_index, column_index = divmod(figure_index, number_of_columns)
            draw_polygon(*vertex_rule(square_size), axes = axes[row_index, column_index])
            # axes[row_index, column_index].fill([0,n,n,0], [0,0,n,n])

    x_min = min([min([vertex[0] for vertex in vertex_rule(n)]) for n in range(1, biggest_n + 1)])
    x_max = max([max([vertex[0] for vertex in vertex_rule(n)]) for n in range(1, biggest_n + 1)])
    y_min = min([min([vertex[1] for vertex in vertex_rule(n)]) for n in range(1, biggest_n + 1)])
    y_max = max([max([vertex[1] for vertex in vertex_rule(n)]) for n in range(1, biggest_n + 1)])

    plt.yticks(range(y_min, y_max + 1))
    plt.xticks(range(x_min, x_max + 1))

    sns.despine()



def draw_polygon(*vertices, axes, interior_color: str="white", boundary_color="black"):
    """draws a polygon with interior and boundary points. Note: The interior points include boundary points"""
    if not vertices[-1] != vertices[0]:
        vertices += vertices[0]
    vertices = np.array([point for point in vertices])
    polygon = Polygon(vertices, closed=True) #, edgecolor='green', facecolor='blue'
    path = Path(vertices)
    
    if not axes:
        fig, axes = plt.subplots()
        axes.set_xlim(0, 5)
        axes.set_ylim(0, 5)
    
    # Generate lattice points
    x_min, x_max = min(vertices[:, 0]), max(vertices[:, 0])
    y_min, y_max = min(vertices[:, 1]), max(vertices[:, 1])
    x, y = np.meshgrid(np.arange(x_min, x_max + 1, 1), np.arange(y_min, y_max + 1, 1))
    mesh_points = np.vstack((x.flatten(), y.flatten())).T
    points_as_tuples = list(zip(x.flatten(), y.flatten()))

    # Check which points are inside the polygon (including the edge points)
    inside = path.contains_points(mesh_points, radius=.01)
    
    # Check which points are on the edge
    on_the_edge = [on_the_boundary(point, *vertices) for point in points_as_tuples]
    # boundary_points = np.unique(boundary_points, axis=0)
        
    axes.add_patch(polygon)
    axes.grid(True, ls=':')

    # Plot the interior points
    axes.scatter(mesh_points[inside][:, 0], mesh_points[inside][:, 1], s=10, c='white')
    

    # Plot the points on the boundary
    axes.scatter(mesh_points[on_the_edge][:, 0], mesh_points[on_the_edge][:,1], s=10, c='black')

 



def set_number_of_columns(number_of_plots, default_number_of_columns):
    if not default_number_of_columns:
        if number_of_plots <= 5:
            default_number_of_columns = number_of_plots
        elif number_of_plots % 4 == 0:
            default_number_of_columns = 4
        elif number_of_plots % 3 == 0:
            default_number_of_columns = 3
        elif number_of_plots % 4 == 3:
            default_number_of_columns = 4
        elif number_of_plots % 3 == 2:
            default_number_of_columns = 3
        else: default_number_of_columns = 5
    return default_number_of_columns
    


def on_the_boundary(point: tuple, *vertices)->bool:
    """Takes a point and vertices for a polygon and checks if the point is on the boundary. """
    for index, vertex in enumerate(vertices):
        endpoint_1, endpoint_2 = vertex, vertices[(index + 1) % len(vertices)]
        if is_between(point, endpoint_1, endpoint_2):
            return True
    return False


def is_between(point: tuple, endpoint_1: tuple, endpoint_2: tuple)->bool:
    """Checks if a point is between two other points."""
    # Finding slopes to compare
    rise_1 = point[1] - endpoint_1[1]
    rise_2 = endpoint_2[1] - point[1]
    run_1 = point[0] - endpoint_1[0]
    run_2 = endpoint_2[0] - point[0]

    # Determining window dimensions
    x_min = min(endpoint_1[0], endpoint_2[0])
    x_max = max(endpoint_1[0], endpoint_2[0])
    y_min = min(endpoint_1[1], endpoint_2[1])
    y_max = max(endpoint_1[1], endpoint_2[1])
    
    if not rise_1 * run_2 == rise_2 * run_1: 
        return False
    
    if not ((x_min <= point[0]) and (point[0] <= x_max)):
        return False
    
    if not ((y_min <= point[1]) and (point[1] <= y_max)):
        return False
    
    return True

    
