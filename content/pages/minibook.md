Title: IPython Minibook
Slug: minibook

<div class="pure-g">
<div class="book-cover pure-u-1 pure-u-sm-1-3">
    <a href="https://www.packtpub.com/big-data-and-business-intelligence/learning-ipython-interactive-computing-and-data-visualization-sec"><img src="/images/minibook.jpg" alt="IPython minibook" /></a>
</div>

<div class="book-descr pure-u-1 pure-u-sm-2-3">
<div class="box">
    <h3>Learning IPython for Interactive Computing and Data Visualization</h3>
    <div class="sub-header-3">Packt Publishing (135 pages, 20$, 05/2013)</div>

    <p>
        This book is a beginner-level introduction to Python for data analysis:
    </p>

    <ul>
        <li>Interactive Python with <a href="http://ipython.org/">IPython</a></li>
        <li>Data analysis with <a href="http://pandas.pydata.org/">pandas</a></li>
        <li>Numerical computing with <a href="http://scipy.org/">NumPy/SciPy</a></li>
        <li>Data visualization with <a href="http://matplotlib.org/">matplotlib</a></li>
    </ul>
</div>
</div>
</div>

<div class="buttons-books buttons-book1">
    <a href="https://www.packtpub.com/big-data-and-business-intelligence/learning-ipython-interactive-computing-and-data-visualization">
        <button class="pure-button button-book2-order"><i class="fa fa-shopping-cart"></i>&nbsp;&nbsp;&nbsp;purchase</button>
    </a>
    <a href="https://github.com/ipython-books/minibook-code">
        <button class="pure-button button-book2-code"><i class="fa fa-code"></i>&nbsp;&nbsp;&nbsp;get the code</button>
    </a>
    <a href="https://github.com/ipython-books/minibook-data">
        <button class="pure-button button-book2-data"><i class="fa fa-database"></i>&nbsp;&nbsp;&nbsp;get the data</button>
    </a>
</div>


This book is a **beginner-level introduction to IPython** for *interactive Python programming*, *high-performance numerical computing*, and *data visualization*. It assumes nothing more than familiarity with Python. It targets developers, students, teachers, hobbyists who know Python a bit, and who want to learn IPython for the extended console, the Notebook, and for more advanced scientific applications.

## Table of contents

### Chapter 1: Getting started with IPython

### Chapter 2: Interactive Work with IPython

  * [Example 1](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter2/201-facebook-data-download.ipynb). We download and extract a social graph dataset (ego graphs of anonymous Facebook users, obtained on the [SNAP project](http://snap.stanford.edu/data/) from Stanford University). This example illustrates how to interact with the filesystem from IPython.

  * [Example 2](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter2/202-facebook-data-explore.ipynb). Here we explore with IPython the dataset downloaded in the previous example.

  * [Example 3](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter2/203-networkx.ipynb). We use the NetworkX package to process social graphs. We show how to explore simultaneously the data and a new Python module as well in an IPython interactive session.


### Chapter 3: Numerical Computing with IPython

  * [Example 1](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter3/301-vector-computations.ipynb). We introduce here the very basics of vector computing and NumPy multidimensional arrays. We show with a simple example what performance gains we can expect by using NumPy instead of pure Python loops.

  * [Example 2](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter3/302-multiplication-tables.ipynb). We generate multiplication tables with different methods, showing the performance benefits of using vectorized computations and broadcasting.

  * [Example 3](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter3/303-cities-data-explore.ipynb). We download and analyze a new dataset containing the geographical coordinates of all cities in the world, as well as the population for some of them. [This free dataset](http://www.maxmind.com/en/worldcities) has been created by [MaxMind](http://www.maxmind.com/).


### Chapter 4: Interactive Plotting and Graphical Interfaces

  * [Example 1](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter4/401-matplotlib-intro.ipynb). This is a short introduction to the most basic plotting features of Matplotlib.

  * [Example 2](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter4/402-world-map.ipynb). We use the world cities dataset from the previous example to create a human density world map with SciPy and Matplotlib.

  * [Example 3](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter4/403-histograms.ipynb). We show how to plot histograms of social data.

  * [Example 4](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter4/404-customization.ipynb). We show a few customization options with Matplotlib.

  * [Example 5](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter4/405-image-processing.ipynb). We show how to use PIL and SciPy for some basic image processing algorithms.

  * [Example 6](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter4/406-plot3d.ipynb). This is a 3D plot example with Matplotlib.


### Chapter 5: High Performance and Parallel Computing

  * [Example 1](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter5/501-parallel-computing.ipynb). We demonstrate the most basic interactive parallel computing features of IPython.

  * [Example 2](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter5/502-monte-carlo.ipynb). We show how Monte Carlo simulations can be parallelized with IPython.

  * [Example 3](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter5/503-mpi.ipynb). This is a simple MPI example executed from an interactive IPython session.

  * [Example 4](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter5/504-cython-eratosthenes.ipynb). We show how an imperative algorithm (Sieve of Eratosthenes) implemented in Python can be accelerated with Cython.

  * [Example 5](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter5/505-cython-numpy.ipynb). We show how to use Cython with NumPy-based algorithms for dramatic speed improvements.


### Chapter 6: Customizing IPython

  * [Example 1](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter6/601-lprof.ipynb). We show how to load IPython extensions, with an application to line-by-line profiling of Python code.

  * [Example 2](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter6/602-cpp.ipynb). We show how to create a new IPython extension. As an example, we create a very basic extension for writing and executing C++ code in the IPython notebook.

  * [Example 3](http://nbviewer.ipython.org/url/raw.github.com/ipython-books/minibook-code/master/chapter6/603-notebook-rich-display.ipynb). We illustrate the rich display features of the IPython notebook.
