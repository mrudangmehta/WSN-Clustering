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
