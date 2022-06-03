# 字节跳动算法进阶办作业2
## 问题一：Deep struct 加入负例的问题
对于推荐系统来说，加入负样例对（x,y）是比较困难的事情，因为很难说用户x真的对物品y不敢兴趣，有可能只是在本系统里面，x还从来没有见过y。此时，简单的认为没有产生交互的（x,y）就是负样例是不太正确的。

因此，在Deep struct中，我认为可以针对path进行负采样，即针对一个物品y得到它的multi-path以后，随机采样m条不在其正样例里的path，参与计算。此时，损失函数可以考虑与multi-path相同，前面加上负号取反即可
## 问题二：Deep struct 加入item的embedding
目前，本系统中尚未加入item embedding,只考虑了user embedding以及path信息。

个人认为如果不考虑计算复杂度情况下，可以采用attention结构。对于每一层来说，可以使用attention来计算$emb(c_i)$的权重$a_i$
$$a=softmax(emb(I)*emb(c)^T)$$
其中emb(I)表示item embedding,emb(c)为前面层得到相应的embedding。

采用attention也是考虑到，一条path可能对应多个不同的视频，但是不同的视频信息应该是不一样的，虽然同样会因为单个视频会对应多个path，从而不同视频最终的编码不一样，但是仍然存在一定可能不同视频的path信息完全相同。因此，加入attention以后，不同的视频即使它们的path信息是一样的，它们最终得到的编码仍然是不一样的。

如果考虑计算复杂度，那么可以简单的将item embedding直接与user embedding 和 path embedding相加
## 问题三：每个视频的path数量选择
对于每个视频来说，其所对应的path数量应该是不同的。因为在multi-path里提到可能一个视频既是搞笑类又是宠物类，所以它可能对应多个path，那么显然对于一个视频来说，它的类别或者说是标签，数目应该是不同的。

所以我们可以考虑将当前的J作为path数量的上限，因为不设上限，可能会导致计算复杂度提升，然后再设定一个阈值s，只有当
$$p(c_{i,j}==π_j(y_i)|x_i,θ)>s$$
的情况下，这一条path才被认为是其一条path。这样，不同的视频其path的数量就将不同。