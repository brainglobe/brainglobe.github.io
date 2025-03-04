# Using supplied training data
cellfinder is released with a pre-trained cell candidate classification network, trained on approximately 
100,000 manually annotated cell candidates (with a roughly 50/50 split between cells and non-cells).

This data was acquired using [serial two-photon tomography](https://www.nature.com/articles/nmeth.1854). While you 
will likely need to retrain the network for your own data, we make the data available for a few reasons:

* You might want to use this data to test the training, or assess how much training data you may need
* You might want to retrain a different network (i.e., a different ResNet depth) than the one supplied (50-layer).
* You might want to retrain the network using a mixture of this data (of which there is a lot) and your data 
(of which you may not be able to generate as much).

The data is available [here](https://gin.g-node.org/cellfinder/training_data/raw/master/serial2p.tar.gz). 
To retrain the network using just this data, download the data, extract the tar archive, and then follow these steps:

:::{hint}
If you're using Windows, you will need to edit `training.yaml` so that the paths (in each `cube_dir` and `cell_def` 
entry) match windows paths (i.e. backslashes)
:::

* Activate your conda environment:

```text
conda activate cellfinder
```

* Navigate to the training data directory

```text
cd serial2p
```

* Start training

```text
cellfinder_train -y training.yaml -o training_output
```

The training will likely take a few minutes to get going; once the network starts, you should see something like this:

```text
Epoch 1/100
   1/6050 [..............................] - ETA: 0s - loss: 0.9579 - accuracy:    
   2/6050 [..............................] - ETA: 1:33:47 - loss: 3.1335 - accur   
   3/6050 [..............................] - ETA: 3:10:17 - loss: 2.6173 - accur   
   4/6050 [..............................] - ETA: 4:03:42 - loss: 2.2663 - accur   
   5/6050 [..............................] - ETA: 4:30:16 - loss: 2.0002 - accur
```

