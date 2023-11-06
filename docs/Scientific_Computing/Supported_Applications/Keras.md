---
created_at: '2019-07-24T04:30:33Z'
hidden: false
label_names: []
position: 34
title: Keras
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001075936
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>Keras is a modular and extensible API for building neural networks in Python. Keras is included with TensorFlow. Note that there are <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000997675-TensorFlow-on-CPUs" target="_self">CPU and</a> <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000990436-TensorFlow" target="_self">GPU versions</a> of TensorFlow, here we'll use TensorFlow 1.10 for GPUs, which is available as an environment module. </p>
<p>Keras can be used to solve a wide set of problems using artificial neural networks, including pattern recognition. Ultimately, a neural network is just a black box that takes input values and computes output values. Internally, the output values are computed using artificial neurons, which are modelled after biological neurons. The connections between neurons have different "weights", which when submitted to different stimuli will output different signals. With sufficient training, we can teach a neural network to acquire the correct weights, i.e. adjust the weights until the desired output is produced. </p>
<h2>Counting dots in images</h2>
<p>In this example, we will set up a neural network to count the number of dots embedded in an image.</p>
<h3>Generating the training and testing datasets</h3>
<p>Start by generating images of dots.  We'll generate 1000 images for our training set and 100 images to test our predictions. On Mahuika type the following commands to generate the training and testing data sets:</p>
<pre>wget <a href="https://raw.githubusercontent.com/mkienzle/MachineLearning/master/Scripts/ProduceSyntheticData/DrawDots.R">https://raw.githubusercontent.com/mkienzle/MachineLearning/master/Scripts/ProduceSyntheticData/DrawDots.R<br></a>ml <span class="s1">R/3.6.1-gimkl-2018b<br></span><span class="s1">Rscript DrawDots.R -n 1000 -r 0 -R 5 -s 123 -o train -c train.csv -w 40</span><br><span class="s1">Rscript DrawDots.R -n 100 -r 0 -R 5 -s 234 -o test -c test.csv -w 40</span></pre>
<p class="p1"><span class="s1">The images are saved under directories train/ and test/, respectively. An example of image is test/img49.jpg.</span></p>
<pre class="p1"><span class="s1">display test/img49.jpg</span></pre>
<p class="p1"><span class="s1"><img src="https://support.nesi.org.nz/hc/article_attachments/360002364835/img49.jpg" alt="img49.jpg" width="100" height="100"></span></p>
<p class="p1"><span class="s1">which shows five, partially overlapping dots. Note that along with the images, a comma separated values (csv) file (e.g. train/train.csv) containing the number of dots (0 to 5) for each image is also saved.</span></p>
<h3 class="p1">Installing image processing software</h3>
<p class="p1">The images need to be slightly manipulated. For instance we expect all the images to be black and white so we can collapse the red, green and blue channel into one. We'll need OpenCV to this task:</p>
<pre class="p1"><span class="s1">pip install opencv-python --user</span></pre>
<h3 class="p1">Running the model</h3>
<p class="p1">Our neural network</p>
<pre class="p1"><span class="s1">wget https://raw.githubusercontent.com/mkienzle/MachineLearning/master/Scripts/Conv2D/classify.py</span></pre>
<p class="p1">is encoded in classify.py. It is made of three convolution layers, each followed by max pooling. The convolution and max pooling layers are often applied to extract features in images. Finally the image is flattened as a 1D array and a dense layer, which returns an estimate of the number of dots as a single floating point number, is added. The corresponding lines in classify.py look like (Python code):</p>
<pre class="p1"><span class="s1">clf = keras.Sequential()</span><br><span class="s1">clf.add( keras.layers.Conv2D(</span><span class="s2">32</span><span class="s1">, kernel_size=(</span><span class="s2">3</span><span class="s1">,</span><span class="s2">3</span><span class="s1">), strides=(</span><span class="s2">1</span><span class="s1">,</span><span class="s2">1</span><span class="s1">),</span><br><span class="s1"><span class="Apple-converted-space">                             </span>padding=</span><span class="s2">'same'</span><span class="s1">, data_format=</span><span class="s2">'channels_last'</span><span class="s1">, activation=</span><span class="s2">'relu'</span><span class="s1">) )</span><br><span class="s1">clf.add( keras.layers.MaxPooling2D(pool_size=(</span><span class="s2">2</span><span class="s1">, </span><span class="s2">2</span><span class="s1">)) )</span><br><span class="s1">clf.add( keras.layers.Conv2D(</span><span class="s2">128</span><span class="s1">, kernel_size=(</span><span class="s2">3</span><span class="s1">,</span><span class="s2">3</span><span class="s1">), strides=(</span><span class="s2">1</span><span class="s1">,</span><span class="s2">1</span><span class="s1">),</span><br><span class="s1"><span class="Apple-converted-space">                             </span>padding=</span><span class="s2">'same'</span><span class="s1">, data_format=</span><span class="s2">'channels_last'</span><span class="s1">, activation=</span><span class="s2">'relu'</span><span class="s1">) )</span><br><span class="s1">clf.add( keras.layers.MaxPooling2D(pool_size=(</span><span class="s2">2</span><span class="s1">, </span><span class="s2">2</span><span class="s1">)) )</span><br><span class="s1">clf.add( keras.layers.Conv2D(</span><span class="s2">256</span><span class="s1">, kernel_size=(</span><span class="s2">3</span><span class="s1">,</span><span class="s2">3</span><span class="s1">), strides=(</span><span class="s2">1</span><span class="s1">,</span><span class="s2">1</span><span class="s1">),</span><br><span class="s1"><span class="Apple-converted-space">                             </span>padding=</span><span class="s2">'same'</span><span class="s1">, data_format=</span><span class="s2">'channels_last'</span><span class="s1">, activation=</span><span class="s2">'relu'</span><span class="s1">) )</span><br><span class="s1">clf.add( keras.layers.MaxPooling2D(pool_size=(</span><span class="s2">2</span><span class="s1">, </span><span class="s2">2</span><span class="s1">)) )</span><br><span class="s1">clf.add( keras.layers.Flatten() )</span><br><span class="s1">clf.add( keras.layers.Dense(</span><span class="s2">1</span><span class="s1">) )</span></pre>
<p class="p1"> </p>
<p class="p1">We're now ready to train and test our model:</p>
<pre class="p1"><span class="s1">#!/bin/bash -e</span><br><span class="s1">#SBATCH --job-name keras-dots</span><br><span class="s1">#SBATCH --partition gpu</span><br><span class="s1">#SBATCH --gres gpu:1</span><br><span class="s1">#SBATCH --ntasks 1</span><br><span class="s1">#SBATCH --cpus-per-task 1</span><br><span class="s1">#SBATCH --time 00:10:00</span><br><span class="s1">#SBATCH --mem 512MB</span><br><span class="s1">module load TensorFlow/1.10.1-gimkl-2017a-Python-3.6.3</span><br><span class="s1">python classify.py --testDir=test --trainDir=train --save=someResults.png</span></pre>
<p class="p1">Copy-paste the above and save in file classify.sl. Submit the Slurm script classify.sl</p>
<pre class="p1">sbatch classify.sl</pre>
<h3 class="p1">Looking at the output</h3>
<p class="p1">Upon completion of the run, expect to find file someResults.png in the same directory as classify.py. This file contains the predictions for the first 50 test images, which will vary for each training but the result will look like: </p>
<p class="p1"><img src="https://support.nesi.org.nz/hc/article_attachments/360002469116/someResults.png" alt="someResults.png"></p>
<p class="p1"><span class="s1">(The purple images have no dots.) With each image the number of dots is displayed as well as the value inferred by the model in parentheses. The inferred values are to be rounded to the nearest integer. Plot titles in red indicate failures. Among the 100 test images, the correct number of dots was found in 90 percent of the cases (the accuracy will change with each training due to the randomness of the process). The predicted number of dots should be off by no more than one unit in most cases. </span></p>
<p class="p1"> </p>
<p class="p1"> </p>
<p> </p>
<p> </p>