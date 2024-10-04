# *********************************************
# *          K-Means Clustering               *
# *                  by                       *
# *             Mrudang Mehta                    *
# *	         Himanshu Mazumdar                *
# *	        Date:- 18-March-2024              *
# *********************************************
import tkinter as tk
import random
from math import sqrt
import csv
from tkinter import Canvas
import os
import time
import threading as th
import math
from tkinter import filedialog

# ************************************************
class KMeansClustering(tk.Tk):

# ***************************************************************
#    Initialize variables for nodes, clusters, UI and display settings.
# ***************************************************************
    def __init__(self):
        super().__init__()
        self.title("K-Means Clustering")
        self.nods = []
        self.grphds = []
        self.nodsHd = []
        self.nodsHdNo = []
        self.myHd = []
        #self.chs = []
        
        self.nodSz = 10
        self.brushes = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'cyan', 'magenta']
        
        self.canvas = tk.Canvas(self, width=800, height=600, bg='black')
        self.canvas.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.canvas.pack()

        self.frame1 = tk.Frame(self)
        self.frame1.pack(side="top", fill="x", pady=5)
         
        self.label1 = tk.Label(self.frame1, text="Number of Nodes:")
        self.label1.pack(side="left", padx=5, pady=5)
        self.label2 = tk.Label(self.frame1, text="Number of Clusters:")
        self.label2.pack(side="left", padx=5, pady=5)

        self.textBox1 = tk.Entry(self.frame1)
        self.textBox1.insert(0,"12")
        self.textBox1.pack(side="left", padx=5, pady=5)
        self.textBox2 = tk.Entry(self.frame1)
        self.textBox2.insert(0,"3")
        self.textBox2.pack(side="left", padx=5, pady=5)

        self.btnNodes = tk.Button(self.frame1, text="Create Nodes", command=self.create_nodes)
        self.btnNodes.pack(side="left", padx=5, pady=5)
        
        self.btnKMeans = tk.Button(self.frame1, text="Run K-Means", command=self.get_k_means_cluster)
        self.btnKMeans.pack(side="left", padx=5, pady=5)

        self.btnImport = tk.Button(self.frame1, text="Import", command=self.importfile)
        self.btnImport.pack(side="left", padx=5, pady=5)


        self.btnExit = tk.Button(self.frame1, text="Exit", command=self.destroy)
        self.btnExit.pack(side="left", padx=5, pady=5)

        self.frame2 = tk.Frame(self)
        self.frame2.pack(side="top", fill="x", pady=5)

        self.btnNxtKmean = tk.Button(self.frame2, text="NextKMean", command=self.nextKmean)
        self.btnNxtKmean.pack(side="left", padx=5, pady=5)

        self.btnNxtKmean = tk.Button(self.frame2, text="WsnHsm", command=self.wsnH)
        self.btnNxtKmean.pack(side="left", padx=5, pady=5)

        self.btnNxtKmean = tk.Button(self.frame2, text="Save nodes to csv", command=self.save_nodes_to_csv)
        self.btnNxtKmean.pack(side="left", padx=5, pady=5)

        self.btnNxtKmean = tk.Button(self.frame2, text="Create Test Set", command=self.create_Test_Set)
        self.btnNxtKmean.pack(side="left", padx=5, pady=5)

        self.label3 = tk.Label(self.frame2, text="Total Distance: ")
        self.label3.pack(side=tk.RIGHT, fill=tk.X)

        self.label4 = tk.Label(self.frame2, text="Total Execution time: ")
        self.label4.pack(side=tk.RIGHT, fill=tk.X)

        self.bm = None
# *************************************************************
#        Clear the canvas to reset the drawing area.
# *************************************************************

    def clear_screen(self):
        self.canvas.delete("all")

# *************************************************************
#        Create random nodes and populate the canvas with them
# *************************************************************
        
    def create_nodes(self):
        global mx_nods
        try:
            mx_nods = int(self.textBox1.get())
            self.nodSz = 15
            self.clear_screen()
            self.nods = [(random.randint(self.nodSz, 800 - self.nodSz), random.randint(self.nodSz, 600 - self.nodSz)) for _ in range(mx_nods)]
            self.populate_node_2d()
            self.draw_nodes()
        except ValueError:
            print("Invalid number entered.")
            pass
# *************************************************************
#        Calculate and store the distances of each node to its nearest neighbor.
# *************************************************************  
    def populate_node_2d(self):
        self.nodsHd = []
        for nod in self.nods:
            distances = [sqrt((nod[0] - nod2[0]) ** 2 + (nod[1] - nod2[1]) ** 2) for nod2 in self.nods]
            distances.sort()
            self.nodsHd.append(distances[1])  # Smallest distance excluding itself
        a=123    
