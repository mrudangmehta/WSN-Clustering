# WSN-Clustering
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

**Results and comparision with Kmean algorithm**

**RESULT 1**

![Result1_dist](https://github.com/user-attachments/assets/f2a230fd-eb12-486e-ad16-dcbc3ca2e6bf)

![Result1_extm](https://github.com/user-attachments/assets/02e0679d-eb61-405b-b8e2-62440919aa79)


**RESULT 2**


![Result2_dis](https://github.com/user-attachments/assets/c9d2add3-9557-4e06-b1fe-e18eedf476bd)


![Result2_extm](https://github.com/user-attachments/assets/0dd04c22-bedd-42ce-8e9e-ba2cd923fcd7)


**RESULT 3**


![Result3_dis](https://github.com/user-attachments/assets/62cddd48-cf47-44ad-acb1-3b2445d211f4)


![Result3_extm](https://github.com/user-attachments/assets/002cfc54-2f13-449a-964e-2b0da62d8161)
