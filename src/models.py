from torch import nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
import torch

class OneLayerGCN(nn.Module):
    def __init__(self, in_channels=34, out_channels=4):
        super().__init__()
        self.conv = GCNConv(in_channels, out_channels)

    def forward(self, x, edge_index):
        self.embeddings = {}
        x = self.conv(x, edge_index)
        self.embeddings['after_conv1'] = x

        return x
    

class TwoLayerGCN(nn.Module):
    def __init__(self, in_channels=34, hidden_channels=16, out_channels=4):
        super().__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)

    def forward(self, x, edge_index):
        self.embeddings = {}
        x = self.conv1(x, edge_index)
        self.embeddings['after_conv1'] = x
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        self.embeddings['after_conv2'] = x

        return x


class ThreeLayerGCN(nn.Module):
    def __init__(self, in_channels=34, hidden_channels1=16, hidden_channels2=16, out_channels=4):
        super().__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels1)
        self.conv2 = GCNConv(hidden_channels1, hidden_channels2)
        self.conv3 = GCNConv(hidden_channels2, out_channels)

    def forward(self, x, edge_index):
        self.embeddings = {}
        x = self.conv1(x, edge_index)
        self.embeddings['after_conv1'] = x
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        self.embeddings['after_conv2'] = x
        x = F.relu(x)
        x = self.conv3(x, edge_index)
        self.embeddings['after_conv3'] = x

        return x

class FourLayerGCN(nn.Module):
    def __init__(self, in_channels=34, hidden_channels1=16, hidden_channels2=16, hidden_channels3=16, out_channels=4):
        super().__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels1)
        self.conv2 = GCNConv(hidden_channels1, hidden_channels2)
        self.conv3 = GCNConv(hidden_channels2, hidden_channels3)
        self.conv4 = GCNConv(hidden_channels3, out_channels)

    def forward(self, x, edge_index):
        self.embeddings = {}
        x = self.conv1(x, edge_index)
        self.embeddings['after_conv1'] = x
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        self.embeddings['after_conv2'] = x
        x = F.relu(x)
        x = self.conv3(x, edge_index)
        self.embeddings['after_conv3'] = x
        x = F.relu(x)
        x = self.conv4(x, edge_index)
        self.embeddings['after_conv4'] = x

        return x

class FiveLayerGCN(nn.Module):
    def __init__(self, in_channels=34, hidden_channels1=16, hidden_channels2=16, hidden_channels3=16, hidden_channels4=16, out_channels=4):
        super().__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels1)
        self.conv2 = GCNConv(hidden_channels1, hidden_channels2)
        self.conv3 = GCNConv(hidden_channels2, hidden_channels3)
        self.conv4 = GCNConv(hidden_channels3, hidden_channels4)
        self.conv5 = GCNConv(hidden_channels4, out_channels)

    def forward(self, x, edge_index):
        self.embeddings = {}
        x = self.conv1(x, edge_index)
        self.embeddings['after_conv1'] = x
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        self.embeddings['after_conv2'] = x
        x = F.relu(x)
        x = self.conv3(x, edge_index)
        self.embeddings['after_conv3'] = x
        x = F.relu(x)
        x = self.conv4(x, edge_index)
        self.embeddings['after_conv4'] = x
        x = F.relu(x)
        x = self.conv5(x, edge_index)
        self.embeddings['after_conv5'] = x

        return x