# *************************************************************
#        Draw nodes on the canvas.
# *************************************************************  
    def draw_nodes(self):
        for index, nod in enumerate(self.nods):
            x, y = nod[0], nod[1]
            # Draw the oval
            self.canvas.create_oval(x - self.nodSz, y - self.nodSz, x + self.nodSz, y + self.nodSz, fill="yellow")      
            # Calculate position for the text (centered)
            text_x = x
            text_y = y
            # Print the node number
            self.canvas.create_text(text_x, text_y, text=str(index), fill="black")
# *************************************************************
#        Draw node indices on the canvas (used after updating centroids).
# *************************************************************  
    def draw_nodes2(self):
        for index, nod in enumerate(self.nods):
            x, y = nod[0], nod[1]
            # Draw the oval
            # Calculate position for the text (centered)
            text_x = x
            text_y = y
            # Print the node number
            self.canvas.create_text(text_x, text_y, text=str(index), fill="black")
# *************************************************************
#        Calculate and return the total distance from nodes to their assigned cluster centroids.
# *************************************************************  
    def get_total_distance(self):
        dst = 0
        for i, nod in enumerate(self.nods):
            hd = self.grphds[self.nodsHd[i]]
            self.canvas.create_line(nod[0], nod[1], hd[0], hd[1], fill="white")
            dst += sqrt((nod[0] - hd[0]) ** 2 + (nod[1] - hd[1]) ** 2)
        return dst
# *************************************************************
#        Plot the cluster centroids and the nodes on the canvas.
# *************************************************************  
    def plot_k_means(self, brs):
        for index, hd in enumerate(self.grphds):
            x, y = hd[0], hd[1]
            # Draw the oval with specified fill color (brs)
            self.canvas.create_oval(x - self.nodSz, y - self.nodSz, x + self.nodSz, y + self.nodSz, fill=brs)
        
            # Calculate position for the text (centered)
            text_x = x
            text_y = y

            self.draw_nodes2()
            # Print the node number
            #self.canvas.create_text(text_x + 5, text_y + 5, text=str(index+1), fill="black",font=("Arial", 12, "bold"))

# *************************************************************
#        Initialize centroids randomly and start the K-Means clustering process.
# ************************************************************* 
    def get_k_means_cluster(self):
        global grps
        try:
            grps = int(self.textBox2.get())
            self.grphds = [(random.randint(self.nodSz, 500 - self.nodSz), random.randint(self.nodSz, 500 - self.nodSz)) for _ in range(grps)]
            self.after(100, self.timer_tick)
            #print("get k means cluster executed")
        except ValueError:
            pass
    
# *************************************************************
#        Assign nodes to the nearest centroids and update centroid positions.
# ************************************************************* 
    def update_grphds(self):
        self.nearest_nodes = []  # List to store tuples of (nearest node, index) for each centroid
        self.nodsHdNo = []
        grps = int(self.textBox2.get())
        for j, hd in enumerate(self.grphds):
            min_distance = float('inf')
            nearest_node = None
            nearest_index = None
            for i, nod in enumerate(self.nods):
                dst = sqrt((nod[0] - hd[0]) ** 2 + (nod[1] - hd[1]) ** 2)
                if dst < min_distance:
                    min_distance = dst
                    nearest_node = nod
                    nearest_index = i
            self.grphds[j] = nearest_node        
            self.nearest_nodes.append((nearest_node, nearest_index))
            self.nodsHdNo.append(nearest_index)
            #print("update_grphd executed")
        a=123   
# *************************************************************
#        Import node data from a CSV file and populate the canvas with nodes.
# ************************************************************* 
    def importfile(self):
        global data
        # Open the text file
        # Initialize Tkinter root (hidden window)
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        flnm = filedialog.askopenfilename(
            title="Select a CSV File",
            filetypes=[("CSV files", "*.csv")],  # Filter for CSV files
            initialdir="D:\\_July2024\\Mrudang_PhD\\KMeansPlus29072024"  # Set initial directory
        )

        if flnm:
            print(f"Selected file: {flnm}")
        else:
            print("No file selected")
            
        #flnm = "D:\\_July2024\\Mrudang_PhD\\KMeansPlus29072024\\wsnHsm1.csv"
        with open(flnm, 'r') as file:
            # Read lines from the file
            lines = file.readlines()

        # Initialize an empty list to store the data
        data = []

        # Iterate over each line
        for line in lines:
            # Split the line into elements based on spaces and store them in a list
            elements = line.strip().split(',')
            # Append the list of elements to the data list
            #data.append(elements)
            if len(elements) >= 3:
                data.append(elements)
            else:
                print("Skipping line:", line)

        try:
            mx_nods = int(self.textBox1.get())
            self.nodSz = 15
            self.clear_screen()
            j=1
            xc = int(data[j][1])
            yc = int(data[j][2])
            nodeno = int(data[j][0])
            nodehead = int(data[j][3])
            self.nods = [(int(data[i][1]), int(data[i][2])) for i in range(1, min(mx_nods, len(data))+1)]
            #self.nods = data
            self.populate_node_2d()
            self.draw_nodes()
        except ValueError:
            pass        
        a=123

