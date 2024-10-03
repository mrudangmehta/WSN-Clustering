# WSN-Clustering
*Wireless Sensor Networks (WSNs) consist of energy-constrained sensor nodes deployed for monitoring and data collection.
Efficient management and data processing techniques are crucial for optimizing WSN performance.
*Clustering algorithms enhance network performance by organizing sensor nodes into clusters.
*A simple and distributed clustering algorithm for WSNs is proposed, utilizing a three-pass localization-based approach.
*The algorithm assumes all nodes are localized using received signal strength from nearby nodes.
*Each node uses a localization table to execute the three-pass algorithm and build a global clustering map.
  First Pass: Estimate the desired number of clusters based on the total number of nodes and the average number within transmission range.
  Second Pass: Perform iterative clustering using nearest node grouping and furthest node selection as the next cluster head.
  Third Pass: Optimize clustering by regrouping based on total paths between cluster heads and member nodes.
*A dynamic cluster head selection mechanism is incorporated, considering:
  Residual energy, Communication range, Connectivity with other nodes.
*The algorithm adapts to changes in node characteristics and network conditions, ensuring efficient and balanced cluster formation.
*A GUI-based simulator for WSNs has been implemented using Python.
*The open-source code has been uploaded and shared with researchers for further use.
