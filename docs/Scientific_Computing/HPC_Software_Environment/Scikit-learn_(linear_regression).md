Scikit-learn is a Python package providing tools for data mining, data
analysis and machine learning. In this example, we\'ll show how to count
the number of dots embedded in an image using the sckit-learn linear
regression model.

### Generating training and testing datasets

Start by generating images of dots.  We\'ll generate 10k images for our
training set and 100 images to test our predictions. On Mahuika type the
following commands:

    wget https://raw.githubusercontent.com/mkienzle/MachineLearning/master/Scripts/ProduceSyntheticData/DrawDots.R
    ml R/3.6.1-gimkl-2018b
    Rscript DrawDots.R -n 10000 -r 0 -R 5 -s 123 -o train -c train.csv -w 40
    Rscript DrawDots.R -n 100 -r 0 -R 5 -s 234 -o test -c test.csv -w 40

[The images are saved under directories train/ and test/, respectively.
An example of image is test/img49.jpg.]{.s1}

    display test/img49.jpg

[![img49.jpg](https://support.nesi.org.nz/hc/article_attachments/360002364835/img49.jpg){width="100"
height="100"}]{.s1}

[which shows five, partially overlapping dots. Note that along with the
images, a comma separated values (csv) file (e.g. train/train.csv)
containing the number of dots (0 to 5) for each image is also
saved.]{.s1}

### Installing image processing software {#installing-image-processing-software .p1}

The images need to be slightly manipulated. For instance we expect all
the images to be black and white so we can collapse the red, green and
blue channel into one. We\'ll need OpenCV to this task:

    pip install opencv-python --user

### Running the model {#running-the-model .p1}

Our regression model

    wget https://raw.githubusercontent.com/mkienzle/MachineLearning/master/Scripts/Regression/classify.py

is encoded in classify.py. The corresponding lines in classify.py are
(Python code):

    clf = linear_model.LinearRegression()
    # now train
    clf.fit(trainingInput.reshape(-1, n0*n1), trainingOutput)

Here, trainingInput is the set of training arrays of size n0 (=40) and
n1 (=40). The arrays are flattened. The training output (trainingOutput)
is a vector of integer values (0-5).

We\'re now ready to train and test our model:

    #!/bin/bash -e
    #SBATCH --job-name regression-dots
    #SBATCH --ntasks 1
    #SBATCH --cpus-per-task 1
    #SBATCH --time 00:10:00
    #SBATCH --mem 512MB

    module load Python
    python classify.py --testDir=test --trainDir=train --save=someResults.png

Copy-paste the above and save in file classify.sl. Submit the Slurm
script classify.sl

    sbatch classify.sl

### Looking at the output {#looking-at-the-output .p1}

Upon completion of the run, expect to find file someResults.png in the
same directory as classify.py. This file contains the predictions for
the first 50 test images, which will vary for each training but the
result will look like: 

![someResults.png](https://support.nesi.org.nz/hc/article_attachments/360002470396/someResults.png)[(The
purple images have no dots.) With each image the number of dots is
displayed as well as the value inferred by the model in parentheses. The
inferred values are to be rounded to the nearest integer. Plot titles in
red indicate failures. Among the 100 test images, the correct number of
dots was found in 77 percent of the cases (the accuracy will change with
each training due to the randomness of the process). In many cases, the
predicted number of dots is off by no more than one unit. ]{.s1}

 
