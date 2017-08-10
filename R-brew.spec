#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-brew
Version  : 1.0.6
Release  : 38
URL      : http://cran.r-project.org/src/contrib/brew_1.0-6.tar.gz
Source0  : http://cran.r-project.org/src/contrib/brew_1.0-6.tar.gz
Summary  : Templating Framework for Report Generation
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
R code for report generation. brew template syntax is similar
        to PHP, Ruby's erb module, Java Server Pages, and Python's psp
        module.

%prep
%setup -q -c -n brew

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502401258

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502401258
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library brew
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library brew
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library brew
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library brew
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/brew/DESCRIPTION
/usr/lib64/R/library/brew/INDEX
/usr/lib64/R/library/brew/Meta/Rd.rds
/usr/lib64/R/library/brew/Meta/features.rds
/usr/lib64/R/library/brew/Meta/hsearch.rds
/usr/lib64/R/library/brew/Meta/links.rds
/usr/lib64/R/library/brew/Meta/nsInfo.rds
/usr/lib64/R/library/brew/Meta/package.rds
/usr/lib64/R/library/brew/NAMESPACE
/usr/lib64/R/library/brew/R/brew
/usr/lib64/R/library/brew/R/brew.rdb
/usr/lib64/R/library/brew/R/brew.rdx
/usr/lib64/R/library/brew/Sweave-test-1-006.eps
/usr/lib64/R/library/brew/Sweave-test-1-006.pdf
/usr/lib64/R/library/brew/Sweave-test-1-007.eps
/usr/lib64/R/library/brew/Sweave-test-1-007.pdf
/usr/lib64/R/library/brew/Sweave-test-1.aux
/usr/lib64/R/library/brew/Sweave-test-1.dvi
/usr/lib64/R/library/brew/Sweave-test-1.log
/usr/lib64/R/library/brew/Sweave-test-1.orig.dvi
/usr/lib64/R/library/brew/Sweave-test-1.tex
/usr/lib64/R/library/brew/brew-test-1-1.eps
/usr/lib64/R/library/brew/brew-test-1-1.pdf
/usr/lib64/R/library/brew/brew-test-1-2.eps
/usr/lib64/R/library/brew/brew-test-1.aux
/usr/lib64/R/library/brew/brew-test-1.brew
/usr/lib64/R/library/brew/brew-test-1.dvi
/usr/lib64/R/library/brew/brew-test-1.log
/usr/lib64/R/library/brew/brew-test-1.tex
/usr/lib64/R/library/brew/brew-test-2-table.brew
/usr/lib64/R/library/brew/brew-test-2.aux
/usr/lib64/R/library/brew/brew-test-2.brew
/usr/lib64/R/library/brew/brew-test-2.dvi
/usr/lib64/R/library/brew/brew-test-2.html
/usr/lib64/R/library/brew/brew-test-2.log
/usr/lib64/R/library/brew/brew-test-2.tex
/usr/lib64/R/library/brew/brew-test-3.brew
/usr/lib64/R/library/brew/broken.brew
/usr/lib64/R/library/brew/catprint.brew
/usr/lib64/R/library/brew/example1.brew
/usr/lib64/R/library/brew/example2.brew
/usr/lib64/R/library/brew/featurefull.brew
/usr/lib64/R/library/brew/help/AnIndex
/usr/lib64/R/library/brew/help/aliases.rds
/usr/lib64/R/library/brew/help/brew.rdb
/usr/lib64/R/library/brew/help/brew.rdx
/usr/lib64/R/library/brew/help/paths.rds
/usr/lib64/R/library/brew/html/00Index.html
/usr/lib64/R/library/brew/html/R.css
