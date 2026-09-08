# Investigating the Impact of Layer Depth in GCNs on Node Classification

## Overview

This project is dedicated to exploring the behavior of Graph Convolutional Networks (GCNs) on the classic "Zachary's Karate Club" dataset. The primary goal is to analyze how increasing the number of convolutional layers affects classification accuracy and the quality of the resulting node embeddings.

In this work, the following experiments were conducted:
1.  Comparing the accuracy of GCN models with 1 to 5 layers.
2.  Visualizing node feature representations after each layer using t-SNE.
3.  Analyzing the stability of the models by running the training process multiple times with different random seeds.

## Repository Structure

-   `gcn-karate-club.ipynb`: The main Jupyter Notebook containing the complete experimental code.
-   `src/models.py`: A Python module containing the definitions of the GCN architectures (OneLayerGCN, TwoLayerGCN, ..., FiveLayerGCN).
-   `images/`: A directory for saving all generated plots.
    -   `karate_club_graph.png`: Visualization of the original Karate Club graph.
    -   `accuracy_vs_layer_number.png`: Plot showing accuracy as a function of the number of layers.
    -   `features_vs_layer_number.png`: t-SNE visualization of embeddings after each layer.
-   `requirements.txt`: A file listing all the required Python libraries.

## Dataset: Zachary's Karate Club

-   **Nodes:** 34 (members of the karate club)
-   **Edges:** 156 (directed social interactions)
-   **Classes:** 4 (different groups the members split into)
-   **Node Features:** One-hot encoded identity vectors (34 dimensions).

## Experimental Results

### 1. Accuracy and the Oversmoothing Effect

The primary experiment involved training several GCNs with an increasing number of layers and comparing their accuracy on a test set of nodes.

**Results:**
-   **1 Layer:** 60.0%
-   **2 Layers:** 80.0%
-   **3 Layers:** 83.3%
-   **4 Layers:** 63.3%
-   **5 Layers:** 50.0%

**Conclusion:**
The results clearly demonstrate the **oversmoothing phenomenon**, a known challenge in deep GCNs. While adding layers initially helps the model aggregate information from a wider neighborhood (improving accuracy from 60% to 83.3%), adding too many layers causes the node representations to become increasingly similar. This leads to a sharp decline in performance for models with 4 and 5 layers, as the nodes become less distinguishable.

### 2. Visualization of Embeddings (t-SNE)

t-SNE was used to project the high-dimensional node embeddings into 2D space for visualization.

**Observations:**
-   **Input Features:** The initial one-hot vectors show no discernible structure or grouping.
-   **After Layer 1:** The embeddings start to form clusters, showing the first signs of meaningful structure.
-   **After Layers 2 & 3:** The clusters become more distinct and well-separated, correlating with the peak in accuracy.
-   **After Layers 4 & 5:** The clusters begin to merge and collapse into a smaller, less separated space, visually confirming the **oversmoothing effect** observed in the accuracy metrics.

### 3. Model Stability Analysis

To assess stability, each model architecture was trained 30 times with different random seeds. The mean accuracy and standard deviation were then calculated.

| Model         | Mean Accuracy | Std Deviation |
|---------------|---------------|---------------|
| 1 Layer GCN   | 60.1%         | 0.006 (Very Low) |
| 2 Layer GCN   | 76.8%         | 0.018 (Low)      |
| 3 Layer GCN   | 73.3%         | 0.055 (Medium)   |
| 4 Layer GCN   | 68.1%         | 0.080 (High)     |
| 5 Layer GCN   | 52.1%         | 0.112 (Very High)|

**Conclusion:**
-   The **1-layer GCN** is the most stable but offers the lowest peak accuracy.
-   The **2-layer GCN** achieves a good balance, providing high average accuracy (76.8%) with low variance.
-   While the 3-layer GCN can achieve higher peak performance (as seen in the single run), it is significantly less stable than its shallower counterpart. The 4 and 5-layer models are both inaccurate and highly unstable.

## Final Conclusion

Based on this study, for the Karate Club dataset and similar small graphs:

-   The optimal architecture is the **2-layer GCN**. It provides the best trade-off between high accuracy and stable training.
-   **Deeper GCNs (4+ layers) are counterproductive** due to the oversmoothing effect, which causes node embeddings to converge and reduces classification performance.
-   The **3-layer GCN** can sometimes outperform the 2-layer version but is much more sensitive to initialization and other random factors, making it less reliable.

## How to Run

1.  **Clone the repository** (or download the files).
2.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Jupyter Notebook:**
    ```bash
    jupyter notebook gcn-karate-club.ipynb
    ```
    You can run the cells sequentially to reproduce the entire experiment, including training, evaluation, and generating the plots.