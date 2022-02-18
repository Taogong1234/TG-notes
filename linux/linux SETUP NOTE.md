# linux setup
## refer to install.html

[install.html](install.html)

- google chrome can't work

- Fuck Anaconda, use [miniconda](https://docs.conda.io/en/latest/miniconda.html) instead

-  Zotero installation not working. use `snap` installation

## zsh setup
- install zsh from **apt**
- install [oh-my-zsh](https://ohmyz.sh/)
- configure [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md) 
- plug-in

## Miniconda packages

conda install numpy
conda install matplotlib
conda install jupyter

# python
## run from a python file
`python trst.py`
## interactive python programming
`jupyter-notebook`


# fortran

example fortran [code](fortran/fortran.f90)

## Compile and run

### test 1
compile
```
gfortran test1.f90 -o test1-single.exec
```

runown

# note
## 1.11
- find a way to fold/unfold 
```
./test1-single.exec
```

compile
```
mpif90 test1.f90 -o test1-parallel.exec
```

run
```
./test1-parallel.exec
```

### test 2
compile
```
gfortran test2.f90 -o test2.exec
```

run
```
./test2.exec
```

# zotero

## sync

- sync key information using zotero account, pdf via Nutstore (web dav)

- keywords for setup **zotero 坚果云**

# vscode 
## plug-in
### python 

### fortran 

- `Modern Fortran` and `FortranIntellense`

- Should install `fortran-language-server` via python.

## shortcut

`ctrl shift p`  command pannel

`ctrl shift v` preview markdown

# note
## 1.11
- find a way to fold/unfold markdown, fortran


### Comments from Zhouteng Ye

- for mpi related function, google to find more details. (Maybe not yet the time.)

- Learn to compile multiple files with `Makefile` is more fundimental and essential right now. Refer to the tutorial on the workstation.

- For remote work, first install `linux` on office PC, then install `Zerotier` on laptop and office, make sure to install 'openssh-server' on office. Then you should be able to ssh to office PC.
  
- to use jupyter on remote, google it.

- Linux basics, refer to the workstation mannual and use google.
  
- Steps for **Makefile**, first, compile multiple fortran files to an executable; second, compile all subroutines as a library, and link with main fortran file. After that, we go further into the Fortran solver
- ML class 台湾大学-李弘毅，斯坦福-feifei li。看完课程做作业顺便就熟悉python了