# *************************************************************
#       Save the current nodes and their cluster assignments to a CSV file.
# ************************************************************* 
       
    def save_nodes_to_csv(self):  #filename='wsnHsm1.csv'
        try:
            # Initialize Tkinter root (hidden window)
            root = tk.Tk()
            root.withdraw()  # Hide the root window

            # Open a directory selection dialog
            selected_directory = filedialog.askdirectory(title="Select Directory to Save the File")

            # Define the file name
            file_name = "wsnHsm1.csv"

            # Create the full file path
            filename = os.path.join(selected_directory, file_name)

            #filename = "D:\\_July2024\\Mrudang_PhD\\KMeansPlus29072024\\wsnHsm1.csv"
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Number of Nodes:", mx_nods])
                writer.writerow(["Number of Groups:", grps])
                writer.writerow(['sno', 'x', 'y', 'nodHead', 'state', 'pow'])  # Writing the header
                for index, nod in enumerate(self.nods, start=1):
                    power = 100  # Example value for Power
                    state = 0  # Example value for State
                    node_head = self.nodsHdNo[self.nodsHd[index-1]] #data[index][3]  # Example value for NodeHead
                    #x, y, node_head,state,power = nod
                    writer.writerow([index-1, nod[0], nod[1], node_head, state, power])
   
            x=123   
             # Check if the file was created
            if os.path.exists(filename):
                print(f"Nodes saved to {filename}")
            else:
                print(f"File {filename} was not created.")
        except Exception as e:
            print(f"An error occurred while saving nodes: {e}")   

# *************************************************************
#       Save nodes and additional data to a CSV file (with custom filename).
# *************************************************************  
    def save_nodes_to_csv2(self, filename, execution_time):  #filename='wsnHsm1.csv'
        try:
            
            file = open(filename, mode='w', newline='')
            writer = csv.writer(file)
            writer.writerow(["Number of Nodes:", mx_nods])
            writer.writerow(["Number of Groups:", grps])
            writer.writerow(["Exec.Time(mSec):", execution_time])
            #writer.writerow(["Kmean Distance:", dst])
            writer.writerow(['sno', 'x', 'y', 'nodHead', 'state', 'pow'])  # Writing the header

            for index, nod in enumerate(self.nods, start=0):
                power = 100  # Example value for Power
                state = 0  # Example value for State
                node_head = self.myHd[index] #data[index][3]  # Example value for NodeHead
                #x, y, node_head,state,power = nod
                writer.writerow([index, nod[0], nod[1], node_head, state, power])
                #writer.writerow([index-1, x, y, node_head, state, power])

            x=123   
             # Check if the file was created
            if os.path.exists(filename):
                print(f"Nodes saved to {filename}")
                print(["Execution Time:", execution_time])
            else:
                print(f"File {filename} was not created.")
        except Exception as e:
            print(f"An error occurred while saving nodes: {e}")   

# *************************************************************
#       Create a test set by generating and saving random nodes to a CSV file.
# *************************************************************  
    def create_Test_Set(self):  
        global loop, sno
        # node_no,X,Y,ghd-K,ghd-m,
        # For number of nodes, 
        # 1. x is taken from 2 to 1000
        # 2. y =  (int) x(1/3)
        # 3. z = (y)3   
        # For Number of groups,
        # 1. a = (int) z(1/3)
        # 2. b =  random of a 
        # 3. c =  (z/2) * (b/a)
        
        #nofnd = self.generate_no_of_nodes()
        
        self.sno=0
        loop=0
        self.after(1000, self.timer2_tick)
        # tmr = th.Timer(1.0, self.timer2_tick)
        # tmr.start()

# *************************************************************
#       Timer event handler to update the cluster centroids and redraw the canvas.
# *************************************************************  
    def timer2_tick(self):
        global execution_time
