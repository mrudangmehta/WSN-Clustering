#*An Analysis tool for 3D Plot for WSN Clustering Algorithms comparision

import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import Tk, filedialog, Button, Frame, Canvas, Menu, Label, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def extract_parameters_v2(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_nodes = int(lines[0].strip().split(':')[1].strip())
        num_groups = int(lines[1].strip().split(':')[1].strip())
        mcluster_exec_time = float(lines[2].strip().split(':')[1].strip())
        kmeans_exec_time = float(lines[3].strip().split(':')[1].strip())
        mcluster_dist = float(lines[4].strip().split(':')[1].strip())
        kmeans_dist = float(lines[5].strip().split(':')[1].strip())

    return num_nodes, num_groups, mcluster_exec_time, kmeans_exec_time, mcluster_dist, kmeans_dist

def collect_data_v2(directory):
    data = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.txt'):
            file_path = os.path.join(directory, file_name)
            parameters = extract_parameters_v2(file_path)
            data.append(parameters)
    return data

def plot_distances(data, canvas):
    fig = plt.figure(figsize=(8, 6))

    num_nodes, num_groups, mcluster_exec_time, kmeans_exec_time, mcluster_dist, kmeans_dist = zip(*data)

    min_dist = min(min(mcluster_dist), min(kmeans_dist))
    max_dist = max(max(mcluster_dist), max(kmeans_dist))

    ax1 = fig.add_subplot(121, projection='3d')
    ax1.scatter(num_nodes, num_groups, kmeans_dist, c='r', marker='o', label='Kmeans Distance')
    ax1.set_xlabel('Number of Nodes')
    ax1.set_ylabel('Number of Groups')
    ax1.set_zlabel('Distance')
    ax1.set_title('Kmeans Distance')
    ax1.set_zlim(min_dist, max_dist)
    ax1.legend()

    ax2 = fig.add_subplot(122, projection='3d')
    ax2.scatter(num_nodes, num_groups, mcluster_dist, c='b', marker='^', label='mCluster Distance')
    ax2.set_xlabel('Number of Nodes')
    ax2.set_ylabel('Number of Groups')
    ax2.set_zlabel('Distance')
    ax2.set_title('mCluster Distance')
    ax2.set_zlim(min_dist, max_dist)
    ax2.legend()

    canvas.figure = fig
    canvas.draw()

def plot_execution_times(data, canvas, algorithm='both'):
    fig = plt.figure(figsize=(8, 6))

    num_nodes, num_groups, mcluster_exec_time, kmeans_exec_time, mcluster_dist, kmeans_dist = zip(*data)

    # Find the min and max values for execution times
    min_exec_time = min(min(mcluster_exec_time), min(kmeans_exec_time))
    max_exec_time = max(max(mcluster_exec_time), max(kmeans_exec_time))

    if algorithm == 'both' or algorithm == 'kmeans':
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.scatter(num_nodes, num_groups, kmeans_exec_time, c='y', marker='o', label='Kmeans Exec Time')
        ax1.set_xlabel('Number of Nodes')
        ax1.set_ylabel('Number of Groups')
        ax1.set_zlabel('Execution Time (mSec)')
        ax1.set_title('Kmeans Execution Time')
        ax1.set_zlim(min_exec_time, max_exec_time)  # Set z-axis limits for execution time
        ax1.legend()

    if algorithm == 'both' or algorithm == 'mcluster':
        ax2 = fig.add_subplot(122, projection='3d')
        ax2.scatter(num_nodes, num_groups, mcluster_exec_time, c='g', marker='^', label='mCluster Exec Time')
        ax2.set_xlabel('Number of Nodes')
        ax2.set_ylabel('Number of Groups')
        ax2.set_zlabel('Execution Time (mSec)')
        ax2.set_title('mCluster Execution Time')
        ax2.set_zlim(min_exec_time, max_exec_time)  # Set z-axis limits for execution time
        ax2.legend()

    canvas.figure = fig
    canvas.draw()


def plot_kmeans_distance(data, canvas):
    fig = plt.figure(figsize=(8, 6))

    num_nodes, num_groups, _, _, _, kmeans_dist = zip(*data)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(num_nodes, num_groups, kmeans_dist, c='r', marker='o', label='Kmeans Distance')
    ax.set_xlabel('Number of Nodes')
    ax.set_ylabel('Number of Groups')
    ax.set_zlabel('Distance')
    ax.set_title('Kmeans Distance')
    ax.legend()

    canvas.figure = fig
    canvas.draw()

def plot_mcluster_distance(data, canvas):
    fig = plt.figure(figsize=(8, 6))

    num_nodes, num_groups, _, _, mcluster_dist, _ = zip(*data)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(num_nodes, num_groups, mcluster_dist, c='b', marker='^', label='mCluster Distance')
    ax.set_xlabel('Number of Nodes')
    ax.set_ylabel('Number of Groups')
    ax.set_zlabel('Distance')
    ax.set_title('mCluster Distance')
    ax.legend()

    canvas.figure = fig
    canvas.draw()

def save_graph_as_jpg():
    if canvas.figure:
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                               filetypes=[("JPEG files", "*.jpg")],
                                               title="Save Graph as JPG")
        if file_path:
            canvas.figure.savefig(file_path, format='jpg')
            messagebox.showinfo("Save Graph", f"Graph saved as {file_path}")
    else:
        messagebox.showwarning("No Graph", "No graph to save. Please generate a plot first.")

