# Novel Approach for WSN-Clustering
**Abstract**
1. WSNs consist of energy-constrained sensor nodes for monitoring and data collection.
2. Efficient management and data processing optimize WSN performance.
3. Clustering algorithms improve network performance by organizing nodes into clusters.
4. A distributed clustering algorithm is proposed using a three-pass localization approach.
5. The algorithm assumes nodes are localized via received signal strength from nearby nodes.
6. Each node uses a localization table to build a global clustering map through the three-pass algorithm:
   - **First Pass**: Estimate the number of clusters based on node count and average within transmission range.
   - **Second Pass**: Perform iterative clustering using nearest node grouping and furthest node selection as the next cluster head.
   - **Third Pass**: Optimize clustering by regrouping based on paths between cluster heads and member nodes.
7. Dynamic cluster head selection considers residual energy, communication range, and connectivity.
8. The algorithm adapts to changing node characteristics and network conditions for balanced cluster formation.
9. A GUI-based WSN simulator has been implemented in Python.
10. Open-source code has been shared with researchers for further use.


The algorithm assumes all nodes are localized as suggested in https://github.com/hsmazumdar/WSN_Localizer/tree/main using received signal strength from nearest nodes. Based on this localization data, each node executes the proposed three-pass algorithm to construct a comprehensive clustering map of all nodes in the network. (1) In the first pass, an estimation is made for the desired number of clusters based on the total number of nodes and the average number of nodes within the transmission range of each node. (2) The second pass involves iterative clustering using nearest node grouping and furthest node selection as the subsequent cluster head. (3) Finally, in the third pass, clustering is optimized by regrouping nodes based on the total paths between cluster heads and their member nodes.

Notably, the proposed algorithm incorporates a dynamic cluster head selection mechanism that takes into account factors such as residual energy, communication range, and connectivity with other nodes. This adaptive mechanism enables the algorithm to accommodate changes in node characteristics and network conditions, thereby ensuring efficient and well-balanced cluster formation.


## Mathematical Formulation for Clustering
![image](https://github.com/user-attachments/assets/f8736e12-7085-4fe4-a7a1-df2b45f7461e)



![image](https://github.com/user-attachments/assets/2c930fbc-1a2f-4f87-b9f8-13d40755a836)



![image](https://github.com/user-attachments/assets/f28ec931-af5b-4743-8ff1-0e5966ba16fd)



![image](https://github.com/user-attachments/assets/0e0b2692-a394-4cc0-a611-e688afe27f5c)






## Algorithm

**Start**

1. `nodsz` = Get number of nodes
2. `grpssz` = Get number of clusters
3. `grpsz[]` = Get node size of each cluster (temporary)
4. `dist[][]` = Get distance between all nodes
5. Initialize `i = 0`
6. Initialize `best` to a very large number

**Loop 1**:

7. `chn` = Get the furthest node as cluster head node `ch_i`
8. Mark `grpsz[i]` nearest cluster members' state as `-1`
9. Choose a new cluster head in the center of gravity of the `i_th` cluster as `ch_i`
10. Increment `i = i + 1`
11. If `i < grpssz`, go to **Loop 1**

12. Calculate `goodness` = Sum of distances between all cluster heads and their members
13. Include nearest members of other groups to each cluster head, excluding from the current group

14. If `best > goodness`, go to **Loop 1**

15. Update `grpsz[]`

**Result**: Mark all cluster heads with their respective cluster members

**End**

## Results and comparision with Kmean algorithm

**KMean Clustering Algorithm: Deployment and Clustering**
![kmean_deployment](https://github.com/user-attachments/assets/35321615-d2a3-43b9-8d84-601e9bf0eda1)

Figure-1: WSN Deployment for evaluation of KMean clustering algorithm



![Kmean_result](https://github.com/user-attachments/assets/2a027d3b-a1a7-42b0-8583-a0b5f3b65b8e)

Figure-2: Simulation of KMean Clustering using our interactive GUI

**Proposed Clustering Algorithm: Deployment and Clustering**

Deployment for Kmean clustering and Proposed algorithm's clustering is same. We have saved the coordinates into the csv file.

Deployment (coordinates are same as used for Kmean clustering)

![ClusterHsm](https://github.com/user-attachments/assets/9bcd4cc5-350b-4cea-b624-d823cccb830c)

Figure-3 WSN Deployment- This deployment is same as in Figure-1

Clustering Phase

![ClusterHsm_cluster](https://github.com/user-attachments/assets/33fd207f-4398-4304-879f-92a8be44bc9b)

Figure-4 Initial Clustering in Wireless Sensor Networks: An Interactive GUI-Based Simulation

Optimization of the Clustering Phase

![ClusterHsm_opt](https://github.com/user-attachments/assets/e2245882-925d-4fa3-8bf4-d1add0358e4f)

Figure-5 Optimized Clustering in Wireless Sensor Networks: An Interactive GUI-Based Simulation


**RESULT 1**

![Result1_dist](https://github.com/user-attachments/assets/f2a230fd-eb12-486e-ad16-dcbc3ca2e6bf)

Figure-6 KMean and Proposed Approach WSN Clustering Distance Comparision for Dataset 1


**RESULT 2**


![Result2_dis](https://github.com/user-attachments/assets/c9d2add3-9557-4e06-b1fe-e18eedf476bd)

Figure-8 KMean and Proposed Approach WSN Clustering Distance Comparision for Dataset 2



![Result3_dis](https://github.com/user-attachments/assets/62cddd48-cf47-44ad-acb1-3b2445d211f4)

Figure-9 KMean and Proposed Approach WSN Clustering Distance Comparision for Dataset 3




### Summary of Kmeans vs mCluster Comparison Based on the Provided Visuals:

1. **Distance Comparison (Results 1,2 and 3)**:
   - **Kmeans Distance**: 
     - Shows a higher distance between nodes and their cluster heads.
     - As the number of nodes and groups increases, the distance tends to increase significantly, peaking at around 150,000 units.
     - The distribution of distances appears more scattered across various node and group sizes.
   - **mCluster Distance**: 
     - Exhibits lower overall distances between nodes and their cluster heads compared to Kmeans.
     - Even with a larger number of nodes and groups, mCluster maintains lower distances, clustering more tightly.
     - The distance stays consistently lower, indicating better optimization in terms of proximity within clusters.

**3D Clustering Video**
In this paper, we used clustering for 2D elements. We have extended this for 3D and more. 



https://github.com/user-attachments/assets/673ce727-ba3f-4024-9705-455274b01a20


### Conclusion:
- **Kmeans** shows higher distances and execution times, indicating that while it clusters data, it may not be as efficient as mCluster for large datasets.
- **mCluster** consistently performs better in both distance reduction and execution time, making it a more optimized choice for clustering in Wireless Sensor Networks, especially in scenarios with a large number of nodes and clusters.