#        count = 0
        node_no, num_groups = self.generate_values(201)
        self.textBox1.delete(0, tk.END)
        self.textBox2.delete(0, tk.END)
        self.textBox1.insert(0,node_no)
        self.textBox2.insert(0,num_groups)
        flnm = self.create_file_path(node_no,num_groups)
        print(flnm)
        self.create_nodes()

        start_time = time.time()

        self.get_k_means_cluster()
        self.update_grphds()
        self.myHd=[]
        for i, nod in enumerate(self.nods):
            dst2_min = float('inf')
            j_min = 0
            for j, hd in enumerate(self.grphds):
                dst2 = (nod[0] - hd[0]) ** 2 + (nod[1] - hd[1]) ** 2
                if dst2_min > dst2:
                    dst2_min = dst2
                    j_min = j
            self.myHd.append(j_min)

        # a1=self.nods
        # a2=self.grphds
        # a3=self.nodsHd
        # a4=self.nodsHdNo
        hd = self.grphds
        hd2 = self.myHd
        end_time = time.time()
        execution_time = end_time - start_time
#        count = count + 1
        self.label4.config(text=f"Total Execution time: {execution_time:.5f} seconds")
        self.update_grphds()
        self.update()
        self.save_nodes_to_csv2(flnm, execution_time)
        

        self.after(2000, self.timer2_tick)
        
        # tmr = th.Timer(3.0, self.timer2_tick)
        # tmr.start()
        k = 123
    
# *************************************************************
#      Generate no of nodes and no of groups randomly
# *************************************************************  
    def generate_values(self,nodes):
        yrn = max(2,int(math.pow(nodes, 1/3)))
        xrn = random.randint(2, yrn)
        # Generate number of nodes (z)
        z = max(2,int(math.pow(xrn, 3)))
        # Generate number of groups (a)
        a = int(math.pow(z, 1/3))
        # Randomly select b from 1 to a
        b = random.randint(1, a)
        # Calculate c = (z / 2) * (b / a)
        c = (z / 2) * (b / a)
        return z, int(c)  # Return number of nodes (x) and number of groups (c), rounded to an

# *************************************************************
#      Timer event handler to update the cluster centroids and redraw the canvas.
# ************************************************************* 
    def timer_tick(self):
        global label3
        global myHd
        global dst

        myHd = []

        start_time1 = time.time()  # Start the timer

        #self.plot_k_means("red")
        for i, nod in enumerate(self.nods):
            dst2_min = float('inf')
            j_min = 0
            for j, hd in enumerate(self.grphds):
                dst2 = (nod[0] - hd[0]) ** 2 + (nod[1] - hd[1]) ** 2
                if dst2_min > dst2:
                    dst2_min = dst2
                    j_min = j
            self.nodsHd[i] = j_min
        flg = True
        for j, hd in enumerate(self.grphds):
            sx, sy, nos = 0, 0, 0
            for i, nod in enumerate(self.nods):
                if self.nodsHd[i] == j:
                    sx += nod[0]
                    sy += nod[1]
                    nos += 1
            if nos != 0:
                xx = sx // nos
                yy = sy // nos
                if self.grphds[j][0] != xx or self.grphds[j][1] != yy:
                    flg = False
                self.grphds[j] = (xx, yy)
            a=123
        if flg:
            self.update_grphds()
            self.plot_k_means("white")
            dst = self.get_total_distance()
            # self.label3 = tk.Label(self.frame2, text="Total Distance: ")
            # self.label3.config(text="Total Distance: " + str(dst))
            self.label3.config(text="Total Distance: {:.2f}".format(dst))
            self.label3.pack()

            end_time1 = time.time()  # End the timer
            execution_time1 = end_time1 - start_time1

            self.label4.config(text="Total Execution Time: {:.4f} seconds".format(execution_time1))
            self.label4.pack()
            c=123
        else:
            self.after(100, self.timer_tick)

# *************************************************************
#     Advance to the next iteration of the K-Means algorithm and update the display.
# *************************************************************
    def nextKmean(self):
        self.importfile()  # Call the importfile function
        self.get_k_means_cluster()  # Call the get_k_means_cluster function
   
# *************************************************************
#     create a file path for each experiment
# *************************************************************    
    def create_file_path(self,node_no, num_groups):
        global file_name
        # Ensure m and n are integers
        n   =   node_no
        g   =   num_groups

        if not isinstance(n, int) or not isinstance(g, int):
            raise ValueError("Both m and n should be integers")

        # Get the absolute path of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Create the data directory path
        data_dir = os.path.join(script_dir, 'data')
        os.makedirs(data_dir, exist_ok=True)

        # Create the file path
        # file_name = f"data_{n}_{g}.csv"
        file_name = f"data_{n}_{g}_{self.sno}.txt"
        file_path = os.path.join(data_dir, file_name)
        
        self.sno += 1
        return file_path
# *************************************************************
#     Call for mCluster algorithm execution program
# *************************************************************
    def wsnH(self):
        import WsnHsmNewVer14 as wsnHsm

# *************************************************************
#     main block
# *************************************************************
if __name__ == "__main__":
    app = KMeansClustering()
    app.mainloop()

# ************************************************