def select_directory():
    global directory
    directory = filedialog.askdirectory(title="Select Directory")
    if directory:
        directory_label.config(text=f"Selected Folder: {directory}")
    return directory

def on_kmeans_exec_time_menu_click(canvas):
    if directory:
        data = collect_data_v2(directory)
        if data:
            plot_execution_times(data, canvas, algorithm='kmeans')
        else:
            messagebox.showerror("Error", "No data found in the directory.")
    else:
        messagebox.showwarning("No Directory", "Please select a directory first.")

def on_kmeans_dist_menu_click(canvas):
    if directory:
        data = collect_data_v2(directory)
        if data:
            plot_kmeans_distance(data, canvas)
        else:
            messagebox.showerror("Error", "No data found in the directory.")
    else:
        messagebox.showwarning("No Directory", "Please select a directory first.")

def on_mcluster_exec_time_menu_click(canvas):
    if directory:
        data = collect_data_v2(directory)
        if data:
            plot_execution_times(data, canvas, algorithm='mcluster')
        else:
            messagebox.showerror("Error", "No data found in the directory.")
    else:
        messagebox.showwarning("No Directory", "Please select a directory first.")

def on_mcluster_dist_menu_click(canvas):
    if directory:
        data = collect_data_v2(directory)
        if data:
            plot_mcluster_distance(data, canvas)
        else:
            messagebox.showerror("Error", "No data found in the directory.")
    else:
        messagebox.showwarning("No Directory", "Please select a directory first.")

def on_distance_comparison_menu_click(canvas):
    if directory:
        data = collect_data_v2(directory)
        if data:
            plot_distances(data, canvas)
        else:
            messagebox.showerror("Error", "No data found in the directory.")
    else:
        messagebox.showwarning("No Directory", "Please select a directory first.")

def on_exec_time_comparison_menu_click(canvas):
    if directory:
        data = collect_data_v2(directory)
        if data:
            plot_execution_times(data, canvas)
        else:
            messagebox.showerror("Error", "No data found in the directory.")
    else:
        messagebox.showwarning("No Directory", "Please select a directory first.")

# Create Tkinter GUI with canvas and buttons
root = Tk()
root.title("Kmeans vs mCluster Comparison")

directory = None

# Create a frame that adjusts to the canvas size
frame = Frame(root)
frame.pack(fill="both", expand=True)

# Create a canvas for the plot
canvas_area = Canvas(frame)
canvas_area.pack(fill="both", expand=True)

# Integrate matplotlib with Tkinter canvas
fig = plt.figure(figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=canvas_area)
canvas.get_tk_widget().pack(fill="both", expand=True)

# Create a label to show selected directory
directory_label = Label(root, text="No folder selected", pady=10)
directory_label.pack()

# Create a frame to hold all buttons in a single row
button_frame = Frame(root)
button_frame.pack(pady=10)

# Create buttons for selecting folder and plotting options
select_folder_button = Button(button_frame, text="Select Folder", command=select_directory)
select_folder_button.pack(side="left", padx=5)

kmeans_exec_time_button = Button(button_frame, text="Kmeans Exec Time", command=lambda: on_kmeans_exec_time_menu_click(canvas))
kmeans_exec_time_button.pack(side="left", padx=5)

kmeans_dist_button = Button(button_frame, text="Kmeans Distance", command=lambda: on_kmeans_dist_menu_click(canvas))
kmeans_dist_button.pack(side="left", padx=5)

mcluster_exec_time_button = Button(button_frame, text="mCluster Exec Time", command=lambda: on_mcluster_exec_time_menu_click(canvas))
mcluster_exec_time_button.pack(side="left", padx=5)

mcluster_dist_button = Button(button_frame, text="mCluster Distance", command=lambda: on_mcluster_dist_menu_click(canvas))
mcluster_dist_button.pack(side="left", padx=5)

distance_comparison_button = Button(button_frame, text="Distance Comparison", command=lambda: on_distance_comparison_menu_click(canvas))
distance_comparison_button.pack(side="left", padx=5)

exec_time_comparison_button = Button(button_frame, text="Exec Time Comparison", command=lambda: on_exec_time_comparison_menu_click(canvas))
exec_time_comparison_button.pack(side="left", padx=5)

save_graph_button = Button(button_frame, text="Save Graph as JPG", command=save_graph_as_jpg)
save_graph_button.pack(side="left", padx=5)

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Add file menu with various options
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Select Folder", command=select_directory)
file_menu.add_command(label="Plot Kmeans Execution Time", command=lambda: on_kmeans_exec_time_menu_click(canvas))
file_menu.add_command(label="Plot Kmeans Distance", command=lambda: on_kmeans_dist_menu_click(canvas))
file_menu.add_command(label="Plot mCluster Execution Time", command=lambda: on_mcluster_exec_time_menu_click(canvas))
file_menu.add_command(label="Plot mCluster Distance", command=lambda: on_mcluster_dist_menu_click(canvas))
file_menu.add_command(label="Distance Comparison", command=lambda: on_distance_comparison_menu_click(canvas))
file_menu.add_command(label="Execution Time Comparison", command=lambda: on_exec_time_comparison_menu_click(canvas))
file_menu.add_command(label="Save Graph as JPG", command=save_graph_as_jpg)

# Start the Tkinter main loop
root.mainloop()
