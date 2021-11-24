
<!-- image -->
<div align="center" id="top"> 
  <img src=https://www.researchgate.net/profile/Hebert-Perez-Roses/publication/251573416/figure/fig1/AS:298122283634689@1448089299412/A-simple-flow-shop-scheduling-problem-with-3-jobs-and-3-machines.png width="500" />
  &#xa0;
</div>

<h1 align="center"> flowshop-scheduling </h1>
<h2 align="center"> Solving the Flow-shop scheduling problem with bruteforce, jhonson's, neh and simulated annealing alogorithms </h2>

<!-- https://shields.io/ -->
<p align="center">
  <img alt="Top language" src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python">
  <img alt="Status" src="https://img.shields.io/badge/Status-done-green?style=for-the-badge">
  <img alt="Code size" src="https://img.shields.io/github/languages/code-size/KamilGos/flowshop-scheduling?style=for-the-badge">
</p>

<!-- table of contents -->
<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#package-content">Content</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#microscope-tests">Tests</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="#technologist-author">Author</a> &#xa0; | &#xa0;
</p>

<br>


## :dart: About ##
This repository contains set of alhorithm that solve the discrete processes segmentation problems.
You can find here the imprementation of the most popular approaches for [flowshop problems](https://en.wikipedia.org/wiki/Flow-shop_scheduling).
## :package: Content
 * [data](data) - directory with example data (problems to solve)
 * [bruteforce.py](bruteforce.py) - implementation of bruteforce algorithm for 2 and 3 machines
 * [johnsons.py](johnsons.py) - implementation of Johnson's algorithm for two and three machines
 * [neh.py](neh.py) - implementation of classical NEH algorithm as well as accelerated and modificated (insetion method) version
 * [simmulated_annealing.py](simulated_annealing.py) - simulated annealing using different approaches

## :checkered_flag: Starting ##
```bash
# Clone this project
$ git clone https://github.com/KamilGos/flowshop-scheduling

# Access
$ cd flowshop-scheduling

# Run the relevant script
$ sudo python3 bruteforce.py
$ sudo python3 johnsons.py
$ sudo python3 neh.py
$ sudo python3 simulated_annealing.py
```
## :microscope: Tests ##
<h2>bruteforce algorithm</h2>
<div align="center" id="put_id"> 
  <img src=images/bruteforce.png width="300" />
  &#xa0;
</div>

---

<h2>Jhonson's algorithm</h2>
<div align="center" id="put_id"> 
  <img src=images/jhonsons.png width="200" />
  &#xa0;
</div>

---

<h2>NEH algorithm</h2>
<div align="center" id="put_id"> 
  <img src=images/neh.png width="300" />
  &#xa0;
</div>

---

<h2>Simmulated annealing algorithm</h2>
<div align="center" id="put_id"> 
  <img src=images/simm_ann.png width="600" />
  &#xa0;
</div>

## :memo: License ##

This project is under license from MIT.

## :technologist: Author ##

Made with :heart: by <a href="https://github.com/KamilGos" target="_blank">Kamil Goś</a>

&#xa0;

<a href="#top">Back to top</a>


