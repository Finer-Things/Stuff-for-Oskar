from matplotlib import pyplot as plt
import seaborn as sns

from plotting_helper_functions import set_number_of_columns, create_plots, plot_setup



def plot_squares(biggest_n: int, vertex_rule = lambda n: [(0,0), (n,0), (n,n), (0,n)], default_number_of_columns: int | None = None):
    """Plots squares in a grid shaded inside"""
    number_of_columns = set_number_of_columns(biggest_n, default_number_of_columns)
    
    # Plot setup
    figure, axes = plot_setup(biggest_n=biggest_n, number_of_columns=number_of_columns)
    
    # Plot Squares
    create_plots(vertex_rule=vertex_rule, biggest_n=biggest_n, number_of_columns=number_of_columns, axes=axes)

def plot_polygons(biggest_n: int, vertex_rule = lambda n: [(0,0), (n,0), (n,n), (0,n)], default_number_of_columns: int | None = None):
    """Plots polygons in a grid shaded inside"""
    number_of_columns = set_number_of_columns(biggest_n, default_number_of_columns)
    
    # Plot setup
    figure, axes = plot_setup(biggest_n=biggest_n, number_of_columns=number_of_columns)
    
    # Plot Squares
    create_plots(vertex_rule=vertex_rule, biggest_n=biggest_n, number_of_columns=number_of_columns, axes=axes)
