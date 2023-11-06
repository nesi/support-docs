---
created_at: '2018-12-17T04:31:59Z'
hidden: true
label_names: []
position: 20
title: 'MATLAB: Parallel Operations'
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000666055
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<div class="paragraphNode wrappable"> </div>
<h1 class="paragraphNode wrappable">Passive Parallelisation</h1>
<div class="paragraphNode wrappable"> </div>
<div class="paragraphNode wrappable"> </div>
<div class="paragraphNode wrappable"> </div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">Arrays and matrices</span></span></div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">•Basic information: ISFINITE, ISINF, ISNAN, MAX, MIN</span></span></div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">•Operators: +, -, .*, ./, .\, .^, *, ^, \ (MLDIVIDE), / (MRDIVIDE)</span></span></div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">•Array operations: PROD, SUM</span></span></div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">•Array manipulation: BSXFUN, SORT</span></span></div>
<div class="paragraphNode wrappable"> </div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">Linear algebra</span></span></div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">•Matrix Analysis: DET, RCOND</span></span></div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">•Linear Equations: CHOL, INV, LDL, LINSOLVE, LU, QR</span></span></div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">•Eigenvalues and singular values: EIG, HESS, SCHUR, SVD, QZ</span></span></div>
<div class="paragraphNode wrappable"> </div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">Elementary math</span></span></div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">•Trigonometric: ATAN2, COS, CSC, HYPOT, SEC, SIN, TAN, including variants for radians, degrees, hyperbolics, and inverses.</span></span></div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">•Exponential: EXP, POW2, SQRT</span></span></div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">•Complex: ABS</span></span></div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">•Rounding and remainder: CEIL, FIX, FLOOR, MOD, REM, ROUND</span></span></div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">•LOG, LOG2, LOG10, LOG<dfn class="dictionary-of-numbers">1P</dfn>, EXPM1, SIGN, BITAND, BITOR, BITXOR</span></span></div>
<div class="paragraphNode wrappable"> </div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">Special Functions</span></span></div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">•ERF, ERFC, ERFCINV, ERFCX, ERFINV, GAMMA, GAMMALN</span></span></div>
<div class="paragraphNode wrappable"> </div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">Data Analysis</span></span></div>
<div class="paragraphNode wrappable"><span class="textBox"><span class="textWrapper">•CONV2, FILTER, FFT and IFFT of multiple columns or long vectors, FFTN, IFFTN</span></span></div>
<div class="paragraphNode wrappable"> </div>
<h1 class="paragraphNode wrappable">Explicit Parallelisation</h1>
<h2>Parfor</h2>
<h1 class="paragraphNode wrappable">GPUs</h1>
<h1 class="paragraphNode wrappable"> </h1>
<h1 class="paragraphNode wrappable">Arrays - Sparse, Dense and GPU </h1>
<h1>Performance</h1>
<p>export TMPDIR=tmp</p>
<div class="paragraphNode wrappable"> </div>
<div class="paragraphNode wrappable">training_procedure_step3_21.m</div>
<div class="paragraphNode wrappable">training_procedure_bf33_40.m</div>
<div class="paragraphNode wrappable"> </div>
<div class="paragraphNode wrappable"> </div>
<div class="paragraphNode wrappable"> </div>
<div class="paragraphNode wrappable">Recursive script</div>
<div class="paragraphNode wrappable">
<pre>#!/bin/bash -e<br><br>#SBATCH --job-name=recusionTest_n<br>#SBATCH --time=00:02:00<br>#SBATCH --ntasks=1<br>#SBATCH --cpus-per-task=2<br>#SBATCH --mem=100<br>#SBATCH --hint=nomultithread<br><br>maxIterations=3<br><br>if [[ -z "${CURRENT_ITERATION}" ]]<br>then<br> export CURRENT_ITERATION=0<br>else<br> export CURRENT_ITERATION=$((CURRENT_ITERATION+1))<br> echo "Iteration ${CURRENT_ITERATION}/${maxIterations}"<br> if [[ $CURRENT_ITERATION -gt $maxIterations ]]<br> then<br> echo "Max iterations hit"<br> exit 0<br> fi<br>fi<br><br>echo "Looking for data in output"<br><br>if [ -e output/data.txt ]<br>then<br> echo "file exists"<br> runCount=$(sed 's/[^0-9]*//g' output/data.txt)<br> echo "this is the ${runCount} run of this job"<br> echo "Doing job stuff"<br> echo "Writing job output"<br><br>echo "This is run number [$(($runCount + 1))]" &gt; output/data.txt<br><br>echo "Having a nap"<br> sleep 20<br><br>#sbatch self<br> echo "Calling next job"<br> sbatch /$0<br>else<br> echo "file doesn't exist"<br> echo "Ending Chain"<br> exit<br>fi</pre>
</div>
<div class="paragraphNode wrappable"> </div>
<div class="paragraphNode wrappable">Looping</div>
<div class="paragraphNode wrappable">
<pre>#!/bin/bash<br><br>submitJob () {<br><br>cat &lt;&lt;EOF &gt; submit.sl<br>#!/bin/bash -e<br><br>#SBATCH --job-name mmpp_$1_$2<br>#SBATCH --time 10:00:00<br>#SBATCH --mem-per-cpu=1500<br>#SBATCH --ntasks=1<br>#SBATCH --cpus-per-task=$2<br>#SBATCH --output=output2/mmpp_$1_$2.out<br><br>module load MATLAB<br><br>export TMPDIR<br><br>matlab -nodisplay -r "pc = parcluster('local');pc.JobStorageLocation = getenv('TMPDIR');parpool(pc, str2num(getenv('SLURM_CPUS_PER_TASK')));matMulParPool($1)"<br><br>EOF<br>sbatch submit.sl<br>}<br><br>#mats=( 100 200 400 800 1600 3200 6400 12800 )<br>cores=( 2 4 8 16 32 )<br><br>mats=( 100 )<br><br>for c in "${cores[@]}"<br>do<br> :<br> for m in "${mats[@]}"<br> do<br> :<br> submitJob $m $c<br> done<br>done</pre>
<p> </p>
<p>CD changing</p>
</div>
<pre>#!/bin/bash -e<br><br>#SBATCH --job-name MaryTest_C2_N5_M20<br>#SBATCH --time 06:00:00<br>#SBATCH --mem-per-cpu 1500<br>#SBATCH --mail-type=ALL # Optional: Send email notifications<br>#SBATCH --cpus-per-task=2<br>#SBATCH --mail-user=callum.walley@nesi.org.nz # Use with --mail-type option<br>#SBATCH --ntasks=1<br>#SBATCH --output=%x_out.log<br>#SBATCH --error=%x_error.err<br><br>module load MATLAB<br><br>mkdir -p outputs/${SLURM_JOB_NAME}<br>cd outputs/${SLURM_JOB_NAME}<br><br>#Job run<br>srun matlab -nodisplay -r "addpath(genpath('../../../DL1014'));run_exp(5,20)"<br><br>#MOVE FILES INTO NEW DIRECTORY<br>mv ../../${SLURM_JOB_NAME}_out.log ${SLURM_JOB_NAME}_out.log<br>mv ../../${SLURM_JOB_NAME}_error.err ${SLURM_JOB_NAME}_error.err</pre>
<p> Validation</p>
<pre dir="ltr"><code>#!/bin/bash
#
# Validation Script
# Checks all your jobs completed successfully 
#
#
#
# Just fill in the sections below each comment.
#  
#
#
# Callum Walley 
# 2019/01/11


#Location of files to be validated.
outputDir="/nesi/project/nesi99999/" 

echo "Validating Files...."

#Range of expected file size.In bytes.
minSize=0
maxSize=65000000

#Number range of jobs to check
firstIndex=10
lastIndex=20

#What to do if missing file is found.
onMissing(){


    echo "Doing the thing"


} 

for (( n=${firstIndex}; n&lt;=${lastIndex}; n++ ))
do

#Specify naming scheme of files. Where ${n} will iterate across all indices.
filename="Job_${n}.cas" 

if [ ! -e ${outputDir}${filename} ]; then

    echo "${filename} does not exist!"
    onMissing ${n}

elif [ $(wc -c &lt;"${outputDir}${filename}") -le $minSize ]; then

    echo "${filename} is too small! ($(wc -c &lt; ${outputDir}${filename}) bytes)"
    onMissing ${n}

elif [ $(wc -c &lt;"${outputDir}${filename}") -ge $maxSize ]; then

    echo "${filename} is too big! ($(wc -c &lt; ${outputDir}${filename}) bytes)" 
    onMissing ${n}

fi

done
echo "Done!"</code></pre>